import pyrebase
from .firebase_Auth import firebase_define, default_login_firebase
from firebase import firebase
import os
from django.conf import settings
from .config import *

url = {}


def upload_file(file_name, user_id):
    firebase = firebase_define(configs_upload)
    default_login_firebase(configs_upload)
    storage = firebase.storage()
    myfile = open(os.path.join(settings.MEDIA_ROOT, file_name), "rb")
    print(myfile)
    byts = myfile.read()
    url = storage.child(user_id).child(file_name).put(byts)
    print(url)
    return storage.child(user_id).child(file_name).get_url(url["downloadTokens"])


def download_file(file_name, user_id):
    firebase = firebase_define(configs_upload)
    storage = firebase.storage()
    storage.child(os.path.join(user_id, file_name).replace(os.sep, "/")).download(
        file_name
    )


def delete_file(file_name, user_id):
    firebase = firebase_define(configs_delete)
    storage = firebase.storage()
    storage.child().delete(os.path.join(user_id, file_name).replace(os.sep, "/"))
