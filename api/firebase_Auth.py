import pyrebase
def login_firebase():
    config = {
    'apiKey': "AIzaSyAaVMbSG1wJqs7o8dCk_PusI73Vuv28u1Q",
    'authDomain': "gd-clone.firebaseapp.com",
    'databaseURL': "https://gd-clone.firebaseio.com",
    'projectId': "gd-clone",
    'storageBucket': "gd-clone.appspot.com",
    'messagingSenderId': "471108653289",
    'appId': "1:471108653289:web:dc3d2302252a0b86"
  }
    firebase=pyrebase.initialize_app(config)
    auth=firebase.auth()
    email='gd@gmail.com'
    password='123456'
    try:
        auth.sign_in_with_email_and_password(email,password)
        message="login_succesfull"
    except:
        message="invalid credentials"
    return message