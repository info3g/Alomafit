from rest_framework import permissions

from customers.models import Customer, Profile
from vfrlight.util import get_or_raise


class IsCustomerAuthenticated(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsCustomerProfiles(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        # Write permissions are only allowed to the owner of the snippet.
        # return True
        return obj.customer.user == request.user


class CustomerAccessOtherProfile(permissions.BasePermission):
    message = "you are accessing other profile, please check for the correct id"

    def has_permission(self, request, view):
        kwargs = request.__dict__['parser_context']['kwargs']
        customer_slug, profile_id = kwargs['slug_slug'], kwargs['id_pk']
        customer = get_or_raise(Customer, slug=customer_slug)
        profile = get_or_raise(Profile, id=profile_id)
        return profile.customer == customer
