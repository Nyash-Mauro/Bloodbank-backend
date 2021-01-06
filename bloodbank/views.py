from rest_framework import status
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .renderer import UserJSONRenderer
from .serializer import *
from .models import *
from django.contrib.auth import login
from knox.models import AuthToken
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework import generics, permissions
from knox.views import LoginView as KnoxLoginView
# class RegistrationAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         user = request.data.get('user', {})
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_201_CREATED)


# class LoginAPIView(APIView):
#     permission_classes = (AllowAny,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = LoginSerializer

#     def post(self, request):
#         user = request.data.get('user', {})
#         serializer = self.serializer_class(data=user)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UserRetrieveUpdateAPIView(RetrieveUpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     renderer_classes = (UserJSONRenderer,)
#     serializer_class = UserSerializer

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(request.user)

#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def update(self, request, *args, **kwargs):
#         serializer_data = request.data.get('user', {})

#         serializer = self.serializer_class(
#             request.user, data=serializer_data, partial=True
#         )
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

#         return Response(serializer.data, status=status.HTTP_200_OK)


# class UserViewSet(viewsets.ModelViewSet):
#     """
#     A viewset for  user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()



class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)


class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user