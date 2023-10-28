from django.shortcuts import render, redirect
from django.urls import reverse

from decouple import config

from .tasks import send_phone_message


def main_page(request):
    verified_phone = config("PHONE_FOR_SMS", default="")

    if request.method == "GET":
        return render(request, "main.html", {"phone": verified_phone})

    message = request.POST.get("message", "")
    send_phone_message.delay(verified_phone, message)

    return redirect(reverse("main_page"))
