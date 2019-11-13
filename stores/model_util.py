import traceback

import vfrlight.config


class FieldChoice:
    """
        this as a wrapper for all hardcoded values that needs to be set in
        our database as a choice constraint.
    """

    def __init__(self, list_of_choices):
        self.listOfChoices = list_of_choices
        self.choices = [[x, x] for x in self.listOfChoices]
        self.max_length = max([len(item)
                               for item in self.listOfChoices])
        self.choices_dict = {x: x for x in list_of_choices}


# TODO those checks hoodies&sweatshirts","sweaters&cardigans are not found in fit
ProductTypeChoicesList = ["None", "tops", "top", "shirts", "shirt", "vests", "vest", "blouses", "blouse",
                          "pants", "pant", "suits", "suit", "shorts", "short", "culott",  "polo",
                          "hoodies & sweatshirts", "sweaters & cardigans", "skirts", "skirt",
                          "t-shirts", "t-shirt", "jeans", "jean", "blazers", "blazer", "jumpsuits", "jumpsuit",
                          "jackets", "jacket", "coats", "coat", "trousers", "trouser", "onesize",
                          "dresses", "dress", "tonics shirts", "hoodies and sweatshirts", "light weight jackets", 
                          "winter jackets", "fit and flare dress", "sheath dress", "shift dress", "shirt dress",
                          "crop top", "polo shirts"
                        ]

FittingTypeChoicesList = ["None", "closefit", "fitted", "semi fitted", "semifit",
                          "loose fit", "oversized", "skinny", "close fit", "fitted", "slim",
                          "regular fit", "semi fitted", "relaxed fit", "loose fit", "oversized",
                          "tailored fit", "pencil skirt", "straight", "a-line", "pleated", "flared", "gathered",
                          "fitted bodice"
                          ]
'''
    here we define two possible values for fabric while
    the actual algorithm implementation needs value in the range [0,50]
    currently we are throwing random values [0,25] (- stretch and [25,50] (- nonestretch

    `(-`, it means belongs in mathematical way
'''
fabricTypeChoicesList = ['stretch', 'nonestretch', 'knitted']
'''
    we could be more flexible when it comes to collection
    defined by admin on their stores, such flexibility could be
    adapted when it comes to different language other than english
 '''
collection_gender_list = ["women", "men"]
# currently supported plans, where the third one is considered to be prime plan
PlanChoiceList = [primary + " " + key for primary in vfrlight.config.Config.PLANS for key in
                  vfrlight.config.Config.PLANS[primary]]  # eg: Male Free , Male First , MaleAndFemale First
'''
    when we are creating a new recurring charge to be confirmed by the admin
    the charge follow these states.
    first it gets in pending mode then if he confirms or declines
    it gets accepted/declined respectively, and finally once we have an
    accepted plan we could easily activated.
    please note that there is many scenarios I could clarify right here
     1) If Admin declines a charge nothing happens
     2) If Admin accepted some plan and we activated, and after that he
        wants to upgrade i.e (Male/Female)->(MaleAndFemale)
            or downgrade i.e (MaleAndFemale)->(Male/Female)
        we create new charge and we activate it if it gets accepted by the admin
        WHAT THAT MEANS?
            it means we don't cancel the previous charge explicitly, we let shopify
            handle that.
        OK BUT WHY?
            because if we cancel it by ourselves, it means the admin
            have to FULLY pay for the billing amount specified each month
            even if there is many days to the end of the month.
            BUT if shopify handle the cancel operation, then shopify calculate only
            how many days spent and charge him appropriately and the new charge will
            be set starting from the current date.

            see https://help.shopify.com/api/charging-for-your-app/faq

'''
plan_status_list = ['pending', 'accepted', 'active']

# defaultHeightMeasurementChoicesList = ["cm","inch"]
# defaultWeightMeasurementChoicesList = ["kg","pound"]

# instantiate field choice for all the lest above
productType = FieldChoice(ProductTypeChoicesList)
product_fit_Type = FieldChoice(FittingTypeChoicesList)
fabricType = FieldChoice(fabricTypeChoicesList)
plans = FieldChoice(PlanChoiceList)
plan_status: FieldChoice = FieldChoice(plan_status_list)


