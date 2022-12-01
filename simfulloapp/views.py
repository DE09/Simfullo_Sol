from django.shortcuts import render
import json
from .models import lcl, air, airother
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')

def quotation(request):
    return render(request, 'quotation.html')

def lclinfo(request):
    info = lcl.objects.all()
    context = {
        'info' : info
    }
    return render(request, 'lclinfo.html', context)


def airinfo(request):
    info = air.objects.all().order_by('id')
    airotherinfo = airother.objects.all().order_by('id')
    context = {
        'info' : info,
        'airotherinfo' : airotherinfo
    }
    return render(request, 'airinfo.html', context)

def fclinfo(request):
    return render(request, 'fclinfo.html')
    

def showquote(request):
    jsonObject = json.loads(request.body)
    origin = jsonObject.get('origin')
    dest = jsonObject.get('dest')
    incoterms = jsonObject.get('incoterms')
    cbm = jsonObject.get('cbm')
    kg = jsonObject.get('kg')

    q = Q(origin=origin, dest=dest)
    
    if incoterms == 'EXW':
        q.add(Q(chargeAt='origin')|Q(chargeAt='freight')|Q(chargeAt='destination'), q.AND)
    elif incoterms == 'DAP':
        q.add(Q(chargeAt='origin')|Q(chargeAt='freight')|Q(chargeAt='destination'), q.AND)
    elif incoterms == 'FOB':
        q.add(Q(chargeAt='freight')|Q(chargeAt='destination'), q.AND)
    else:
        q.add(Q(chargeAt='origin')|Q(chargeAt='freight'), q.AND)

    rate = lcl.objects.filter(q)

    lcltotal = 0
    
    for i in range(0,len(rate)):
        if rate[i].cur == 'USD':
            if rate[i].unit == 'R/TON':
                total = float(rate[i].rate) * 1400 * float(cbm)
            elif rate[i].unit == 'BL':
                total = float(rate[i].rate) * 1400
            elif rate[i].unit == 'KG':
                total = float(rate[i].rate) * float(kg)
        else:
            if rate[i].unit == 'R/TON':
                total = float(rate[i].rate) * float(cbm)
            elif rate[i].unit == 'BL':
                total = float(rate[i].rate)
            elif rate[i].unit == 'KG':
                total = float(rate[i].rate) * float(kg)
    
        lcltotal = lcltotal + total
        
    context = {
            'lcltotal' : lcltotal,

        }
    return JsonResponse(context)


def lcladd(request):
    
    jsonObject = json.loads(request.body)
    
    lcladd = lcl.objects.create(
        origin = jsonObject.get('origin'),
        dest = jsonObject.get('dest'),
        name = jsonObject.get('name'),
        cur = jsonObject.get('cur'),
        rate = jsonObject.get('rate'),
        unit = jsonObject.get('unit'),
        chargeAt = jsonObject.get('chargeAt'),
        group = jsonObject.get('group'),
    )
    
    lcladd.save()
    id = lcladd.id

    context = {
        'id' : id
    }
    
    return JsonResponse(context)

def fcladd(request):
    return render(request, 'fclinfo.html')

def airadd(request):
    
    jsonObject = json.loads(request.body)
    
    airadd = air.objects.create(
        origin = jsonObject.get('origin'),
        dest = jsonObject.get('dest'),
        consol = jsonObject.get('consol'),
        line = jsonObject.get('line'),
        cur = jsonObject.get('cur'),
        minimum = jsonObject.get('minimum'),
        normal = jsonObject.get('normal'),
        over45 = jsonObject.get('over45'),
        over100 = jsonObject.get('over100'),
        over300 = jsonObject.get('over300'),
        over500 = jsonObject.get('over500'),
        over1000 = jsonObject.get('over1000'),
        fsc = jsonObject.get('fsc'),
        skdl = jsonObject.get('skdl'),
        via = jsonObject.get('via'),
    )

    airadd.save()
    id = airadd.id

    context = {
        'id' : id
    }
    
    return JsonResponse(context)

