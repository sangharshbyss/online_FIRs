
import smtplib, ssl


port = 465  # For SSL
password = "ManDlac@2020"

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("mail.manuski.in", port, context=context) as server:
    server.login("dlac@manuski.in", password)

    sender = 'dlac@manuski.in'
    receivers = ['sangharshbyss@gmail.com']

    message = """From: From Person <from@fromdomain.com>
    To: To Person <to@todomain.com>
    Subject: SMTP e-mail test
    
    This is a test e-mail message.
    """


    smtpObj = smtplib.SMTP('localhost')
    smtpObj.sendmail(sender, receivers, message)
print("Successfully sent email")
