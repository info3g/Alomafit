import random

from stores.serializers import *


def updateProduct_factory(product, ignore_variant=False):
    """
        Here we assume that product is partially filled as if its instantiated
        when syncing with shopify.
        it updates all product's variants with dummy validated values
        and returns ProductSerializer data
    """
    product.product_type = random.choice(productType.listOfChoices[1:])
    product.fit_type = random.choice(product_fit_Type.listOfChoices[1:])
    product.elasticity = random.uniform(1, 100)
    product.fabric = random.choice(fabricType.listOfChoices)
    product._required_attributes = from_product_type_to_required_body_parts(
        product.product_type, product.gender)
    productSerialized = ProductSerializer(product).data
    productSerialized['variants'] = []
    for variant in product.variants.all():
        if not ignore_variant:
            for _required_attribute in product._required_attributes:
                variant.__dict__[_required_attribute] = random.uniform(
                    VariantRangesDict.product_ranges[_required_attribute][product.gender][0],
                    VariantRangesDict.product_ranges[_required_attribute][product.gender][1])
            productSerialized['variants'].append(
                VariantSerializer(variant).data)
    return productSerialized
