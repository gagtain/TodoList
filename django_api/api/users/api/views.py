from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from based.generic_api.generic_api_views import GenericAPIView
from users.api.serializers import TodoUserCreateSerializer, TodoUserManyDataSerializer
from users.models import TodoUser


class UserAPI(GenericAPIView):
    serializer_class = TodoUserManyDataSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = TodoUser.objects.all()

    SERIALIZER = {
        'create': {
            "request": TodoUserCreateSerializer,
            "response": TodoUserManyDataSerializer
        }
    }


class ObtainTokenPairView(TokenObtainPairView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = TokenObtainPairSerializer


    def post(self, request, *args, **kwargs):


        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        return self.set_response(data=serializer.validated_data)

    @classmethod
    def set_response(cls, data):
        access = data.get("access", None)
        if access is not None:
            return Response({"access": access}, status=200)

        return Response({"Error": "Something went wrong"}, status=status.HTTP_400_BAD_REQUEST)