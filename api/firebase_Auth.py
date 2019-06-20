import pyrebase

config = {}


def firebase_define(configs):
    """
    Creates a Firebase instance
    """
    config = configs
    firebase = pyrebase.initialize_app(config)
    return firebase


def default_login_firebase(configs):
    """Logs into Firebase using the credentials stored in configs
    
    Arguments:
        configs {dict} -- Stores User credentials
    """
    config = configs
    firebase = firebase_define(config)
    auth = firebase.auth()
    # TODO Enter email and password of the Firebase user account where you want those data to be stored.
    """ Under Authentication tab go to sign in method and select email and password as a method to sign in, 
    create a account and fill those same details below. """
    email = "gd@gmail.com"
    password = "123456"
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        message = "LOGIN_SUCCESSFULL"
    except:
        message = "INVALID_CREDENTIALS"

    user = auth.refresh(user["refreshToken"])
    user["idToken"]
    print(message)

