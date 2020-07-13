## Awwwards

[![codebeat badge](https://codebeat.co/badges/a15c910b-012e-4f1b-b404-93db3562013c)](https://codebeat.co/projects/github-com-rosekairu-awwwards-master)

### Author: [rosekairu](https://github.com/rosekairu)

### Description
 
A django application that allows a user to post a project he/she has created and get it reviewed by his/her peers.

## Live Link

[View Site](https://sites-awwwards.herokuapp.com/)

### Setup/Installation Requirements

* Github and Heroku account - from where the application can be cloned or downloaded
* Git installed in pc - for downloading the application to interact with it locally i.e. on one's device
* Text Editor e.g. Visual Studio or Atom or pycharm - for creating, viewing and editing the code.
* A CLI (Command Line Interface) or terminal where the user can interact with the application using the various python commands e.g. python3.6 run.py or test commands.
* Browser - from where to view and further interact with the application

## Development Installation

To get the code...

1. Clone the repository:

  ```bash
  https://github.com/rosekairu/Awwwards.git
   ```

2. Move to the folder:

  ```bash
  cd Awwwards
  ```

3. Install requirements:

  ```bash
  pip install -r requirements.txt
  ```

4.Migrate the database:

  ```bash
  python manage.py migrate
  ```
  
 5.Create a superuser:

  ```bash
  python manage.py createsuperuser
  ```
  
6.Testing the application

  ```bash
  python3.6 manage.py test
  ```
  
  7.Set the required environment variables.

  ```bash
  cp .env.example .env : copy environment example config.
  Edit the variables to suit your Claudinary account. If you don't have one, create it.
  source .env : export the environment variables.
  ```
  
8.Running the application

  ```bash
  python manage.py runserver
  ```
 Open the application on your browser `127.0.0.1:8000`

## USER INTERACTION

1. To run the application, type python manage.py runserver (if cloned the repo)
```
or
```
2. Click on the provided link
3. Browse through the apps/sites
3. Register or Sign In
4. The homepage will then be displayed

### Known Bugs


### Technologies Used

1. Python3.6
2. Django3
3. Postgres
4. Bootstrap
5. HTML
6. CSS

### Support and contact details

If you have any comments, suggestions, questions, and/or contributions, please email me at [rosekairu@gmail.com]

### [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/rosekairu/Awwwards/blob/master/LICENSE) <br>

Copyright (c) **Rose Kairu June 2020**
