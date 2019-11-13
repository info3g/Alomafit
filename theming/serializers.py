from rest_framework import serializers
from rest_framework.exceptions import NotFound

from stores.models import Store
from theming.models import Theme


class ThemeSerializer(serializers.ModelSerializer):
    store_slug = serializers.CharField(read_only=True)
    store = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:
        model = Theme
        fields = '__all__'

    def create(self, validated_data):
        try:
            slug = self.context['request'].POST.get('store_slug')
            store = Store.objects.get(slug=slug)
            theme = Theme.objects.create(store=store, **validated_data)
        except Store.DoesNotExist:
            raise NotFound(detail="store {} not found".format(validated_data['store_slug']))
        return theme
