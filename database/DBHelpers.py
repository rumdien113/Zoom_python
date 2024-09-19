import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCTvWEv-raCwRbFsrr6_EBIxiWITGyNS8c",
    'authDomain': "zoom-6168e.firebaseapp.com",
    'databaseURL': "https://zoom-6168e-default-rtdb.firebaseio.com",
    'projectId': "zoom-6168e",
    'storageBucket': "zoom-6168e.appspot.com",
    'messagingSenderId': "696910928874",
    'appId': "1:696910928874:web:ead4f53ee7d12e94a83093",
    'measurementId': "G-W61LY98BH9"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()


def registerDB(email, password):
    if len(password) < 6:
        print("Password should be at least 6 characters.")
        return False

    try:
        user = auth.create_user_with_email_and_password(email, password)
        print(user)
        return True
    except Exception as e:
        print(f"Error: {e}")


def loginDB(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return user
    except Exception as e:
        print(f"Error: {e}")
        return None
