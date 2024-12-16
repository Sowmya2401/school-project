from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Facilities, Teacher
from . forms import AppointmentFrom
def index(request):
    facilities=Facilities.objects.all()
    teachers=Teacher.objects.all()
    form= AppointmentFrom()
    context = {
        "facilities":facilities,
        "teachers":teachers,
        "form":form
    }
    if request.method=='POST':
        form=AppointmentFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "index.html", context)