# defaultHeightMeasurement = FieldChoice(defaultHeightMeasurementChoicesList)
# defaultWeightMeasurement = FieldChoice(defaultWeightMeasurementChoicesList)

def validate_variant_range(gender, body_part, value, variant_ranges, metric, is_person=False):
    print('Gender: {}, Body Part: {}, Variant Ranges: {}, Metric: {}'.format(gender, body_part, variant_ranges, metric))
    # As for profile, it's required to fill all additional values
    if not value:
        if is_person:
            return "{} is required".format(body_part)
        '''
            return None i.e no error has occurred, please see how this method gets
            called and errors are accumulated accordingly
        '''
    return None

    # if(not metric == 'cm'):
    #    value = in_to_cm(value)

    # Variant_Range = Variant_Ranges[gender]
    # (min_value, max_value) = (Variant_Range[0], Variant_Range[1])

    # if not (value >= min_value and value <= max_value):
    #     if(not metric == 'cm'):
    #         min_value, max_value = cm_to_in(min_value), cm_to_in(max_value)
    #     return (body_part + " value is not in the range [{},{}] for {}".format(
    #             min_value, max_value, gender))


class VariantRangesDict:
    """
        validation ranges for F:Female and M:Males
        notice that we unified the names for males and females
        such as seat for male is considered to be hips
        and chest is also bust, notice that all values are compared in cm metric
        so variable with inch is converted first then we apply this validation thing
    """
    profile_ranges = {'bust': {'F': (0, 2000), 'M': (0, 2000)},
                      'waist': {'F': (0, 2000), 'M': (0, 2000)},
                      'hips': {'F': (0, 2000), 'M': (0, 2000)},
                      'shoulder': {'F': (0, 2000), 'M': (0, 2000)}, }

    product_ranges = {'bust': {'F': (0, 2000), 'M': (0, 2000)},
                      'waist': {'F': (0, 2000), 'M': (0, 2000)},
                      'hips': {'F': (0, 2000), 'M': (0, 2000)},
                      'shoulder': {'F': (0, 2000), 'M': (0, 2000)}, }


body_parts_list = ['shoulder', 'waist', 'hips', 'bust']
body_parts_choiceField = FieldChoice(body_parts_list)


def from_product_type_to_required_body_parts(variant_product_type, gender):
    """
        we design dictionary `switcher` to be more flexible once we have more
        product's type added in the future.
        it's used to impose a required_attributes constraint on variants of products
        since we have the product type we mostly need not all attributes to be filled
        by the merchant, i.e for jeans as a product type why do we have to fill shoulder measure
    """

    body_parts = {x: x for x in body_parts_list}
    switcher = {
        productType.choices_dict['hoodies and sweatshirts']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['sweaters & cardigans']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['tonics shirts']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['winter jackets']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['light weight jackets']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['jackets']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['jacket']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['coats']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['coat']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['blazers']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['blazer']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['vests']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['vest']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['shirts']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['shirt']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['t-shirts']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['t-shirt']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['jeans']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['jean']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['trousers']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['trouser']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['shorts']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['short']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['pants']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['pant']:
            [body_parts['waist'], body_parts['hips']],
        productType.choices_dict['dresses']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['dress']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['fit and flare dress']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['sheath dress']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['shift dress']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['shirt dress']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],

        productType.choices_dict['blouses']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['blouse']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['jumpsuits']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['jumpsuit']:
            [body_parts['bust'], body_parts['waist'],
             body_parts['hips']],
        productType.choices_dict['tops']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['top']:
            [body_parts['bust'], body_parts['waist']],

        productType.choices_dict['skirts']:
            [body_parts['hips'], body_parts['waist']],
        productType.choices_dict['skirt']:
            [body_parts['hips'], body_parts['waist']],
        # TODO: Jaber please check if only bust & waist are needed (I've only added them!!)
        productType.choices_dict['crop top']:
            [body_parts['bust'], body_parts['waist']],
        productType.choices_dict['polo shirts']:
            [body_parts['bust'], body_parts['waist']],

    }
    required_attributes = [body_parts['hips'], body_parts['waist'],
                           body_parts['bust'], body_parts['shoulder']]
    try:
        required_attributes = switcher[variant_product_type]
    except AttributeError:
        traceback.format_exc()
    if gender == 'F' and 'shoulder' in required_attributes:
        required_attributes.remove('shoulder')
    return required_attributes
