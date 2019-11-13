from stores.model_util import fabricType
from . import female, male


def bodyshape_OUTPUT():
    return {
        'Hourglass body shape': 'Hourglass body shape',
        'Oval Body shape': 'Oval Body shape',
        'Pear body shape with a bit tummy fat.': 'Pear body shape with a bit tummy fat.',
        'Rectangle Body shape': 'Rectangle Body shape',
        'Rectangle Body shape with a bit tummy fat.': 'Rectangle Body shape with a bit tummy fat.',
        'inverted triangle Body shape': 'inverted triangle Body shape',
        'inverted triangle Body shape with a bit tummy fat.': 'inverted triangle Body shape with a bit tummy fat.',
        'inverted triangle body shape with a bit tummy fat.': 'inverted triangle body shape with a bit tummy fat.',
        'pear Body shape': 'pear Body shape',
        'trapazod': 'trapazod',
        'triangle Body shape': 'triangle Body shape',
        'triangle body shape with a bit tummy fat.': 'triangle body shape with a bit tummy fat.'
    }


def please_refactor_me(metric_length, gender, standardsizes):
    if (gender.lower() == 'm'):
        top_size = standardsizes.rule_topsize_cm()
        bottom_size = standardsizes.rule_bottomsize_cm()
    else:
        if (metric_length == 'cm'):
            top_size = standardsizes.rule_topsize_cm()
            bottom_size = standardsizes.rule_bottomsize_cm()
        else:
            top_size = standardsizes.rule_topsize_in()
            bottom_size = standardsizes.rule_bottomsize_in()

    return top_size, bottom_size


def generate_stress_map(obj, sizes):
    res = obj.notfit()

    if res:
        return {}

    def get_fit_data(fit):
        return {
            'size': fit.size,
            'stress_map': {location: accept for location, accept in
                           zip(fit.__dict__['location'],
                               fit.__dict__['accept'])}}

    # get best fit
    best_fit = obj.get_best_fit()
    # get the index of the variant, to decide later on, the upper/lower's fit data
    best_fit_index = sizes.index(best_fit.size)
    # generate stress_mape
    best_fit_data = get_fit_data(best_fit)
    # initialize other options, in case of fit algorithm did not respond well
    other_options = None
    lower_best_fit_data = upper_best_fit_data = {
        'size': None, 'stress_map': {}}
    try:
        # get all options
        other_options = {x.size: get_fit_data(x) for x
                         in obj.get_fitted()}
    except:
        pass
    if (other_options):
        # check if best fit is the largest size then we don't have an upper's fit data
        if (not (best_fit_index == len(sizes) - 1) and
                (sizes[best_fit_index + 1] in other_options.keys())):
            upper_best_fit_data = other_options[sizes[best_fit_index + 1]]
        # check if best fit is the smallest size then we don't have a lower one beside it
        if (not (best_fit_index == 0) and
                (sizes[best_fit_index - 1] in other_options.keys())):
            lower_best_fit_data = other_options[sizes[best_fit_index - 1]]

    data = {
        'best_fit': best_fit_data,
        'upper_size_best_fit_data': upper_best_fit_data,
        'lower_size_best_fit_data': lower_best_fit_data
    }
    return data


def fitsys(*args, **kwargs):
    '''
        WHY you change fabric i.e stretch requirement from set of
        two elements into annonymous range that you did not specify
        it in any of the docuementations
    '''

    '''
       Females parameters:
           fit, stretch_percentage, type, sporty, sizes, busts,
           hips, waists, shoulders, bust, hip, waist, shoulder
       Male parameters:
           fit, stretch_percentage, type, sporty, sizes, chests,
           seats, waists, shoulders, chest, seat, waist, shoulder
    '''
    # TODO change stretch to a discrete variable takes value from [0,50]
    import random
    if (kwargs['stretch_percentage'] == fabricType.choices_dict['nonestretch']):
        kwargs['stretch_percentage'] = random.randint(0, 25)
    else:
        kwargs['stretch_percentage'] = random.randint(25, 50)
    gender = kwargs['gender']
    del kwargs['gender']
    if gender == 'M':
        return male.fitsys(*kwargs.values())
    else:
        return female.fitsys(*kwargs.values())


def fabrictype(gender, *args):
    if gender == 'M':
        return male.fabrictype(*args)
    else:
        return female.fabrictype(*args)


def measure(gender, *args, **kwargs):
    if gender == 'M':
        # TODO PLEASE GOD :(  WHY THIS IS HAPPENING!!! I'm TOO UGLY
        del kwargs['shoulder']
        return male.measure(*kwargs.values())
    else:
        return female.measure(*kwargs.values())


def full_size(gender, *args):
    if gender == 'M':
        return male.full_size(*args)
    else:
        return female.full_size(*args)


def size_range(gender, *args):
    if gender == 'M':
        return male.range(*args)
    else:
        return female.range(*args)


def bodyshape(gender, *args, **kwargs):
    if gender == 'M':
        return male.bodyshape(*args, **kwargs)
    else:
        return female.bodyshape(*args, **kwargs)
