from flask_restplus import Resource, Namespace, fields
from flask import request
from flask_bcrypt import Bcrypt
from models.user import user_data, User

auth_namespace = Namespace(
    'auth', description="Handle Authentification Related Operation")

registration_model = auth_namespace.model(
    "Registration", {
        "FirstName":
        fields.String(
            required=True, description='Your First Name', example='John'),
        "LastName":
        fields.String(
            required=True, description='Your Last Name', example='Doe'),
        "Email":
        fields.String(
            required=True,
            description='your email accounts',
            example='John_Doe@example.com'),
        "Password":
        fields.String(
            required=True,
            description='Your secret password',
            example='its26uv3nf')
    })

login_model = auth_namespace.model(
    'Login', {
        "Email":
        fields.String(
            required=True,
            description='your email accounts',
            example='John_Doe@example.com'),
        "Password":
        fields.String(
            required=True,
            description='Your secret password',
            example='its26uv3nf')
    })


@auth_namespace.route("/signup")
class Signup(Resource):
    """Handles api registration url api/auth/signup."""

    @auth_namespace.doc('create new user')
    @auth_namespace.expect(registration_model)
    def post(self):
        """create a new user to database"""
        data = request.get_json()
        first_name = data['FirstName']
        last_name = data['LastName']
        email = data['Email']
        password = data['Password']

        user = User(first_name, last_name, email, password)
        user.create()

        return {
            'status': 'success',
            'message': 'Successfully registered.'
        }, 201


@auth_namespace.route('/login')
@auth_namespace.doc(
    responses={
        201: 'Successfully login',
        401: 'Invalid credential'
    },
    security=None,
    body=login_model)
class Login(Resource):
    """Handles api registration url api/auth/signin."""

    def post(self):
        """Handle POST request for login"""
        post = request.get_json()
        user_email = post['Email']
        user_password = post['Password']

        if user_email in user_data:
            if Bcrypt().check_password_hash(user_data[user_email]["Password"],
                                            user_password):
                return {
                    'status': 'success',
                    'message': 'Successfully login.'
                }, 201
            else:
                return {
                    "message": "Failed, Invalid password! Please try again"
                }, 401
        else:
            return {"message": "Failed, Invalid email! Please try again"}, 401