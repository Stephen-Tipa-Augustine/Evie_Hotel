from django.shortcuts import render
from . import models, xml_generator
from Evie_Hotel.settings import STATICFILES_DIRS
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'Hotel/index.html')

def book_table(request):
    xml_path = STATICFILES_DIRS[0] + "/xml/booking.xml"
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        time = request.POST.get("time")
        people = request.POST.get("people")
        message = request.POST.get("message")
        writer = xml_generator.BookingRecord(xml_path)
        writer.createChild(name=name, email=email, phone=phone, date=date, time=time,people=people, message=message)
        writer.saveToXML()
    return render(request, 'Hotel/notification.html')

def contact(request):
    xml_path = STATICFILES_DIRS[0] + "/xml/contact.xml"
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")
        writer = xml_generator.ContactRecord(xml_path)
        writer.createChild(name=name, email=email, subject=subject, message=message)
        writer.saveToXML()
    return render(request, 'Hotel/notification.html')