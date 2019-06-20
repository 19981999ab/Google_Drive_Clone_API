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
    "apiKey": "AIzaSyAaVMbSG1wJqs7o8dCk_PusI73Vuv28u1Q",
    "authDomain": "gd-clone.firebaseapp.com",
    "databaseURL": "https://gd-clone.firebaseio.com/",
    "projectId": "gd-clone",
    "storageBucket": "gd-clone.appspot.com",
    "messagingSenderId": "471108653289",
    "appId": "1:471108653289:web:dc3d2302252a0b86",
}
configs_delete = {
    "apiKey": "AIzaSyAaVMbSG1wJqs7o8dCk_PusI73Vuv28u1Q",
    "authDomain": "gd-clone.firebaseapp.com",
    "databaseURL": "https://gd-clone.firebaseio.com/",
    "projectId": "gd-clone",
    "storageBucket": "gd-clone.appspot.com",
    "messagingSenderId": "471108653289",
    "appId": "1:471108653289:web:dc3d2302252a0b86",
    "serviceAccount": "D:\\Python\\Django\\gd_api_clone\\api\\gd-clone-firebase-adminsdk-gnth9-7bd3a3934b.json",
}

