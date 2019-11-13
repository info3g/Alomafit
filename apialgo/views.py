import json

import numpy as np
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets

from apialgo.models import Measurements
from apialgo.serializer import MeasurementSerializer


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurements.objects.all()
    serializer_class = MeasurementSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly,)


@csrf_exempt
def brasize(request):
    y = json.loads(request.GET.get('data'))['name']
    return JsonResponse(y)


def getUnderBust(request):
    braSize = json.loads(request.POST.get('braSize'))['data']
    SIZES = [30, 32, 34, 36, 38, 40, 42, 44, 46]
    minMeasure = [68, 73, 73, 78, 83, 88, 93, 98, 103]
    maxMeasure = [72, 77, 77, 82, 87, 92, 97, 102, 107]
    ind = SIZES.index(braSize)
    result = {"min": minMeasure[ind], "max": maxMeasure[ind]}
    return JsonResponse(result)


def getFullBust(request):
    braSize = json.loads(request.POST.get('braSize'))['data']
    cupSize = json.loads(request.POST.get('cupSize'))['data']

    SIZES = [30, 32, 34, 36, 38, 40, 42, 44, 46]

    AAminMeasure = [0, 79, 84, 89, 95, 0, 0, 0, 0]
    AAmaxMeasure = [0, 81, 86, 91, 97, 0, 0, 0, 0]

    AminMeasure = [0, 81, 86, 91, 97, 101, 107, 112, 114]
    AmaxMeasure = [0, 84, 89, 94, 99, 104, 109, 114, 117]

    BminMeasure = [0, 84, 89, 94, 99, 104, 109, 114, 117]
    BmaxMeasure = [0, 87, 91, 97, 101, 107, 112, 117, 119]

    CminMeasure = [0, 87, 91, 97, 101, 107, 112, 117, 119]
    CmaxMeasure = [0, 89, 94, 99, 104, 109, 114, 119, 122]

    DminMeasure = [84, 89, 94, 99, 104, 109, 114, 119, 122]
    DmaxMeasure = [86, 91, 97, 101, 107, 112, 117, 122, 124]

    DDminMeasure = [86, 91, 97, 101, 107, 112, 117, 122, 124]
    DDmaxMeasure = [89, 94, 99, 104, 109, 114, 119, 124, 127]

    EminMeasure = [89, 94, 99, 104, 109, 114, 119, 124, 127]
    EmaxMeasure = [91, 97, 101, 107, 112, 117, 122, 124, 130]

    FminMeasure = [91, 97, 101, 107, 112, 117, 122, 127, 130]
    FmaxMeasure = [94, 99, 104, 109, 114, 119, 124, 130, 133]

    GminMeasure = [94, 99, 104, 109, 114, 119, 124, 130, 133]
    GmaxMeasure = [97, 101, 107, 112, 117, 122, 127, 133, 136]

    HminMeasure = [97, 101, 107, 112, 117, 122, 127, 133, 136]
    HmaxMeasure = [99, 104, 109, 114, 119, 124, 130, 136, 139]

    ind = SIZES.index(braSize)
    result = {}
    if cupSize == 'AA':
        result = {"min": AAminMeasure[ind], "max": AAmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'A':
        result = {"min": AminMeasure[ind], "max": AmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'B':
        result = {"min": BminMeasure[ind], "max": BmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'C':
        result = {"min": CminMeasure[ind], "max": CmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'D':
        result = {"min": DminMeasure[ind], "max": DmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'DD':
        result = {"min": DDminMeasure[ind], "max": DDmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'E':
        result = {"min": EminMeasure[ind], "max": EmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'F':
        result = {"min": FminMeasure[ind], "max": FmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'G':
        result = {"min": GminMeasure[ind], "max": GmaxMeasure[ind]}
        return JsonResponse(result)
    if cupSize == 'H':
        result = {"min": HminMeasure[ind], "max": HmaxMeasure[ind]}
        return JsonResponse(result)
    return JsonResponse(result)


def GetBestFitTop(request):
    sizes = json.loads(request.POST.get('sizes'))['data']

    bustMeasurements = json.loads(request.POST.get('bustMeasurements'))['data']
    waistMeasurements = json.loads(
        request.POST.get('waistMeasurements'))['data']
    profileBust = json.loads(request.POST.get('profileBust'))['data']
    profileWaist = json.loads(request.POST.get('profileWaist'))['data']

    BustStd = round(np.std(bustMeasurements))
    waistStd = round(np.std(waistMeasurements))

    temp = [abs(x - profileBust) for x in bustMeasurements]

    result = {}

    if min(temp) > BustStd:
        return JsonResponse(result)
    minInd = temp.index(min(temp))

    result['bust'] = {}
    result['waist'] = {}

    if minInd != 0 and minInd != (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['looser'] = sizes[minInd + 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['tighter'] = sizes[minInd - 1]
        result['bust']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
                result['waist']['best fit'] = sizes[minInd + 1]
        return JsonResponse(result)

    elif minInd == (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['tighter'] = sizes[minInd - 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]

        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]

            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
        return JsonResponse(result)

    if minInd == 0:
        result['best fit'] = sizes[minInd]
        result['looser'] = sizes[minInd + 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd + 1]
        return JsonResponse(result)


def GetBestFitBottom(request):
    sizes = json.loads(request.POST.get('sizes'))['data']

    hipMeasurements = json.loads(request.POST.get('hipMeasurements'))['data']
    waistMeasurements = json.loads(
        request.POST.get('waistMeasurements'))['data']
    profilehip = json.loads(request.POST.get('profilehip'))['data']
    profileWaist = json.loads(request.POST.get('profileWaist'))['data']

    hipStd = round(np.std(hipMeasurements))
    waistStd = round(np.std(waistMeasurements))

    temp = [abs(x - profilehip) for x in hipMeasurements]

    result = {}

    if min(temp) > hipStd:
        return JsonResponse(result)
    minInd = temp.index(min(temp))

    result['hip'] = {}
    result['waist'] = {}

    if minInd != 0 and minInd != (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['looser'] = sizes[minInd + 1]
        result['hip']['best fit'] = sizes[minInd]
        result['hip']['tighter'] = sizes[minInd - 1]
        result['hip']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
                result['waist']['best fit'] = sizes[minInd + 1]
        return JsonResponse(result)

    elif minInd == (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['hip']['best fit'] = sizes[minInd]
        result['hip']['tighter'] = sizes[minInd - 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]

        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]

            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
        return JsonResponse(result)

    if minInd == 0:
        result['best fit'] = sizes[minInd]
        result['looser'] = sizes[minInd + 1]
        result['hip']['best fit'] = sizes[minInd]
        result['hip']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd + 1]
        return JsonResponse(result)


def GetBestFitDress(request):
    sizes = json.loads(request.POST.get('sizes'))['data']
    bustMeasurements = json.loads(request.POST.get('bustMeasurements'))['data']
    hipMeasurements = json.loads(request.POST.get('hipMeasurements'))['data']
    waistMeasurements = json.loads(
        request.POST.get('waistMeasurements'))['data']
    profilehip = json.loads(request.POST.get('profilehip'))['data']
    profileWaist = json.loads(request.POST.get('profileWaist'))['data']
    profileBust = json.loads(request.POST.get('profileBust'))['data']

    BustStd = round(np.std(bustMeasurements))
    hipStd = round(np.std(hipMeasurements))
    waistStd = round(np.std(waistMeasurements))

    temp = [abs(x - profileBust) for x in bustMeasurements]
    result = {}

    if min(temp) > BustStd:
        return JsonResponse(result)
    minInd = temp.index(min(temp))

    result['bust'] = {}
    result['waist'] = {}
    result['hip'] = {}
    if minInd != 0 and minInd != (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['looser'] = sizes[minInd + 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['tighter'] = sizes[minInd - 1]
        result['bust']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
                result['waist']['best fit'] = sizes[minInd + 1]
        if abs(hipMeasurements[minInd] - profilehip) < hipStd:
            result['hip']['best fit'] = sizes[minInd]
            result['hip']['tighter'] = sizes[minInd - 1]
            result['hip']['looser'] = sizes[minInd + 1]
        else:
            if hipMeasurements[minInd] - profilehip > 0:
                result['hip']['looser'] = sizes[minInd]
                result['hip']['best fit'] = sizes[minInd - 1]
                result['hip']['loose'] = sizes[minInd + 1]
            else:
                result['hip']['tighter'] = sizes[minInd]
                result['hip']['tight'] = sizes[minInd - 1]
                result['hip']['best fit'] = sizes[minInd + 1]

    elif minInd == (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['tighter'] = sizes[minInd - 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['tighter'] = sizes[minInd - 1]

        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd - 1]

            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['tight'] = sizes[minInd - 1]
        if abs(hipMeasurements[minInd] - profilehip) < hipStd:
            result['hip']['best fit'] = sizes[minInd]
            result['hip']['tighter'] = sizes[minInd - 1]
        else:
            if hipMeasurements[minInd] - profilehip > 0:
                result['hip']['looser'] = sizes[minInd]
                result['hip']['best fit'] = sizes[minInd - 1]
            else:
                result['hip']['tighter'] = sizes[minInd]
                result['hip']['tight'] = sizes[minInd - 1]

    if minInd == 0:
        result['best fit'] = sizes[minInd]
        result['looser'] = sizes[minInd + 1]
        result['bust']['best fit'] = sizes[minInd]
        result['bust']['looser'] = sizes[minInd + 1]
        if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
            result['waist']['best fit'] = sizes[minInd]
            result['waist']['looser'] = sizes[minInd + 1]
        else:
            if waistMeasurements[minInd] - profileWaist > 0:
                result['waist']['looser'] = sizes[minInd]
                result['waist']['loose'] = sizes[minInd + 1]
            else:
                result['waist']['tighter'] = sizes[minInd]
                result['waist']['best fit'] = sizes[minInd + 1]
        if abs(hipMeasurements[minInd] - profilehip) < hipStd:
            result['hip']['best fit'] = sizes[minInd]
            result['hip']['looser'] = sizes[minInd + 1]
        else:
            if hipMeasurements[minInd] - profilehip > 0:
                result['hip']['looser'] = sizes[minInd]
                result['hip']['loose'] = sizes[minInd + 1]
            else:
                result['hip']['tighter'] = sizes[minInd]
                result['hip']['best fit'] = sizes[minInd + 1]

    return JsonResponse(result)



def GetBestFit(request):
    sizes = json.loads(request.POST.get('sizes'))['data']

    result = {}

    param1=request.POST.get('bustMeasurements')
    bustMeasurements=''
    BustStd=''
    
    if not(param1 is None):
        bustMeasurements = json.loads(param1)['data']
        BustStd = round(np.std(bustMeasurements))
        

    param2=request.POST.get('hipMeasurements')
    hipMeasurements=''
    hipStd=''
    if not(param2 is None):
        hipMeasurements = json.loads(param2)['data']
        hipStd = round(np.std(hipMeasurements))


    param3=request.POST.get('waistMeasurements')
    waistMeasurements=''
    waistStd=''
    if not(param3 is None):
        waistMeasurements = json.loads(param3)['data']
        waistStd = round(np.std(waistMeasurements))

    param4=request.POST.get('profilehip')
    profilehip=''
    if not(param4 is None):   
        profilehip = json.loads(param4)['data']

    param5=request.POST.get('profileWaist')
    profileWaist=''
    if not(param5 is None):
        profileWaist = json.loads(param5)['data']

    param6=request.POST.get('profileBust')
    profileBust=''
    if not(param6 is None):
        profileBust = json.loads(param6)['data']

    temp=[]
    if(profileBust!='' and bustMeasurements!=''):
         temp = [abs(x - profileBust) for x in bustMeasurements]
    elif (profilehip!='' and hipMeasurements!=''):
        temp = [abs(x - profilehip) for x in hipMeasurements]
    elif (profileWaist!='' and waistMeasurements!=''):
        temp = [abs(x - profileWaist) for x in waistMeasurements]
    else:
        return JsonResponse(result)

    minInd = temp.index(min(temp))
    

    result['bust'] = {}
    result['waist'] = {}
    result['hip'] = {}
    if minInd != 0 and minInd != (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        result['looser'] = sizes[minInd + 1]
        if(profileBust!='' and bustMeasurements!=''):
            if(abs(bustMeasurements[minInd] - profileBust) < BustStd):
                result['bust']['best fit'] = sizes[minInd]
                result['bust']['tighter'] = sizes[minInd - 1]
                result['bust']['looser'] = sizes[minInd + 1]
            else:
                if bustMeasurements[minInd] - profileBust > 0:
                    result['bust']['looser'] = sizes[minInd]
                    result['bust']['best fit'] = sizes[minInd - 1]
                    result['bust']['loose'] = sizes[minInd + 1]
                else:
                    result['bust']['tighter'] = sizes[minInd]
                    result['bust']['tight'] = sizes[minInd - 1]
                    result['bust']['best fit'] = sizes[minInd + 1]



        if(profileWaist!='' and waistMeasurements!=''):
            if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
                result['waist']['best fit'] = sizes[minInd]
                result['waist']['tighter'] = sizes[minInd - 1]
                result['waist']['looser'] = sizes[minInd + 1]
            else:
                if waistMeasurements[minInd] - profileWaist > 0:
                    result['waist']['looser'] = sizes[minInd]
                    result['waist']['best fit'] = sizes[minInd - 1]
                    result['waist']['loose'] = sizes[minInd + 1]
                else:
                    result['waist']['tighter'] = sizes[minInd]
                    result['waist']['tight'] = sizes[minInd - 1]
                    result['waist']['best fit'] = sizes[minInd + 1]

        if(profilehip!='' and hipMeasurements!=''):
                if abs(hipMeasurements[minInd] - profilehip) < hipStd:
                    result['hip']['best fit'] = sizes[minInd]
                    result['hip']['tighter'] = sizes[minInd - 1]
                    result['hip']['looser'] = sizes[minInd + 1]
                else:
                    if hipMeasurements[minInd] - profilehip > 0:
                        result['hip']['looser'] = sizes[minInd]
                        result['hip']['best fit'] = sizes[minInd - 1]
                        result['hip']['loose'] = sizes[minInd + 1]
                    else:
                        result['hip']['tighter'] = sizes[minInd]
                        result['hip']['tight'] = sizes[minInd - 1]
                        result['hip']['best fit'] = sizes[minInd + 1]

    elif minInd == (len(temp) - 1):
        result['best fit'] = sizes[minInd]
        result['tighter'] = sizes[minInd - 1]
        if(profileBust!='' and bustMeasurements!=''):
            if(abs(bustMeasurements[minInd] - profileBust) < BustStd):
                result['bust']['best fit'] = sizes[minInd]
                result['bust']['tighter'] = sizes[minInd - 1]
            else:
                if bustMeasurements[minInd] - profileBust > 0:
                    result['bust']['looser'] = sizes[minInd]
                    result['bust']['best fit'] = sizes[minInd - 1]
                else:
                    result['bust']['tighter'] = sizes[minInd]
                    result['bust']['tight'] = sizes[minInd - 1]



        if(profileWaist!='' and waistMeasurements!=''):
            if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
                result['waist']['best fit'] = sizes[minInd]
                result['waist']['tighter'] = sizes[minInd - 1]
            else:
                if waistMeasurements[minInd] - profileWaist > 0:
                    result['waist']['looser'] = sizes[minInd]
                    result['waist']['best fit'] = sizes[minInd - 1]
                else:
                    result['waist']['tighter'] = sizes[minInd]
                    result['waist']['tight'] = sizes[minInd - 1]

        if(profilehip!='' and hipMeasurements!=''):
                if abs(hipMeasurements[minInd] - profilehip) < hipStd:
                    result['hip']['best fit'] = sizes[minInd]
                    result['hip']['tighter'] = sizes[minInd - 1]
                else:
                    if hipMeasurements[minInd] - profilehip > 0:
                        result['hip']['looser'] = sizes[minInd]
                        result['hip']['best fit'] = sizes[minInd - 1]
                    else:
                        result['hip']['tighter'] = sizes[minInd]
                        result['hip']['tight'] = sizes[minInd - 1]

    if minInd == 0:
        result['best fit'] = sizes[minInd]
        result['looser'] = sizes[minInd + 1]
        if(profileBust!='' and bustMeasurements!=''):
            if(abs(bustMeasurements[minInd] - profileBust) < BustStd):
                result['bust']['best fit'] = sizes[minInd]
                result['bust']['looser'] = sizes[minInd + 1]
            else:
                if bustMeasurements[minInd] - profileBust > 0:
                    result['bust']['looser'] = sizes[minInd]
                    result['bust']['loose'] = sizes[minInd + 1]
                else:
                    result['bust']['tighter'] = sizes[minInd]
                    result['bust']['best fit'] = sizes[minInd + 1]



        if(profileWaist!='' and waistMeasurements!=''):
            if abs(waistMeasurements[minInd] - profileWaist) < waistStd:
                result['waist']['best fit'] = sizes[minInd]
                result['waist']['looser'] = sizes[minInd + 1]
            else:
                if waistMeasurements[minInd] - profileWaist > 0:
                    result['waist']['looser'] = sizes[minInd]
                    result['waist']['loose'] = sizes[minInd + 1]
                else:
                    result['waist']['tighter'] = sizes[minInd]
                    result['waist']['best fit'] = sizes[minInd + 1]

        if(profilehip!='' and hipMeasurements!=''):
                if abs(hipMeasurements[minInd] - profilehip) < hipStd:
                    result['hip']['best fit'] = sizes[minInd]
                    result['hip']['looser'] = sizes[minInd + 1]
                else:
                    if hipMeasurements[minInd] - profilehip > 0:
                        result['hip']['looser'] = sizes[minInd]
                        result['hip']['loose'] = sizes[minInd + 1]
                    else:
                        result['hip']['tighter'] = sizes[minInd]
                        result['hip']['best fit'] = sizes[minInd + 1]
    return JsonResponse(result)

def GetMeasurements(request):
    profileSize = json.loads(request.POST.get('profileSize'))['data']
    sizeDict = json.loads(request.POST.get('sizeDict'))['data']

    ind = sizeDict['sizes'].index(profileSize)

    result = {}
    if "busts" in sizeDict:
        result['bust'] = sizeDict['busts'][ind]
    if "waists" in sizeDict:
        result['waist'] = sizeDict['waists'][ind]
    if "hips" in sizeDict:
        result['hip'] = sizeDict['hips'][ind]
    return JsonResponse(result)
