[![Build Status](https://travis-ci.com/YA7YA-H/DIARY.svg?branch=develop-challenge-2)](https://travis-ci.com/YA7YA-H/DIARY)
[![Coverage Status](https://coveralls.io/repos/github/YA7YA-H/DIARY/badge.svg?branch=develop-challenge-2)](https://coveralls.io/github/YA7YA-H/DIARY?branch=develop-challenge-2)
<a href="https://www.python.org/dev/peps/pep-0008/">
<img class="notice-badge" src="https://img.shields.io/badge/code%20style-pep8-orange.svg" alt="Badge"/>
<a href="DIARY/LICENSE.md">
<img class="notice-badge" src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="Badge"/>
</a>
</a>

**MY DIARY Api:** version 1.0

<h2>MY DIARY</h2>

A simple api for My Diary app <br>
MyDiary is an online journal where users can pen down their thoughts and feelings.
The my diary api has been beautifully designed with a endpoints functionalities that include:
creation of new user account, creation of new entries, viewing of entries, updating of entries, deletion of entries,


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

## Prerequisites

A working web browser and or a pc.
If you wish to clone the repo please satisfy the requirements in the requirements.txt

## Installing

```
install python language (preferably version 3.6)

clone the repo to your desktop/laptop

git clone https://github.com/YA7YA-H/DIARY.git

## install and run a development environment

apt-get install virtualenv -p python3 venv
apt-get install -f

```


<ol>
<h5> Navigate to the cloned repo </h5>
Navigate to the local host with your favorite browser
enjoy
<li> Activate your virtual environment </li>
<p><code>$ source venv/bin/activate</code></p>
<li> You should now see an virtual (venv) environment inside and install </li>
<p><code>$ pip install -r requirements.txt</code></p>
</ol>

## Running the Server
*Inside the virtualenv*
<br>
Start the server at localhost:5000 by running the following command:
```
python3 run.py
```


<span>you should now see a local host ```127.0.0.1:5000```
. Navigate to the local host and you should see a beautiful documentation of
flask restplus of an API with endpoints
</span>

<h3>Running  the test</h3>

<p>Testing has been implemented using the unit testing framework of the Python language. To run tests, use the following command:</p>
<p><code>$ pytest</code></p>

```
#run
pip3 install pytest

pytest /path/to/repo

### Breaking down the tests
These tests ensure Users are registered login credentials are secure, entries are created and are able to be modified
example below

```


### Api endpoints

| url | Method|  Description| Authentication |
| --- | --- | --- | --- |
| /api/v1/auth/register | POST | Registers new user | FALSE
| /api/v1/auth/login | POST | Sign in a user and generate token | TRUE
| /api/v1/auth/logout | GET | Logs out an authenticated user | TRUE
| /api/v1/users/entries | GET | Fetch all entries of an authenticated user|TRUE
| /api/v1/users/entries/contentId} | GET | Get an entry with {id}  of an authenticated user|TRUE
| /api/v1/users/entries | POST | Create a new entry of an authenticated user|TRUE
| /api/v1/users/entries/contentId} | PUT | Update an entry with {id} of authenticated user|TRUE
| /api/v1/users/entries/contentId} | DELETE | Delete an entry  with {id} of authenticated user|TRUE

<h3>Test Example</h3>


```
    def test_api_invalid_email(self):
        """Test for invalid email in signin endpoint"""
        response = self.client.post(
            '/api/v1/auth/signup',
            data=json.dumps(self.user_registration),
            content_type="application/json")
        self.assertEqual(response.status_code, 201)
        response = self.client.post(
            '/api/v1/auth/login',
            data=json.dumps({
                "Email": "John@example.com",
                "Password": "its26uv3nf"
            }),
            content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'],
                         'Failed, Invalid email! Please try again')
        self.assertEqual(response.status_code, 401)
```
## Need for test

To ensure maintainability of code in future developments
This ensures no new code breaks our already existing code

Note: Travis-ci ensures continous integration and runs test automatically for this build

## Deployment

Heroku app live-demo https://mydiry2k18.herokuapp.com/

## Built With
**Powered by Flask!**
* [_FLASK_RESTPLUS_] - For restful API
* [Dependencies in requirements.txt] - Dependency Management
*
## Contributing

Contributions would be highly appreciated, Help out and make a pull request, and the process for submitting pull requests to me.


## GH-PAGES TEMPLATE
 https://ya7ya-h.github.io/DIARY/UI/Design/front.html


## Authors

* **YAHYA HUSSEIN**


## COMPANY

* **ANDELA KENYA**

## License

This project is licensed under the GNU License - see the [LICENSE.md](LICENSE.md) file for details
