import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

def send_mail():
    smtp_host = "smtp.gmail.com"
    smtp_port = 587

    html = Template(Path('index.html').read_text())
    msg = EmailMessage()
    msg["From"] = "Zero"
    msg["To"] = "email@example.com"
    msg["Subject"] = "Contacting you based on your offer"
    msg.set_content(html.substitute(name=" Bhai"), "html")

    try:
        with smtplib.SMTP(host=smtp_host, port=smtp_port, timeout=30) as smtp:
            smtp.set_debuglevel(1)   # prints protocol exchange to console for debugging
            smtp.ehlo()
            smtp.starttls()         # secure the connection
            smtp.ehlo()
            smtp.login("email@example.com", "czbb rbxg tnka clwz")
            smtp.send_message(msg)
            print("Email sent successfully.")
    except smtplib.SMTPAuthenticationError as e:
        print("Authentication failed:", e)
        print("If you're using Gmail: enable 2FA and create an App Password, then use it as SMTP_PASS.")
    except Exception as e:
        print("Failed to send email:", type(e).__name__, e)

if __name__ == "__main__":
    send_mail()
