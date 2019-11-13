from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

from fitalgorithms.utils import bodyshape, measure, please_refactor_me
from customers.model_util import *


class Customer(models.Model):
    """
        In our app logic we could assign multiple profiles to one customer, and it return
        customer have to be authenticated so a django user has been bound to it with
        a OneToOne relationship
    """
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='customer_user')
    slug = models.SlugField(
        unique=True, max_length=255, editable=False)

    class Meta:
        ordering = ('slug',)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.email)
        super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.slug


class Profile(models.Model):
    """
        null=True, this could happen when an anonymous customer wants
        to try product,please notice that editable=False, we want to insure
        that creating new profile is either going through unregistered customer
        or registered one.
        NOTE, if we allow to bound profile to registered customer that was
        previously unregistered, all history data such as `profile try product`,
        `profile visits store` will be bounded to the new registered customer though
        when those activities had occurred it was bounded to anonymous customer.
     """
    customer = models.ForeignKey(
        'customers.Customer', on_delete=models.CASCADE, related_name='customer_profile',
        null=True, editable=False)
    name = models.TextField(default="unnamed")
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)
    # male and female differs in naming conventions such as bust and chest are the same
    bust = models.FloatField(null=True)
    waist = models.FloatField(null=True)
    # male name convention for hips is seat. just naming conventions
    hips = models.FloatField(null=True)
    # female don't need to enter a shoulder value since it's not used in female fit algorithm
    shoulder = models.FloatField(null=True)
    gender = models.CharField(max_length=1,
                              choices=(('M', 'Male'),
                                       ('F', 'Female')),
                              default='M')
    '''
        we make sure to save metric length as well as
        metric weight because front-end is ignostic about it,
        Hence we need to convert to cm and kg while using the fitalgorithms package
    '''
    metric_length = models.CharField(max_length=2,
                                     choices=(('cm', 'cm'),
                                              ('in', 'in')),
                                     default='cm')
    metric_weight = models.CharField(max_length=2,
                                     choices=(('kg', 'kg'),
                                              ('lb', 'lb')),
                                     default='kg')
    # it's used solely for front-end
    skin = models.CharField(max_length=5,
                            choices=(('dark', 'dark'),
                                     ('light', 'light')),
                            default='light')
    # the below fields are results when the above fields are filled
    body_shape = models.CharField(
        max_length=bodyshape_choices.max_length,
        choices=bodyshape_choices.choices,
        null=False)
    top_size = models.CharField(
        max_length=bodySize_choices.max_length,
        choices=bodySize_choices.choices,
        null=False)
    bottom_size = models.CharField(
        max_length=bodySize_choices.max_length,
        choices=bodySize_choices.choices,
        null=False)

    def calculate_bodyshape(self):
        # TO CONVERT from in to cm
        # TODO needs to be refactored, you could use method attribute `dynamic`
        bust_profile = self.bust
        hip_profile = self.hips
        waist_profile = self.waist
        # convert them if its neccessary
        # if(self.metric_length == 'in'):
        #    bust_profile = in_to_cm(bust_profile)
        #    hip_profile = in_to_cm(hip_profile)
        #    waist_profile = in_to_cm(waist_profile)
        self.body_shape = bodyshape(self.gender, bust=bust_profile,
                                    height=self.height, waist=waist_profile,
                                    hips=hip_profile)

    def save(self, *args, **kwargs):
        """
            Here we get those outputs before commiting the profile isntance data to
            the database since we are making the validation resides on the serializer
            layer, we are pretty sure that all the required attributes are in its
            respective domains
        """
        self.clean()
        self.calculate_bodyshape()
        standardsizes = measure(gender=self.gender, bust=self.bust,
                                hips=self.hips, waist=self.waist,
                                shoulder=self.shoulder,
                                metric=self.metric_length)
        self.top_size, self.bottom_size = please_refactor_me(
            self.metric_length, self.gender, standardsizes)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        ordering = ('name',)
        '''
            impose two constraint, the former is for the sake of customer
            has multi profiles, each of them is unique, while the latter is
            required to handle the case where anonymous customer is trying
            product to prevent creating an existing 'unregistered' profile
        '''
        unique_together = (("customer", "name"),
                           ("name", "height", "weight", "bust",
                            "waist", "shoulder", "hips", "gender",
                            "metric_length", "metric_weight"))

    def __str__(self):
        return self.name
