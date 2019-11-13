def bodyshape(bust, height, waist, hips):
    whtr = round(waist / height, 2)
    # print(whtr)
    bodyshap = "Rectangle Body shape"
    if (whtr > 0.6):
        bodyshap = "Oval Body shape"
    elif (hips / bust > 1.05):
        if (whtr <= 0.5):
            bodyshap = "pear Body shape"
        elif (0.5 < whtr <= 0.6):
            bodyshap = "Pear body shape with a bit tummy fat."
    elif (bust / hips > 1.05):
        if (whtr <= 0.5):
            bodyshap = "inverted triangle Body shape"
        elif (0.5 < whtr <= 0.6):
            bodyshap = "inverted triangle Body shape with a bit tummy fat."
    elif (whtr < 0.5):
        bodyshap = "Hourglass body shape"
    elif (0.5 <= whtr <= 0.6):
        bodyshap = "Rectangle Body shape"
    return bodyshap
