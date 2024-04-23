# GwardiaHub Project 🌐

## 📄 About the project

We want to create website with Django, that will be useful to as many as three different user groups!

- Our classmates
- [Gwardia Czapli](https://github.com/Gwardia-Czapli/) members
- Genshin Impact players from both of above

### Modules

- For all our classmates:
  - information about lunch menu for given day,
  - calendar with events from Mobidziennik and other events, that our class want to include,
  - information about our homeworks with option to submit solution.
- For [Gwardia Czapli](https://github.com/Gwardia-Czapli/) members:
  - information about next meetings,
  - place to submit feedback about meetings,
  - assignments given on meetings.
- For Genshin Impact players:
  - TBD
  - Few ideas to enhance the game:
1)wish simulator(and list of the characters you've collected already)
2)future banners info (duration, which characters)
3)events info (duration, next events, rewards)
4)a table(or smt like that) containing incoming daily hoyolabs in/pop-up notification about next daily hoyolabs in
5)expanded ui design (later when the common one is finished, genshin inspired)

## 🛠️ Installation guide for contributors

### Installation

1. Install [git](https://git-scm.com/downloads)
2. In terminal go to folder where you want to have this repository, fe. Documents and enter `git clone https://github.com/Gwardia-Czapli/GwardiaHub` command
3. Install [python-poetry](https://python-poetry.org/)
4. In terminal go to repository folder (if we follow example from 2. it will be Documents/GwardiaHub) and enter `poetry install` 
5. Install [pre-commit](https://pre-commit.com/)
6. In terminal go to repository folder and enter and `pre-commit install`
7. Open IDE (preferably PyCharm) and with `Open folder` option open repository folder as project in your IDE
8. Install Docker and Docker Compose

### Server running

1. If you installed Docker Desktop open it
2. Open terminal in repo folder 
3. Enter `docker compose up` 
4. Open new terminal window
5. Enter `python manage.py runserver`
