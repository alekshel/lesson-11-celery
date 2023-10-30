from django.shortcuts import render, redirect
from django.urls import reverse

from .tasks import send_phone_message


def main_page(request):
    if request.method == "GET":
        return render(request, "main.html")

    message = request.POST.get("message", "")
    phone = request.POST.get("phone", "")
    send_phone_message.delay(phone, message)

    return redirect(reverse("main_page"))
