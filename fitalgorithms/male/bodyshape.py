def bodyshape(bust, height, waist, hips):
    whtr = round(waist / height, 2)
    t = True
    # print(whtr)
    bodyshap = "Rectangle Body shape"
    if (whtr >= 0.73):
        t = False
        bodyshap = "Oval Body shape"

    elif (hips / bust > 1.1):
        t = False
        if (whtr <= 0.63):
            bodyshap = "triangle Body shape"
        elif (0.63 < whtr):
            bodyshap = "triangle body shape with a bit tummy fat."

    elif (bust / hips > 1.1):
        t = False
        if (waist / hips >= 1.06):
            bodyshap = "trapazod"
        if (whtr <= 0.53):

            bodyshap = "inverted triangle Body shape"
        elif ((whtr > 0.53)):
            bodyshap = "inverted triangle body shape with a bit tummy fat."

    if ((whtr >= 0.63) and (whtr < 0.73) and t):
        bodyshap = "Rectangle Body shape with a bit tummy fat."
    # if(whtr<=0.63):
    #   bodyshap="inverted triangle Body shape"
    # elif (0.63<whtr):
    #   bodyshap="trapazod."
    return bodyshap
