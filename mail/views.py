from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import EmailMessage


def mail(request):
    return render(request, 'mail/mail.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        emailMessage = EmailMessage(
            to=['fko2347037@stu.O-hara.ac.jp'],
            subject='お問い合わせがありました：{0}'.format(subject),
            body='名前: {0}\nメールアドレス: {1}\n本文: {2}'.format(name, email, message),
        )
        emailMessage.send()
        return HttpResponseRedirect('/mail/contact')
    else:
        return render(request, 'mail/contact.html')
