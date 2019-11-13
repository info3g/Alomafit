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