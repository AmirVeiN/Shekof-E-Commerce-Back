import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from user.models import PhoneCode, User
from user.permissions import IsTypeOneUser
from user.serializers import CodePhoneSerializer
from sms_ir import SmsIr
import jwt
from django.conf import settings
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import AccessTokenSerializer, AdminUserSerializer, UserFillSerializer, UserSerializer

class SendCode(APIView):

    permission_classes = []

    def post(self, request, format=None):

        code = random.randint(11111, 99999)

        serializer = CodePhoneSerializer(
            data={
                "code": code,
                "phone": request.data["phone"],
            }
        )

        if serializer.is_valid():

            sms_ir = SmsIr(
                "o1Affme8CeJfdW8OuPMv1qo1f1JKDIy0vT7MKLvJvfkF6pgnre2ugXghVeAdQcKz",
                30007732011682,
            )

            sms = sms_ir.send_verify_code(
                number=f"+98{request.data["phone"]}",
                template_id=100000,
                parameters=[
                    {
                        "name": "code",
                        "value": f"{code}",
                    },
                ],
            )

            if sms.status_code == 200 :

                serializer.save()
                return Response({"ok":"code send"} ,status=status.HTTP_200_OK)
            else :
                
                return Response({"error":"sms.ir not found"} ,status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class CreateUser(APIView):

    permission_classes = []

    def post(self, request, format=None):

        try:

            exits = PhoneCode.objects.get(code=request.data["code"],phone=request.data["phone"])

            try :
                user_valid = User.objects.get(phone=request.data["phone"])
                
                if exits and user_valid:
                    refresh = RefreshToken.for_user(user_valid)
                    serializer = AccessTokenSerializer(data={'access': str(refresh.access_token), "refresh": str(refresh)})
                    serializer.is_valid(raise_exception=True)
                    token = serializer.validated_data
                    exits.delete()

                return Response(token ,status=status.HTTP_200_OK)
            
            except :
                
                if exits:
                    user = User.objects.create(
                    phone=request.data["phone"],
                    username = request.data["phone"],
                    is_superuser=False,
                    is_staff=False,
                    is_active=True,
                    user_type=2)
                    user.save()
                    exits.delete()
                    
                    refresh = RefreshToken.for_user(user)
                    serializer = AccessTokenSerializer(data={'access': str(refresh.access_token), "refresh": str(refresh)})
                    serializer.is_valid(raise_exception=True)
                    token = serializer.validated_data
                    return Response(token ,status=status.HTTP_201_CREATED)
        except:

            return Response({"error":"code not found or expired"} ,status=status.HTTP_406_NOT_ACCEPTABLE)

class FillInformation(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        try:
            user = User.objects.get(pk=request.user.id)

            serializer = UserFillSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"ok" : "user updated"}, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
class UserInformation(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        
        try:
            decoded_payload = jwt.decode(request.headers["Authorization"].split(" ")[1], settings.SECRET_KEY, algorithms=['HS256'])

            user_id = decoded_payload['user_id']

            user = User.objects.get(pk=user_id)

            serializer = UserSerializer(user)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

class GetAllUsers(APIView):

    permission_classes = [IsTypeOneUser]

    def get(self, request, format=None):
        
        try:
            model = User.objects.all()
            
            serializer = AdminUserSerializer(model, many=True)

            return Response(serializer.data, status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        
        
class Address(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        
        try:
            user = User.objects.get(pk=request.user.id)

            serializer = AdminUserSerializer(user, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response({"ok" : "user updated"}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
