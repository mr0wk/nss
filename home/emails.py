from django.template import context
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings

def send_delay_info_email(context: dict) -> None:
    email_address = context["email_address"]
    email_subject = "Nie śpiesz się!"
    email_body_context = {key: value for (key, value) in context.items() if key != "email_address"}
    email_body = render_to_string('email_message.txt', email_body_context)

    email = EmailMessage(
        email_subject,
        email_body,
        settings.DEFAULT_FROM_EMAIL,
        email_address
    )

    return email.send(fail_silently=False)