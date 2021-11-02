from django.urls import path

from api.views import AccountDetail, AccountList

urlpatterns = [
    path('accounts/',
         AccountList.as_view(), ),
    path('accounts/<int:pk>/',
         AccountDetail.as_view(), ),
]
