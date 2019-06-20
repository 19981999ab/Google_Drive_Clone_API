"""Contains the config of Firebase stored in a dictionary

Example:
{"apiKey":"  "
"authDomain":"   "
}

config_upload should contain the following fields: 
"apiKey"
"authDomain"
"databaseURL"
"projectId"
"storageBucket"
"messagingSenderId"
"appId"

config_download should include in addition "serviceAccount" field which gives admin access to delete storage class.
serviceAccount contains the path of service_Account details stored in json format. 
Example:
"serviceAccount":"D:gd_api_clone\\gd-clone-firebase-adminsdk.json"

"""
# TODO Fill up ### configs_upload and configs_delete using your firebase credentials
configs_upload = {
    "apiKey": "###",
    "authDomain": "###",
    "databaseURL": "###",
    "projectId": "###",
    "storageBucket": "###",
    "messagingSenderId": "###",
    "appId": "###",
}
configs_delete = {
    "apiKey": "###",
    "authDomain": "###",
    "databaseURL": "###",
    "projectId": "###",
    "storageBucket": "###",
    "messagingSenderId": "###",
    "appId": "###",
    "serviceAccount": "###",
}

