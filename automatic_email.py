import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time

# Your email credentials
sender_email = "shlok.mathur2020@gmail.com"
sender_password = "nlsq irfd hlwx vyf"  # Use App Password for Gmail

# CSV file containing recipient emails (Assuming the column name is 'email')
csv_file = "emails.csv"  # Path to your CSV file
df = pd.read_csv(csv_file)
recipients = df['email'].tolist()

# Email content
subject = "Your Subject Here"
body = "This is your message content."

# File to be attached (adjust the path accordingly)
attachment_file = "/path/to/your/file.pdf"

# Function to send emails with an attachment
def send_email(to_email):
    try:
        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Open the file to be sent
        with open(attachment_file, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {attachment_file}")

            # Attach the file to the message
            msg.attach(part)

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()

        print(f"Email sent successfully to {to_email}")

    except Exception as e:
        print(f"Failed to send email to {to_email}. Error: {e}")

# Send emails to each recipient
for email in recipients:
    send_email(email)
    time.sleep(1)  # Delay to prevent overwhelming the mail server (adjust this delay if needed)
