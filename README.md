# Google_Drive_Clone_API

This is an API that can download, upload and delete files stored in Firebase Storage.
This is written in python using Django, rest-framework and pyrebase libraries

# Setup

Make a firebase account > Create a project > Make a user account > Copy the config file api/config.py and follow instruction

**Update **the email and password in Firebase_Auth file

Then make activate Firebase storage _select firebase storage_ and change the rules to allow for reading and writing remotely

`service firebase.storage { match /b/{bucket}/o { match /{allPaths=**} { allow read, write: if true; } } }`

To activate admin priviledges create a service account and download the Admin SDK configuration snippet

Set the path of the json in config.py file

# Usage

For convience there are 3 user accounts already added

Username>Password

admin>q7w8e9a4s5d6

TestUser>testing321

NewUser>testing321

Create a superuser to have admin access

> python manage.py createsuperuser

To add users go to admin site _127.0.0.1:8000/admin_

Run django app using

> python manage.py runserver

Without login you won't be able to access anything.Login into site.

Use postman app for querying requests.

# Libraries

Install Django, Pyrebase, rest-framework

# Uploading

In postman add your credentials for authorization, send a file request (form-data).

Name of the file will be auto-filled. But you can give it a name you want during request.

The selected file will be copied to **/media** and uploaded to filebase at username/file_name

# Deleting

Go to single entry view by _(enter pk of the relevant entry)_

> 127.0.0.1:8000/pk

A delete option will appear

# Downloading

To download just press the POST button in single entry view. The file will be downloaded to base directory
