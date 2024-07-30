# 0x02. i18n

## Back-end

![ALWAYS](https://private-user-images.githubusercontent.com/125453474/302601105-4274bad0-5d45-4ff0-8e8d-726442c6ea81.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMjM1MTUsIm5iZiI6MTcyMjMyMzIxNSwicGF0aCI6Ii8xMjU0NTM0NzQvMzAyNjAxMTA1LTQyNzRiYWQwLTVkNDUtNGZmMC04ZThkLTcyNjQ0MmM2ZWE4MS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDczMFQwNzA2NTVaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0yYmZlZTNiZDI3NWQ4NDdlM2NlOTk2NGUwMjE0YmYyMTQ1ODc2MTE4NDExMjNmYWNlOTc2ZThhY2FiZGJmMjAxJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.AmcVNo_0P3rmTeX2JsoMpqYPrb6XI9elKPLmJCv1Nmg)

## Resources

### Read or watch:

  - [Flask-Babel](https://web.archive.org/web/20201111174034/https://flask-babel.tkte.ch/)
  - [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
  - [pytz](https://sourceforge.net/directory/software-development/linux/)

## Learning Objectives 📖

At the end of this project, you are expected to be able to [explain to anyone](https://fs.blog/feynman-learning-technique/), without the help of Google:

  - Learn how to parametrize Flask templates to display different languages
  - Learn how to infer the correct locale based on URL parameters, user settings or request headers
  - Learn how to localize timestamps

## Requirements

  - All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
  - All your files should end with a new line
  - A `README.md` file, at the root of the folder of the project, is mandatory
  - Your code should use the pycodestyle style (version 2.5)
  - The first line of all your files should be exactly `#!/usr/bin/env python3`
  - All your `*.py` files should be executable
  - All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
  - All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
  - All your functions and methods should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
  - A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
  - All your functions and coroutines must be type-annotated.

# Tasks 📃

## 0. Basic Flask app

First you will setup a basic Flask app in `0-app.py`. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

__Repo:__

  - GitHub repository: `alx-backend`
  - Directory: `0x02-i18n`
  - File: `0-app.py, templates/0-index.html`

## 1. Basic Babel setup

Install the Babel Flask extension:

    $ pip3 install flask_babel==2.0.0

Then instantiate the `Babel` object in your app. Store it in a module-level variable named `babel`.

In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.

Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).

Use that class as config for your Flask app.

__Repo:__

  - GitHub repository: `alx-backend`
  - Directory: `0x02-i18n`
  - File: `1-app.py, templates/1-index.html`

## 2. Get locale from request

Create a `get_locale` function with the `babel.localeselector` decorator. Use `request.accept_languages` to determine the best match with our supported languages.

__Repo:__

  - GitHub repository: `alx-backend`
  - Directory: `0x02-i18n`
  - File: `2-app.py, templates/2-index.html`

## 3. Parametrize templates

Use the `_` or `gettext` function to parametrize your templates. Use the message IDs `home_title` and `home_header`.

Create a `babel.cfg` file containing

    [python: **.py]
    [jinja2: **/templates/**.html]
    extensions=jinja2.ext.autoescape,jinja2.ext.with_

Then initialize your translations with

    $ pybabel extract -F babel.cfg -o messages.pot .

and your two dictionaries with

    $ pybabel init -i messages.pot -d translations -l en
    $ pybabel init -i messages.pot -d translations -l fr

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid       | English                 | French                     |
|-------------|-------------------------|----------------------------|
| home_title  | "Welcome to Holberton"  | "Bienvenue chez Holberton" |
| home_header | "Hello world!"          | "Bonjour monde!"   

Then compile your dictionaries with

    $ pybabel compile -d translations

Reload the home page of your app and make sure that the correct messages show up.

__Repo:__

  - GitHub repository: `alx-backend`
  - Directory:` 0x02-i18n`
  - File: `3-app.py, babel.cfg, templates/3-index.html, translations/en/LC_MESSAGES/messages.po, translations/fr/LC_MESSAGES/messages.po, translations/en/LC_MESSAGES/messages.mo, translations/fr/LC_MESSAGES/messages.mo`

## 4. Force locale with URL parameter

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

Visiting `http://127.0.0.1:5000/?locale=fr` __should display this level 1 heading:__

![MONDE](https://private-user-images.githubusercontent.com/125453474/302606307-3940de33-ce26-4575-9c48-1726b47c64fa.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMjQ5MDMsIm5iZiI6MTcyMjMyNDYwMywicGF0aCI6Ii8xMjU0NTM0NzQvMzAyNjA2MzA3LTM5NDBkZTMzLWNlMjYtNDU3NS05YzQ4LTE3MjZiNDdjNjRmYS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDczMFQwNzMwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0wMTUxZWVmNzM5MmMzMjE4OWJmZmI5OWJkNGU4NzE5YmExMDc5NWNiMmYwNGM1ZWVmYTM2MWE2M2YxNDc2YmE1JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.n8nkzSE6f_PIsiveGVb3R1Y0X_WnQQwlVSoIwrCsBTc)

## 5. Mock logging in

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.

    users = {
        1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
        2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
        3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
        4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
    }

This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user `to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| msgid        | English                                     | French                                    |
|--------------|---------------------------------------------|-------------------------------------------|
| logged_in_as | "You are logged in as %(username)s."        | "Vous êtes connecté en tant que %(username)s." |
| not_logged_in| "You are not logged in."                    | "Vous n'êtes pas connecté."               |

Visiting `http://127.0.0.1:5000/` in your browser should display this:

![WORLD](https://private-user-images.githubusercontent.com/125453474/302607411-6df1964e-0124-4071-b720-75f3505b0780.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMjQ5MDMsIm5iZiI6MTcyMjMyNDYwMywicGF0aCI6Ii8xMjU0NTM0NzQvMzAyNjA3NDExLTZkZjE5NjRlLTAxMjQtNDA3MS1iNzIwLTc1ZjM1MDViMDc4MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDczMFQwNzMwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1lYWQzZmM5MzI5OWEyMjVhNzAxOWZjY2I5YzQyZWVlM2M0OWY1YjdkYzBhZGM2NmFlZTEwZmZhM2I3Y2NjMzRhJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.FsDiRXTF6KY26ZEABj6OFaMCHygPZDXMpYp5oMg7EiE)

Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:

![HELLO](https://private-user-images.githubusercontent.com/125453474/302607652-90f601c3-2113-4992-be40-b6d21d4846f7.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjIzMjQ5MDMsIm5iZiI6MTcyMjMyNDYwMywicGF0aCI6Ii8xMjU0NTM0NzQvMzAyNjA3NjUyLTkwZjYwMWMzLTIxMTMtNDk5Mi1iZTQwLWI2ZDIxZDQ4NDZmNy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQwNzMwJTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MDczMFQwNzMwMDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1kYjUwNzFhOTc3NDNjZDZlZmViN2VlZmNmNWY4MTVmMTBkOGU0YjhlMjk3MTk0NDQzMDVhNjFjOTc3MDA3ZjdmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZhY3Rvcl9pZD0wJmtleV9pZD0wJnJlcG9faWQ9MCJ9.bPFSL9sxRHaaI7S2-OX3JF71Bo3YSv2G_vfRlY6MwRI)

