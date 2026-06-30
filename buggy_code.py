import os

# Bug 1 : Mot de passe hardcodé (sécurité critique)
password = "admin123"
SECRET_KEY = "hardcoded_secret_key_xyz"
API_TOKEN = "ghp_faketoken123456"

# Bug 2 : Division sans vérification
def divide(a, b):
    return a / b

# Bug 3 : Index sans vérification
def get_item(my_list, index):
    return my_list[index]

# Bug 4 : SQL Injection
def get_user(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query
