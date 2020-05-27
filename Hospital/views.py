from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import *


# Create your views here.

def Home(request):
    return render(request, "home.html")


def About(request):
    return render(request, "about.html")


def Contact(request):
    return render(request, "contact.html")


def Index(request):
    if not request.user.is_staff:
        return redirect('login')

    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    appointments = Appointment.objects.all()

    d = 0
    p = 0
    a = 0
    for i in doctors:
        d += 1

    for i in patients:
        p += 1

    for i in appointments:
        a += 1

    dict1 = {'d': d,
             'p': p,
             'a': a}
    return render(request, "index.html", dict1)


def Login(request):
    error = ""
    if request.method == 'POST':
        uname = request.POST['uname']
        upass = request.POST['upass']
        user = authenticate(username=uname, password=upass)
        try:
            if user.is_staff:
                login(request, user)
                error = "No"
            else:
                error = "Yes"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "login.html", d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')

    logout(request)
    return redirect('login')


def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')

    doc = Doctor.objects.all()
    d = {'doc': doc}
    return render(request, 'view_doctor.html', d)


def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        dname = request.POST['dname']
        dcontact = request.POST['dcontact']
        dspecial = request.POST['dspecial']
        try:
            Doctor.objects.create(name=dname, phone=dcontact, specialization=dspecial)
            error = "No"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "add_doctor.html", d)


def Delete_Doctor(request, did):
    if not request.user.is_staff:
        return redirect('login')

    doctor = Doctor.objects.get(id=did)
    doctor.delete()
    return redirect('view_doctor')


def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')

    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request, 'view_patient.html', d)


def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == 'POST':
        pname = request.POST['pname']
        pgender = request.POST['pgender']
        pcontact = request.POST['pcontact']
        paddress = request.POST['paddress']
        try:
            Patient.objects.create(name=pname, gender=pgender, phone=pcontact, address=paddress)
            error = "No"
        except:
            error = "Yes"
    d = {'error': error}
    return render(request, "add_patient.html", d)


def Delete_Patient(request, pid):
    if not request.user.is_staff:
        return redirect('login')

    patient = Patient.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')


def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')

    appoint = Appointment.objects.all()
    d = {'appoint': appoint}
    return render(request, 'view_appointment.html', d)


def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()
    if request.method == 'POST':
        dname = request.POST['doctor']
        pname = request.POST['patient']
        date = request.POST['date']
        time = request.POST['time']
        doctor = Doctor.objects.filter(name=dname).first()
        patient = Patient.objects.filter(name=pname).first()
        try:
            Appointment.objects.create(doctor=doctor, patient=patient, date1=date, time1=time)
            error = "No"
        except:
            error = "Yes"
    d = {'doctor': doctor1,
         'patient': patient1,
         'error': error}
    return render(request, "add_appointment.html", d)


def Delete_Appointment(request, aid):
    if not request.user.is_staff:
        return redirect('login')

    appointment = Appointment.objects.get(id=aid)
    appointment.delete()
    return redirect('view_appointment')
