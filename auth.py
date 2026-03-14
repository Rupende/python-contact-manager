import hashlib
import os

USERS_FILE = "users.txt"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register_user(username, password):

    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as file:
            for line in file:
                saved_user, _ = line.strip().split(",")
                if saved_user == username:
                    return False

    hashed = hash_password(password)

    with open(USERS_FILE, "a") as file:
        file.write(username + "," + hashed + "\n")

    return True


def login_user(username, password):

    if not os.path.exists(USERS_FILE):
        return False

    hashed = hash_password(password)

    with open(USERS_FILE, "r") as file:
        for line in file:
            saved_user, saved_pass = line.strip().split(",")
            if saved_user == username and saved_pass == hashed:
                return True

    return False