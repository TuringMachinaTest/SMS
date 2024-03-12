from django.contrib.auth.models import User

from .models import City, Account, AccountUser
from rest_framework import serializers


class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    city_name = serializers.ReadOnlyField(source='city.name')
    created_by = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all())

    class Meta:
        model = Account
        fields = [
            'id', 'name',
            'address_line1', 'address_line2', 'address_line3',
            'city', 'city_name', 'zip_code',
            'email', 'phone_number1', 'phone_number2', 'whatsapp_number',

            'security_number',
            'memo',
            'police_number1', 'police_number2', 'police_number3',
            'fire_dept_number1', 'fire_dept_number2', 'fire_dept_number3',
            'emergency_number1', 'emergency_number2', 'emergency_number3',

            'partition_name1', 'partition_name2', 'partition_name3', 'partition_name4', 'partition_name5',
            'partition_name6', 'partition_name7', 'partition_name8', 'partition_name9', 'partition_name10',

            'created_at', 'updated_at', 'created_by'
        ]


class AccountUserSerializer(serializers.HyperlinkedModelSerializer):
    account = serializers.PrimaryKeyRelatedField(queryset=Account.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(default=serializers.CurrentUserDefault(), queryset=User.objects.all())

    class Meta:
        model = AccountUser
        fields = [
            'id', 'account', 'partition',
            'name', 'password',

            'in_out_codes',

            'phone_number1', 'phone_number2', 'phone_number3',
            'title',

            'holiday_begins', 'holiday_ends',
            'hot_user',
            'authorized_days_sat', 'authorized_days_sun', 'authorized_days_mon',
            'authorized_days_tue', 'authorized_days_wed', 'authorized_days_thu',
            'authorized_days_fri',

            'created_at', 'updated_at', 'created_by'
        ]
