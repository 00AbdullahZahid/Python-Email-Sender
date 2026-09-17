# PyMail — HTML Email Sender

PyMail is a lightweight Python-based email automation project that sends professionally formatted HTML emails through Gmail's SMTP server.

The project combines a Python SMTP client with a responsive HTML email template, allowing dynamic values such as the recipient's name to be inserted into the message before delivery.

---

## Overview

The project consists of two main components:

* **Python SMTP Sender** — Handles the SMTP connection, authentication, HTML template loading, variable substitution, and email delivery.
* **Responsive HTML Template** — Provides the visual design and content of the email.

The Python application connects to Gmail's SMTP server using port `587` and establishes a secure connection with STARTTLS before authentication and message delivery.

---

## Features

* Send HTML emails using Python
* Gmail SMTP integration
* Secure STARTTLS connection
* Dynamic template variables
* External HTML email template
* Responsive email layout
* Built-in SMTP debugging
* Authentication error handling
* General exception handling
* Simple and lightweight implementation

---

## Project Structure

```text
PyMail/
│
├── pymail.py
├── index.html
└── README.md
```

### `pymail.py`

The Python script handles the complete email-sending process.

It:

1. Connects to Gmail SMTP.
2. Loads the HTML template from `index.html`.
3. Creates an `EmailMessage`.
4. Inserts dynamic values into the template.
5. Establishes a secure TLS connection.
6. Authenticates with Gmail.
7. Sends the email.
8. Reports success or errors.

The template is loaded using Python's `pathlib` and `string.Template`, with the `$name` variable replaced before sending.

### `index.html`

The HTML file contains the email design and message content.

It includes:

* Responsive layout
* Centered email container
* Styled heading and paragraphs
* Highlighted text
* Call-to-action button
* Footer
* Mobile-specific styling

The email container is designed with a maximum width of `600px`, while a media query adjusts the content and footer spacing on smaller screens.

---

# Requirements

* Python 3.x
* A Gmail account
* Gmail SMTP access
* A Gmail App Password

The project uses Python's built-in libraries, including:

```python
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
```

No external Python packages are required.

---

# Installation

## 1. Clone the Repository

```bash
git clone https://github.com/00AbdullahZahid/PyMail.git
cd PyMail
```

Replace the repository URL with the actual repository URL if it differs.

---

## 2. Configure Gmail

For Gmail SMTP authentication, enable **2-Step Verification** on your Google account and create an **App Password**.

Do not use your normal Gmail account password in the application.

---

## 3. Configure the Script

Update the email configuration in `pymail.py`:

```python
smtp_host = "smtp.gmail.com"
smtp_port = 587
```

Then configure the sender, recipient, subject, and authentication credentials.

For example:

```python
msg["From"] = "your-email@gmail.com"
msg["To"] = "recipient@example.com"
msg["Subject"] = "Your Subject"
```

The current implementation uses Gmail SMTP and authenticates before sending the message.

---

# HTML Templates

The project uses Python's `Template` class to process the HTML email.

The template can contain dynamic variables such as:

```html
<h1>Hello $name,</h1>
```

The Python script can then substitute the value:

```python
html.substitute(name="Recipient")
```

This makes it possible to reuse the same HTML template for different recipients.

The included template uses `$name` for personalization.

---

# Running the Project

Run:

```bash
python pymail.py
```

If authentication and SMTP configuration are correct, the script sends the email and prints:

```text
Email sent successfully.
```

The application also enables SMTP debug output, which prints the SMTP protocol exchange to the console for troubleshooting.

---

# Email Template

The included template is designed as a professional follow-up email.

The current message contains:

* Personalized greeting
* Follow-up message
* Request for an update
* Professional closing
* Details button
* Follow-up footer

The template also includes a responsive mobile layout so the email adapts to smaller screens.

---

# Error Handling

The application handles Gmail authentication failures separately from other exceptions.

Authentication failures provide a specific message directing the user toward Gmail 2FA and App Password configuration.

Example:

```text
Authentication failed: ...
If you're using Gmail: enable 2FA and create an App Password, then use it as SMTP_PASS.
```

---

# Security

Never commit credentials directly to GitHub.

The current source contains SMTP authentication credentials, so they should be removed from the source code and replaced with environment variables before publishing the repository.

A safer implementation would use:

```env
SMTP_EMAIL=your-email@gmail.com
SMTP_PASSWORD=your-app-password
```

and load them through environment variables.

Also add:

```gitignore
.env
__pycache__/
*.pyc
```

to `.gitignore`.

If an App Password has already been exposed publicly, revoke it and generate a new one.

---

# Customizing the Email

You can modify `index.html` to customize:

* Email text
* Colors
* Typography
* Button text
* Button URL
* Footer
* Layout
* Responsive behavior

The current template uses Arial/Helvetica typography, a light gray page background, a white content container, and a blue call-to-action button.

---

# Technologies

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Email automation          |
| `smtplib`         | SMTP communication        |
| `EmailMessage`    | Email construction        |
| `string.Template` | Dynamic HTML substitution |
| HTML5             | Email structure           |
| CSS               | Email styling             |
| Gmail SMTP        | Email delivery            |
| STARTTLS          | Secure SMTP connection    |

---

# Future Improvements

Potential improvements for the project include:

* Environment-variable based configuration
* Multiple recipient support
* HTML template selection
* Attachment support
* Email scheduling
* Email delivery logging
* CSV-based recipient lists
* Reusable email templates
* CLI arguments for recipient and subject
* Configuration file support
* Improved template validation

---

# Developer Note

PyMail was created as a practical demonstration of Python's built-in email capabilities, SMTP communication, HTML email templating, and basic automation.

The project demonstrates how a Python application can combine backend logic with a professionally designed HTML email template to create personalized automated emails.

---

# License

Add your preferred license here.

For example:

```text
MIT License
```

---

# Author

**Abdullah Zahid**

Python Developer | WordPress & Web Developer

GitHub: `00AbdullahZahid`
