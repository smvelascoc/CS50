    # COP currency follow script
    #### Video Demo:  <https://youtu.be/DyXfki_7xkM>
    #### Description:
    This program allow user to follow the price from a well-known exchange currency to send money from Europe to Colombia. With this program you can set a target exchange rate.
    The script will check each 5 minutes the exchange rate. If the target is reached, the script will automatically send an email alert from the user, password already recovered to the notification email. For purpose of the exercise, a 'bot' email' has been created to send the automatic notification.

    So as first step, the program will login into the email to check if user and password are correct, it will proceed. If not, the program will exit. The idea is to ensure that all the information for the notification is correct before starting to look for the exchange rate.

    The script starts asking basic information as, the target rate and the information about the email from where the notification will be sent. Using the library 'getpass-asterisk' receive the password. After, the notification email is asked and tested using validators library.

    Then, next step is, using the library 'Beautiful Soup' the webpage is scrapped to obtain the current rate. The rate is corrected using the commission fee scrapped to from the webpage. At this point, several possible errors can be reached. The function is fliexible enough to catch all this errors and continue the checking later.

    If the exchange is not higher than target, the script waits 5 minutes to check again. This delay is chosen to avoid over request the webserver to avoid be banned.

    Once the target is reached, using the ssl library, an email is created and send to notify the target reached and the script ends. 