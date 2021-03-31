# Heroku-Scheduled-Python-App

This is a sample python app for Heroku that executes using cronjob ( schuedling ) without using any external resources required like using weblink.

I prefer to use a free Addon named `Heroku Scheduler` https://elements.heroku.com/addons/scheduler

Make sure you have [Python 3](https://www.python.org/downloads/) and the [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) installed.

## Steps:

- [ ] Fork this repo.
- [ ] Modify the file `code.py` according to your need.
- [ ] Create a virtual environment for your app. `py -m venv venv-name-here`.
- [ ] Activate that virtual environment.
- [ ] Install all required libraries for your python app in that environment.
- [ ] Replace the link of repo in `app.json` inside `repository`.
- [ ] Run the script `pip freeze > requirements.txt`.
- [ ] Commit and push the code.
- [ ] Star this repo if that helped you 😊.

## Installation:

```
$ heroku create
$ git push heroku main

$ heroku run python code.py
```

or

[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

## Documentation

For more information about using Python on Heroku, see these Dev Center articles:

- [Python on Heroku](https://devcenter.heroku.com/categories/python)
- [Heroku Scheduling](https://devcenter.heroku.com/articles/scheduler#scheduling-jobs)

## License

[MIT](https://choosealicense.com/licenses/mit/)
