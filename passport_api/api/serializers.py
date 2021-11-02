from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from api.models import Account, Passport
from passport_api.settings import DATE_FORMAT, DATE_INPUT_FORMATS


class PassportSerializer(serializers.ModelSerializer):
    date_of_issue = serializers.DateField(format=DATE_FORMAT,
                                          input_formats=DATE_INPUT_FORMATS)
    expiration_date = serializers.DateField(format=DATE_FORMAT,
                                            input_formats=DATE_INPUT_FORMATS)

    class Meta:
        model = Passport
        fields = ('number', 'country', 'date_of_issue', 'expiration_date')

    def validate(self, data):
        if data.get('date_of_issue') >= data.get('expiration_date'):
            raise serializers.ValidationError(
                'Дата выдачи паспорта не может быть '
                'позже даты окончания действительности.')


class AccountSerializer(serializers.ModelSerializer):
    passports = PassportSerializer(read_only=True, many=True)

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'photo', 'passports')


class CreateAccountSerializer(serializers.ModelSerializer):
    passports = PassportSerializer(many=True)
    photo = Base64ImageField()

    class Meta:
        model = Account
        fields = ('pk', 'first_name', 'last_name',
                  'email', 'photo', 'passports')

    def create(self, validated_data):
        passports = validated_data.pop('passports')
        account = Account.objects.create(**validated_data)
        for passport_data in passports:
            Passport.objects.create(owner=account, **passport_data)
        return account
