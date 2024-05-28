from django.db.models import Q
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from users.serializers import RegisterSerializer, LoginSerializer
from users.models import Account


class AccountRegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        username = serializer.data.get("username")
        tokens = Account.objects.get(username=username).tokens
        user_data["tokens"] = tokens
        return Response(
            {"success": True, "data": user_data}, status=status.HTTP_201_CREATED
        )


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            {"success": True, "data": serializer.data}, status=status.HTTP_200_OK
        )
