# from .female import fit ,standard , fullsize , range , bodyshape
# from .male import fit , standard , fullsize , bodyshape
import sys

from customers.serializers import ProfileSerializer
from fitalgorithms.utility_helper import in_to_cm
from insights.models import Profile_Try_Product
from stores.models import Variant
from .utils import *


def None2Zero(body_part_variant_list):
    """
        We convert body part value hips/waist/shoulder to zero if it's None
        Those required attributes `body parts` do not need to fill all of them
        Hence we specify which is required by the product type, for example jeans
        doesn't require to get shoulder value from each variant of the product
    """
    return [body_part_variant if not body_part_variant is None
            else 0 for body_part_variant in
            body_part_variant_list]


def fit_product(product, profile):
    # convert from queryset form into tuple form
    (sizes, busts, hips, shoulders, waists) = Variant.group_variants(
        product.variants.all())
    # zero out all None values
    busts = None2Zero(busts)
    hips = None2Zero(hips)
    shoulders = None2Zero(shoulders)
    waists = None2Zero(waists)

    # just catch the profile body measurements
    bust_profile = profile.bust
    hip_profile = profile.hips
    waist_profile = profile.waist
    shoulder_profile = profile.shoulder
    # convert them if its neccessary
    if profile.metric_length == 'in':
        bust_profile = in_to_cm(bust_profile)
        hip_profile = in_to_cm(hip_profile)
        waist_profile = in_to_cm(waist_profile)
        shoulder_profile = in_to_cm(shoulder_profile)
    #    busts=[in_to_cm(b) for b in busts]
    #    waists=[in_to_cm(b) for b in waists]
    #    hips=[in_to_cm(b) for b in hips]
    #    shoulders=[in_to_cm(b) for b in shoulders]
    # call the fit algorithm with data from the product as well as from profile
    # Changes by Nour Alhadi: stretch_percentage = product.fabric & fabric and denim were not there before

    print(profile.gender, product.fit_type, product.elasticity, product.fabric, product.denim, product.product_type,
          busts, hips, waists, shoulders, bust_profile, hip_profile, waist_profile, shoulder_profile)

    obj = fitsys(gender=profile.gender,
                 fit=product.fit_type,
                 stretch_percentage=product.elasticity,
                 fabric=product.fabric,
                 denim=product.denim,
                 type=product.product_type,
                 sporty=False,
                 sizes=sizes,
                 busts=busts,
                 hips=hips,
                 waists=waists,
                 shoulders=shoulders,
                 bust=bust_profile,
                 hip=hip_profile,
                 waist=waist_profile,
                 shoulder=shoulder_profile)

    '''
        generate stress map, i.e on each body part, `location of the body`
        how fit the variant will be, such as on shoulder= well fitted
        see doc of `generate_stress_map` method
    '''
    # def dump(obj):
    #    for attr in dir(obj):
    #        if hasattr( obj, attr ):
    #            print( "obj.%s = %s" % (attr, getattr(obj, attr)))

    # dump (obj)
    print(sizes)
    sys.stdout.flush()

    results = generate_stress_map(obj, sizes)
    # save the history of the fit process such as try data between product and profile
    product.yet_another_try(profile)
    # let the store know that this profile has visited it, to get some insight out of it
    product.store.yet_another_visitor(profile)
    '''
        Insert a new record with date.NOW()
        to say that the profile `x` tried right now the product `y`
    '''
    Profile_Try_Product.objects.create(
        product=product, profile=profile)

    '''
        TODO maybe we should return product image that matches
        the variant instead of the generic image
     '''
    # best_fit =
    data = {'profile': ProfileSerializer(profile).data,
            'results': results,
            'product_image': product.image,
            'bodyshape': profile.body_shape,
            }
    return data
