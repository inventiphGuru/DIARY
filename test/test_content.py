import unittest
import os
import json
from flask import Flask
from app.app import create_app


class EntryTestCase(unittest.TestCase):
    """Test Entry content in app"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client()
        self.user_registration = {
            "FirstName": "John",
            "LastName": "Doe",
            "Email": "John_Doe@example.com",
            "Password": "its26uv3nf"
        }
        self.user_login = {
            "Email": "John_Doe@example.com",
            "Password": "its26uv3nf"
        }
        self.data = {
            "ContentID": 1,
            "Date": "01/01/18",
            "Content": "I had fun at the zoo"
        }

    def test_api_get_entries_without_token(self):
        """Test get entries without token"""
        response = self.client.get(
            'api/v1/user/entries',
            data=json.dumps(self.data),
            content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result['Message'],
                         "Unauthorized, access token required!")
        self.assertEqual(response.status_code, 401)

    def test_api_can_get_all_entries(self):
        """Test API can GET all entries """
        #Signup
        signup = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.user_registration),
            content_type="application/json")
        self.assertEqual(signup.status_code, 201)

        #Login
        login = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps(self.user_login),
            content_type="application/json")
        result = json.loads(login.data)
        self.assertEqual(result['message'], 'Successfully login.')
        self.assertEqual(login.status_code, 201)

        #entries
        access_token = json.loads(login.data.decode())['auth_token']
        response = self.client.get(
            'api/v1/user/entries',
            data=json.dumps(self.data),
            content_type="application/json",
            headers=dict(access_token=access_token))
        self.assertEqual(response.status_code, 200)

    # def test_400_post_entries(self):
    #     """Test bad request on post method"""
    #     empty = self.client.post(
    #         'api/v1/user/entries', data={}, content_type="application/json")
    #     self.assertEqual(empty.status_code, 400)

    # def test_api_post_entries(self):
    #     """Test API url [POST] api/user/entries"""
    #     response = self.client.post(
    #         'api/v1/user/entries',
    #         data=json.dumps(self.data),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)

    # def test_api_get_single_entry(self):
    #     """Test API url [GET] api/user/{id}"""
    #     response = self.client.post(
    #         "api/v1/user/entries",
    #         data=json.dumps(self.data),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)
    #     response1 = self.client.get('api/v1/user/entries/1')
    #     self.assertEqual(response1.status_code, 200)

    # def test_404_get_single_entry(self):
    #     response = self.client.get("/api/user/entry/3")
    #     self.assertEqual(response.status_code, 404)

    # def test_api_update_entry_with_id(self):
    #     """Test API url [PUT] api/user/entries"""
    #     response = self.client.post(
    #         'api/v1/user/entries',
    #         data=json.dumps(self.data),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)
    #     response = self.client.put(
    #         'api/v1/user/entries/1',
    #         data=json.dumps({
    #             "Date": "02/02/18",
    #             "Content": "Updated I had fun at the zoo"
    #         }),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)

    # def test_404_PUT_entries(self):
    #     """Test bad entry on [PUT] method"""
    #     bad_content = self.client.put(
    #         'api/v1/user/entries/1',
    #         data={
    #             "Date": "18/18/2018",
    #             "Content": "Invalid id "
    #         },
    #         content_type="application/json")
    #     self.assertEqual(bad_content.status_code, 404)

    # def test_api_400_invalid_parameter(self):
    #     """Test status_code 400 [PUT] for api/user/entries/<id>"""
    #     response = self.client.post(
    #         'api/v1/user/entries',
    #         data=json.dumps(self.data),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)
    #     response = self.client.put(
    #         'api/v1/user/entries/0', data={}, content_type="application/json")
    #     self.assertEqual(response.status_code, 400)

    # def test_delete_an_entry(self):
    #     """Test API resource [DELETE] endpoint url api/user/entries/<id>"""
    #     response = self.client.post(
    #         'api/v1/user/entries',
    #         data=json.dumps(self.data),
    #         content_type="application/json")
    #     self.assertEqual(response.status_code, 201)
    #     response = self.client.delete('api/v1/user/entries/1')
    #     self.assertEqual(response.status_code, 201)

    # def test_del_status_400_invalid_id(self):
    #     """Test API resource [DELETE] endpoint url api/user/entries/<id>"""
    #     response = self.client.delete('api/v1/user/2')
    #     self.assertEqual(response.status_code, 404)
