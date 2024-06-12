from datetime import datetime, timedelta

import requests
from django.core.handlers.wsgi import WSGIRequest
from django.urls import reverse
from django.utils import timezone
from requests.exceptions import JSONDecodeError

from core.models import User, UserRole
from gwardia_hub.settings import CLIENT_ID, CLIENT_SECRET, GUILD_ID

API_ENDPOINT = "https://discord.com/api/v10"
DISCORD_TOKEN_COOKIE = "discord_access_token"
DISCORD_REFRESH_COOKIE = "discord_refresh_token"
DISCORD_ID_COOKIE = "discord_id"


def authorise_code(request: WSGIRequest) -> dict[str, str] | None:
    """Returns HTTP JSON response from Discord API or None when authorization fails."""
    code = request.GET.get("code")
    if code is None:
        return None

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": request.build_absolute_uri(reverse("core:discord_code")),
    }
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        f"{API_ENDPOINT}/oauth2/token",
        data=data,
        headers=headers,
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
    if not response.ok:
        return None
    return response.json()


def refresh_access_token(refresh_token):
    data = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    response = requests.post(
        f"{API_ENDPOINT}/oauth2/token",
        data=data,
        headers=headers,
        auth=(CLIENT_ID, CLIENT_SECRET),
    )
    if not response.ok:
        return None
    return response.json()


def fetch_user(access_token: str) -> User | None:
    json = json_api_get("/oauth2/@me", access_token)
    if json is None:
        return None

    user = User.objects.get_or_create(discord_id=json["user"]["id"])[0]
    user.username = json["user"]["global_name"] or json["user"]["username"]
    user.avatar_hash = json["user"]["avatar"]
    if user.data_valid_until < timezone.now():
        if fetch_user_details(access_token):
            user.data_valid_until = datetime.now() + timedelta(minutes=10)
    user.save()

    return user


def fetch_user_details(access_token: str) -> bool:
    """
    :param access_token: access token for Discord API
    :return: True if data was fetched successfully
    """
    json = json_api_get(f"/users/@me/guilds/{GUILD_ID}/member", access_token)
    if json is None:
        return False

    user = User.objects.get_or_create(discord_id=json["user"]["id"])[0]
    for role_id in json["roles"]:
        try:
            role = UserRole.objects.get(id=role_id)
            user.roles.add(role)
        except UserRole.DoesNotExist:
            pass
    return True


def json_api_get(endpoint: str, access_token: str):
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(
        f"{API_ENDPOINT}{endpoint}",
        headers=headers,
    )
    if not response.ok:
        return None
    try:
        return response.json()
    except JSONDecodeError:
        return None