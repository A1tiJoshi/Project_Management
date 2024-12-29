from celery import shared_task

# Define a shared task for sending emails
@shared_task
def send_email_task(recipient, subject, message):
    # Example logic for sending email
    print(f"Email sent to {recipient} with subject: {subject}")
    # Here you would add the actual email sending logic using an email library
