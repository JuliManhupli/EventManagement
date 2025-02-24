from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_event_registration_email(user, event):
    subject = f'You have successfully registered for {event.title}'
    html_message = render_to_string('event_registration_email.html', {'user': user, 'event': event})
    plain_message = strip_tags(html_message)
    from_email = settings.EMAIL_HOST_USER
    to_email = [user.email]

    mail = EmailMultiAlternatives(subject, plain_message, from_email, to_email)
    mail.attach_alternative(html_message, "text/html")
    mail.send()