def airotheradd(request):
    jsonObject = json.loads(request.body)
    airotheradd = airother.objects.create(
        airother_origin = jsonObject.get('airother_origin'),
        airother_dest = jsonObject.get('airother_dest'),
        airother_consol = jsonObject.get('airother_consol'),
        airother_line = jsonObject.get('airother_line'),
        airother_name = jsonObject.get('airother_name'),
        airother_cur = jsonObject.get('airother_cur'),
        airother_rate = jsonObject.get('airother_rate'),
        airother_unit = jsonObject.get('airother_unit'),
        airother_chargeAt = jsonObject.get('airother_chargeAt'),
    )
    
    airotheradd.save()
    id = airotheradd.id

    context = {
        'id' : id
    }
    
    return JsonResponse(context)


def lcldelete(request):
    jsonObject = json.loads(request.body)
    lcldelete = lcl.objects.get(id=jsonObject.get('id'))
    lcldelete.delete()
    
    context = {
        'success' : 'success'
    }
    
    return JsonResponse(context)

def fcldelete(request):
    return render(request, 'fclinfo.html')


def airdelete(request):
    jsonObject = json.loads(request.body)
    airdelete = air.objects.get(id=jsonObject.get('id'))
    airdelete.delete()
    
    context = {
        'success' : 'success'
    }
    
    return JsonResponse(context)

def airotherdelete(request):
    jsonObject = json.loads(request.body)
    airotherdelete = airother.objects.get(id=jsonObject.get('id'))
    airotherdelete.delete()
    
    context = {
        'success' : 'success'
    }
    
    return JsonResponse(context)


def lclupdate(request):
    jsonObject = json.loads(request.body)
    lclupdate = lcl.objects.filter(id=jsonObject.get('id'))
    lclupdate.update(
        origin = jsonObject.get('origin'),
        dest = jsonObject.get('dest'),
        name = jsonObject.get('name'),
        cur = jsonObject.get('cur'),
        rate = jsonObject.get('rate'),
        unit = jsonObject.get('unit'),
        chargeAt = jsonObject.get('chargeAt'),
        group = jsonObject.get('group'),
    )

    context = {
        'lclupdate' :'lclupdate'
    }
        
    return JsonResponse(context)

def fclupdate(request):
    return render(request, 'fclinfo.html')



def airupdate(request):
    jsonObject = json.loads(request.body)
    airupdate = air.objects.filter(id=jsonObject.get('id'))
    airupdate.update(
        consol = jsonObject.get('consol'),
        line = jsonObject.get('line'),
        cur = jsonObject.get('cur'),
        minimum = jsonObject.get('minimum'),
        normal = jsonObject.get('normal'),
        over45 = jsonObject.get('over45'),
        over100 = jsonObject.get('over100'),
        over300 = jsonObject.get('over300'),
        over500 = jsonObject.get('over500'),
        over1000 = jsonObject.get('over1000'),
        fsc = jsonObject.get('fsc'),
        skdl = jsonObject.get('skdl'),
        via = jsonObject.get('via'),
    )

    context = {
        'airupdate' :'airupdate'
    }
        
    return JsonResponse(context)

def airotherupdate(request):
    jsonObject = json.loads(request.body)
    airotherupdate = airother.objects.filter(id=jsonObject.get('id'))
    airotherupdate.update(
        airother_consol = jsonObject.get('consol'),
        airother_line = jsonObject.get('line'),
        airother_name = jsonObject.get('name'),
        airother_cur = jsonObject.get('cur'),
        airother_rate = jsonObject.get('rate'),
        airother_unit = jsonObject.get('unit'),
        airother_chargeAt = jsonObject.get('chargeAt'),
    )

    context = {
        'airotherupdate' :'airotherupdate'
    }
        
    return JsonResponse(context)