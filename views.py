from django.core.mail import EmailMessage
from django.shortcuts import render
from .forms import EmailForm

def send_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            to = form.cleaned_data['to']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attachments = request.FILES.getlist('attachments')

            email = EmailMessage(
                subject,
                message,
                'yashaswinigowda2124@gmail.com',  # from email
                [to]
            )

            for attachment in attachments:
                email.attach(attachment.name, attachment.read(), attachment.content_type)
            
            email.send()

            return render(request, 'email_sender/success.html')
    else:
        form = EmailForm()

    return render(request, 'email_sender/email_form.html', {'form': form})