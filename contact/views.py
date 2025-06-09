from django.core.mail import EmailMessage
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse

def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"Name: {name}\nEmail: {email}\nMobile Number: {phone}\nMessage:\n{message}"

        try:
            mail = EmailMessage(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
                reply_to=[email]
            )
            mail.send()
            print("✅ Email sent successfully to:", settings.CONTACT_EMAIL)
        except Exception as e:
            print("❌ Failed to send email:", str(e))

        # ✅ Redirect to the same page with a success flag
        return redirect(reverse('index') + '?sent=1')

    # ✅ On GET request, check if form was just submitted
    sent = request.GET.get("sent") == "1"
    return render(request, "contact/index.html", {"sent": sent})
