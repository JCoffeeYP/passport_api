from rest_framework import generics

from api.models import Account
from api.serializers import AccountSerializer, CreateAccountSerializer


class AccountList(generics.ListCreateAPIView):
    queryset = Account.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return AccountSerializer
        return CreateAccountSerializer


class AccountDetail(generics.RetrieveDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
