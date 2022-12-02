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
    airotherrate = airother.objects.filter(q)
    
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
<<<<<<< HEAD
    
    
    if float(cbm) * 167 > float(kg):
        cw = float(cbm) * 167
    else: 
        cw = float(kg)
    
    airother_total = 0
    for i in range(0,len(airotherrate)):
        if airotherrate[i].cur == 'USD':
            if airotherrate[i].unit == 'AWB':
                total = float(airotherrate[i].rate) * 1400
            elif airotherrate[i].unit == 'KG':
                total = float(airotherrate[i].rate) * 1400 * float(cw)
        else:
            if airotherrate[i].unit == 'AWB':
                total = float(airotherrate[i].rate)
            elif airotherrate[i].unit == 'KG':
                total = float(airotherrate[i].rate) * float(cw)

        airother_total = airother_total + total
    
    afc = air.objects.filter(origin=origin, dest=dest)    
    

    afclist = []
    for i in range(0,len(afc)):
=======
        
    
    afc = air.objects.filter(origin=origin , dest = dest)
    
    if float(cbm) * 167 > float(kg):
        cw = float(cbm)*167
    else : 
        cw = float(kg)
    
    afclist = []
    for i in range(0,len(afc)):
        cur = afc[i].cur
>>>>>>> d8dab3490f36c91c612de187f49bd68b7a94c841
        minimum = float(afc[i].minimum)
        normal = float(afc[i].normal)
        over45 = float(afc[i].over45)
        over100 = float(afc[i].over100)
        over300 = float(afc[i].over300)
        over500 = float(afc[i].over500)
        over1000 = float(afc[i].over1000)
        fsc = float(afc[i].fsc)
<<<<<<< HEAD
                
        if afc[i].cur == 'USD' :
            if cw < 45 :
                if minimum > (normal+fsc) * 45:
                    afclist.append(minimum * 1400)
                else :
                    if (normal+fsc) * cw > (over45+fsc) * 45:
                        afclist.append((over45+fsc) * 45 * 1400)
                    else : 
                        afclist.append((normal+fsc) * cw * 1400)
            elif cw < 100 :
                if minimum > (over45+fsc) * cw:
                    afclist.append(minimum * 1400)
                else : 
                    if (over45+fsc) * cw > (over100+fsc) * 100:
                        afclist.append((over100+fsc) * 100 * 1400)
                    else : 
                        afclist.append((over45+fsc) * cw * 1400)
            elif cw < 300 :
                if minimum > (over100+fsc) * cw:
                    afclist.append(minimum * 1400)
                else : 
                    if (over100+fsc) * cw > (over300+fsc) * 300:
                        afclist.append((over300+fsc) * 300 * 1400)
                    else : 
                        afclist.append((over100+fsc) * cw * 1400)
            elif cw < 500 :
                if minimum > (over300+fsc) * cw:
                    afclist.append(minimum * 1400)
                else : 
                    if (over300+fsc) * cw > (over500+fsc) * 500:
                        afclist.append((over500+fsc) * 500 * 1400)
                    else : 
                        afclist.append((over300+fsc) * cw * 1400)
            elif cw < 1000 :
                if minimum > (over1000+fsc) * cw:
                    afclist.append(minimum * 1400)
                else : 
                    if (over500+fsc) * cw > (over1000+fsc) * 1000:
                        afclist.append((over1000+fsc) * 1000 * 1400)
                    else : 
                        afclist.append((over500+fsc) * cw * 1400)
            else : 
                if minimum > (over1000+fsc) * cw:
                    afclist.append(minimum * 1400)
                else : 
                    afclist.append((over1000+fsc) * cw * 1400)           
                    
        elif afc[i].cur == 'KRW' :
            if cw < 45 :
                if minimum > (normal+fsc) * 45:
                    afclist.append(minimum)
                else :
                    if (normal+fsc) * cw > (over45+fsc) * 45:
                        afclist.append((over45+fsc) * 45)
                    else : 
                        afclist.append((normal+fsc) * cw)
            elif cw < 100 :
                if minimum > (over45+fsc) * cw:
                    afclist.append(minimum)
                else : 
                    if (over45+fsc) * cw > (over100+fsc) * 100:
                        afclist.append((over100+fsc) * 100)
                    else : 
                        afclist.append((over45+fsc) * cw)
            elif cw < 300 :
                if minimum > (over100+fsc) * cw:
                    afclist.append(minimum)
                else : 
                    if (over100+fsc) * cw > (over300+fsc) * 300:
                        afclist.append((over300+fsc) * 300)
                    else : 
                        afclist.append((over100+fsc) * cw)
            elif cw < 500 :
                if minimum > (over300+fsc) * cw:
                    afclist.append(minimum)
                else : 
                    if (over300+fsc) * cw > (over500+fsc) * 500:
                        afclist.append((over500+fsc) * 500)
                    else : 
                        afclist.append((over300+fsc) * cw)
            elif cw < 1000 :
                if minimum > (over1000+fsc) * cw:
                    afclist.append(minimum)
                else : 
                    if (over500+fsc) * cw > (over1000+fsc) * 1000:
                        afclist.append((over1000+fsc) * 1000)
                    else : 
                        afclist.append((over500+fsc) * cw)
            else : 
                if minimum > (over1000+fsc) * cw:
                    afclist.append(minimum)
                else : 
                    afclist.append((over1000+fsc) * cw)           


    airtotal = min(afclist) + airother_total
    print(airtotal)
    
