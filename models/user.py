user_data = {}
from flask_bcrypt import Bcrypt


class User:
    """Class for user"""

    def __init__(self, firstname, lastname, email, password):
        global user_data
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password_hash = Bcrypt().generate_password_hash(password).decode(
            'UTF-8')

    def create(self):
        user = {
            self.email: {
                "FirstName": self.firstname,
                "LastName": self.lastname,
                "Email": self.email,
                "Password": self.password_hash
            },
        }
        return user_data.update(user)
