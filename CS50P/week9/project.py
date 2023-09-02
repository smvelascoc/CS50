import sys
from os import system
import time
import requests
from validators import email as ch_email
from email.message import EmailMessage as Mail
import smtplib
import ssl
from getpass_asterisk.getpass_asterisk import getpass_asterisk
from bs4 import BeautifulSoup as bs

remitly = {"value": {"url": "https://www.remitly.com/fr/es/colombia", "type": "h2", "class": "fg6m42n" },
           "fee": {"url": "https://www.remitly.com/fr/es/colombia/pricing", "type": "div", "class": "f1vybcs fnsgms5" }}

def main():
    try:
        targ = get_float("Target rate: ")

        while True:
            #emfrom = get_email("Email from: ")
            emfrom = "bot.smvelascoc@gmail.com"
            password = getpass_asterisk()

            if check_connection(emfrom, password):
                #print("Connection done")
                break

        emto = get_email("Email to notify: ")

        while True:
            cop = get_value_url(remitly["value"])
            fee = get_value_url(remitly["fee"])
            if (cop > 0) and (fee > 0):
                cop_c = cop - 150

                if cop_c >= targ:
                    print(f"Target reached: {cop_c} COP")
                    sendmail(emfrom, password, emto, create_message(cop_c))
                    break
                else:
                    #system("clear")
                    print("Waiting for best rate")
                    time.sleep(300)

    except ssl.SSLError:
        sys.exit("Error in SSL protocol. Notification cannot be sent")

    except smtplib.SMTPAuthenticationError:
        sys.exit("Authentification error")

    except smtplib.SMTPNotSupportedError:
        sys.exit("Problem with server connection")

    except KeyboardInterrupt:
        sys.exit("\nProgram aborted")

def get_float(msg=""):
    while True:
        try:
            a = float(input(msg))
            if a > 0:
                return a
        except ValueError:
            print("No valid entry")

def get_email(msg=""):
    while True:
        mail = input(msg)
        if ch_email(mail):
            return mail

def get_value_url(pw):
    try:
        page = requests.get(pw["url"])
        if page:
            s = bs(page.content, "html.parser")
            result = s.find_all(pw["type"], {"class": pw["class"]}, limit=3)
            val = float(result[2].text.strip().removesuffix("COP").removeprefix("€").replace(",","."))
        else:
            page.raise_for_status()

    except requests.exceptions.HTTPError:
        print("URL error")
        return -1

    except IndexError:
        print("No value found")
        return -2

    except ValueError:
        print("Error in value conversion")
        return -3

    return val

def check_connection(user, password):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)
    server.login(user, password)
    server.quit()
    return True

def create_message(rate):
    msg = Mail()
    msg["Subject"] = "Your target rate has been reached"
    msg.set_content(f"Your target rate has been reached.\nThe actual exchange rate is 1EUR = {rate:.1f} COP")
    return msg

def sendmail(sender, password, receiver, message):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",465, context=context)
    server.login(sender, password)
    server.send_message(message, sender, receiver)
    server.quit()

if __name__ == "__main__":
    main()