=======
        
        if cur =='USD' :
            if cw < 45 :
                if minimum > (normal+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    if (normal+fsc)*cw > (over45+fsc)*45:
                        afclist.append((over45+fsc)*45*1400) 
                    else : 
                        afclist.append((normal+fsc)*cw*1400) 
            elif cw < 100 :
                if minimum > (over45+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    if (over45+fsc)*cw > (over100+fsc)*100:
                        afclist.append((over100+fsc)*100*1400) 
                    else : 
                        afclist.append((over45+fsc)*cw*1400) 
            elif cw < 300 :
                if minimum > (over100+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    if (over100+fsc)*cw > (over300+fsc)*300:
                        afclist.append((over300+fsc)*300*1400)
                    else : 
                        afclist.append((over100+fsc)*cw*1400) 
            elif cw < 500 :
                if minimum > (over300+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    if (over300+fsc)*cw > (over500+fsc)*500:
                        afclist.append((over500+fsc)*500*1400)
                    else : 
                        afclist.append((over300+fsc)*cw*1400)
            elif cw < 1000 :
                if minimum > (over500+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    if (over500+fsc)*cw > (over1000+fsc)*1000:
                        afclist.append((over1000+fsc)*1000*1400)
                    else : 
                        afclist.append((over500+fsc)*cw*1400)
            else:
                if minimum > (over1000+fsc)*cw:
                    afclist.append(minimum*1400)
                else:
                    afclist.append((over1000+fsc)*cw*1400)
                    

        elif cur == 'KRW' :
            if cw < 45 :
                if minimum > (normal+fsc)*cw:
                    afclist.append(minimum)
                else:
                    if (normal+fsc)*cw > (over45+fsc)*45:
                        afclist.append((over45+fsc)*45) 
                    else : 
                        afclist.append((normal+fsc)*cw)
            elif cw < 100 :
                if minimum > (over45+fsc)*cw:
                    afclist.append(minimum)
                else:
                    if (over45+fsc)*cw > (over100+fsc)*100:
                        afclist.append((over100+fsc)*100) 
                    else : 
                        afclist.append((over45+fsc)*cw) 
            elif cw < 300 :
                if minimum > (over100+fsc)*cw:
                    afclist.append(minimum)
                else:
                    if (over100+fsc)*cw > (over300+fsc)*300:
                        afclist.append((over300+fsc)*300) 
                    else : 
                        afclist.append((over100+fsc)*cw) 
            elif cw < 500 :
                if minimum > (over300+fsc)*cw:
                    afclist.append(minimum)
                else:
                    if (over300+fsc)*cw > (over500+fsc)*500:
                        afclist.append((over500+fsc)*500) 
                    else : 
                        afclist.append((over300+fsc)*cw) 
            elif cw < 1000 :
                if minimum > (over500+fsc)*cw:
                    afclist.append(minimum)
                else:
                    if (over500+fsc)*cw > (over1000+fsc)*1000:
                        afclist.append((over1000+fsc)*1000) 
                    else : 
                        afclist.append((over500+fsc)*cw) 
            else:
                if minimum > (over1000+fsc)*cw:
                    afclist.append(minimum)
                else:
                    afclist.append((over1000+fsc)*cw)

    print(afclist)

    

    

        
>>>>>>> d8dab3490f36c91c612de187f49bd68b7a94c841
    context = {
            'lcltotal' : lcltotal,
            'airtotal' : airtotal,
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
        origin = jsonObject.get('airother_origin'),
        dest = jsonObject.get('airother_dest'),
        line = jsonObject.get('airother_line'),
        name = jsonObject.get('airother_name'),
        cur = jsonObject.get('airother_cur'),
        rate = jsonObject.get('airother_rate'),
        unit = jsonObject.get('airother_unit'),
        chargeAt = jsonObject.get('airother_chargeAt'),
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