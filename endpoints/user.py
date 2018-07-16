from flask_restplus import Resource, Namespace, fields
from flask import request
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
