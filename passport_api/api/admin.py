from django.contrib import admin

from api.models import Account, Passport


class AccountAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'email')
    search_fields = ('email', )
    empty_value_display = 'empty'


class PassportAdmin(admin.ModelAdmin):
    list_display = ('pk', 'number', 'country',
                    'date_of_issue', 'expiration_date')
    search_fields = ('number', )
    empty_value_display = 'empty'


admin.site.register(Account, AccountAdmin)
admin.site.register(Passport, PassportAdmin)
