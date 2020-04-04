
import requests
from django.shortcuts import render
from django.shortcuts import render, redirect
import http.client
import json

from .forms import AddInternship
# models
from .models import Hospitals,District,rescue

# Create your views here.

def index(request):


    conn = http.client.HTTPSConnection("covid-19-coronavirus-statistics.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com",
        'x-rapidapi-key': "9dcb69727amsh75270b63ce4637ap1201afjsn444b900fc39e"
    }

    conn.request("GET", "/v1/stats?country=India", headers=headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    data = data.decode("utf-8")
    data = json.loads(data)
    data = data['data']
    data = data['covid19Stats']
    print(data)
    for i in data:
        country = i['country']
        deaths = i['deaths']
        confirmed = i['confirmed']
        recover = i['recovered']
        last_update = i['lastUpdate']
    context ={
        'country' : country,
        'deaths':deaths,
        'confirmed': confirmed,
        'recover' : recover,
        'last_update':last_update
    }


   # print(data['data'])
    return render(request, 'index.html',context)


def country(request):
    conn = http.client.HTTPSConnection("covid-193.p.rapidapi.com")

    headers = {
        'x-rapidapi-host': "covid-193.p.rapidapi.com",
        'x-rapidapi-key': "9dcb69727amsh75270b63ce4637ap1201afjsn444b900fc39e"
    }

    conn.request("GET", "/countries", headers=headers)

    res = conn.getresponse()
    data = res.read()
    # print(data.decode("utf-8"))
    data = data.decode("utf-8")
    # print(data)
    data = json.loads(data)
    countries = data['response']

    context = {
        'countries': countries,
    }

    return render(request,'countries.html',context)

def hospitals(request):
    s_Data =  District.objects.all()

    h_data = Hospitals.objects.all()
    print(s_Data)
    print(h_data)
    for i in s_Data:
        h = Hospitals.objects.filter(state__dName=i.dName)
        for i in h:
            print(i.state)
            print(i.hName)
    context ={
        's_data':s_Data,
        'h_data':h_data
    }
    return render(request,'hospitals.html',context)

def Rescue(request):
    form = AddInternship()

    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        state = request.POST['stt']
        district = request.POST['district']
        pincode = request.POST['pin']
        mobile = request.POST.get('user_phone')
        data = rescue(name=name,address=address,state=state,district=district,pincode=pincode,user_phone
        =mobile)
        data.save()
    context = {
        'form': form,
    }
    return render(request,'rescue.html',context)

# Guidlines

def guid(request):
    return render(request,'guidlines.html')


#corona details

def details(request):
    return render(request,'details.html')