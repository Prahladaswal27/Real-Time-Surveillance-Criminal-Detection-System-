import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import getpass

def send_email(subject, body, to_email, from_email, from_password):
    # Create the container (outer) email message.
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create the server object
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # specify the mail server and port number
        server.starttls()  # upgrade the connection to a secure encrypted SSL/TLS connection
        server.login(from_email, from_password)  # login to your email account
        text = msg.as_string()  # convert the message to a string
        server.sendmail(from_email, to_email, text)  # send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()  # close the connection

# Example usage
send_email(
    subject="Test Email",
    body="This is a test email sent from Python.",
    to_email="imsemwalmayank@gmail.com",
    from_email="imsemwalmayank@gmail.com",
    from_password="jmlp kaxu sqqh wwsg"
)