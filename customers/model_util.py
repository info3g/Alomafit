from fitalgorithms import female, male
from fitalgorithms.utils import bodyshape_OUTPUT
from stores.model_util import FieldChoice

'''
    those are used for validation purposes, as we dont permit the customer
    to enter values out of these domains
'''
min_height_cm_male, max_height_cm_male = 165, 210
min_weight_kg_male, max_weight_kg_male = 59, 140

min_height_cm_female, max_height_cm_female = 153, 190
min_weight_kg_female, max_weight_kg_female = 45, 120


def validate_height(height, metric_length, gender):
    print('Metric Length: {}, Gender: {}'.format(metric_length, gender))
    if not height:
        return "height is required"

    # if(not metric_length == 'cm'):
    #    height = in_to_cm(height)

    # (min_value, max_value) = (min_height_cm_male, max_height_cm_male) \
    #     if gender == "M" else (min_height_cm_female, max_height_cm_female)

    # if(not(height >= min_value and height <= max_value)):
    #     if(metric_length == 'in'):
    #         min_value, max_value = cm_to_in(min_value), cm_to_in(max_value)
    #     message = "This field: {}:{} cm, must be in between [{},{}].".format(
    #         'height', height, min_value, max_value)
    #     return message


def validate_weight(weight, metric_weight, gender):
    print('Metric Weight: {}, Gender: {}'.format(metric_weight, gender))
    if not weight:
        return "weight is required"
    # if(not metric_weight == 'kg'):
    #     weight = lb_to_kg(weight)

    # (min_value, max_value) = (min_weight_kg_male, max_weight_kg_male) \
    #     if gender == "M" else (min_weight_kg_female, max_weight_kg_female)

    # if(not(weight >= min_value and weight <= max_value)):
    #     if(metric_weight == 'lb'):
    #         min_value, max_value = kg_to_lb(min_value), kg_to_lb(max_value)
    #     message = "This field: {}:{} kg, must be in between [{},{}].".format(
    #         'weight', weight, min_value, max_value)
    #     return message


bodyTopSizeListFemale = female.standard.measure.size_topsize()
bodyBottomSizeListFemale = female.standard.measure.size_bottomsize()

bodyBottomSizeListMale = male.standard.measure.size_bottomsize()

bodyTopSizeListMale = male.standard.measure.size_topsize()

'''
    notice here every time makemigrations is called, django will make migrations again
    since we don't fix this below field ahead of time, hence it's generated dynamically
    and it's used in profile model to act as a result after
    profile's body measurement has been filled, see save method of the profile model
'''
# TODO needs to be refactored
genericSizeList = list(set(bodyTopSizeListFemale + bodyBottomSizeListFemale +
                           bodyBottomSizeListMale + bodyTopSizeListMale))

bodyShapeList = bodyshape_OUTPUT().values()
bodyshape_choices = FieldChoice(list_of_choices=bodyShapeList)
bodySize_choices = FieldChoice(list_of_choices=genericSizeList)
