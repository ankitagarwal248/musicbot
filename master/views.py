from django.conf import settings
from django.shortcuts import render
from django.template.loader import render_to_string
import requests


def home(request):

    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        numbooks = request.POST.get('numbooks')

        key = settings.MAILGUN_KEY
        recipient = [
            'ankitagarwal24.8@gmail.com',
            'tpurohit91@gmail.com'
        ]
        from_ = settings.SENDER_EMAIL_ID
        context = {
            'name': name,
            'email': email,
            'phone': phone,
            'city': city,
            'numbooks': numbooks
        }
        html = render_to_string("master/email.html", context)

        request_url = settings.REQUEST_URL
        requests.post(request_url, auth=('api', key), data={
            'from': from_,
            'to': recipient,
            'subject': 'Bookworm Registration',
            "html": html,
        })

    return render(request, 'master/home.html', {})
