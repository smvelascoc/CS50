from pytest import raises
from project import create_message, get_value_url, check_connection
from email.message import EmailMessage as Mail
from smtplib import SMTPAuthenticationError as AuthError


def test_create_message():
    msg = Mail()
    msg.set_content("Your target rate has been reached.\nThe actual exchange rate is 1EUR = 4500.0 COP")
    assert create_message(4500).get_content() == msg.get_content()

def test_get_value_url():
    value = {"url": "https://www.remitly.com/fr/es/colombie", "type": "h2", "class": "fg6m42n" }
    assert get_value_url(value) == -1

def test_check_connection():
    user="noadress@gmail.com"
    password="NoPassword"
    with raises(AuthError):
        assert check_connection(user,password)