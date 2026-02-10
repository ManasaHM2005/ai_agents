import smtplib
from email.message import EmailMessage
from secrets import sender_email,receiver_email,password
# Create email
def send_email(receiver_email: str, subject: str, content: str):
    """Send an email to the given receiver with the specified subject and content."""
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg.set_content(content)

    # Login and send
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()  # Secure the connection
        server.login(sender_email, password)
        server.send_message(msg)

print("Email sent successfully!")

#send_email(receiver_email="shravyashraya26@gamil.com", subject="hello from python", content="this email sent using python")
