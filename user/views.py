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


class PhoneConfirm(APIView):

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
            serializer.save()

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

                return Response(status=status.HTTP_200_OK)
            else :
                
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class CheckPhone(APIView):

    permission_classes = []

    def post(self, request, format=None):

        try:

            exits = PhoneCode.objects.get(code=request.data["code"],phone=request.data["phone"])
            
            if exits:
                return Response(status=status.HTTP_200_OK)
            
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        except:

            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class CreateUser(APIView):

    permission_classes = []

    def post(self, request, format=None):

        try :
            if request.data['password'] == request.data['repassword'] :
                user = User.objects.create(
                    phone=int(request.data["phone"]),
                    firstName=request.data["firstName"],
                    lastName=request.data["lastName"],
                    email=request.data["email"],
                    is_superuser=False,
                    is_staff=False,
                    is_active=True,
                    user_type=2,
                )

                user.set_password(request.data["password"])
                user.save()

                return Response(status=status.HTTP_201_CREATED)
            
            else :
                return Response(status=status.HTTP_400_BAD_REQUEST)
        
        except :
        
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

class PasswordForget(APIView):

    permission_classes = []

    def post(self, request, format=None):

        try:

            exits = PhoneCode.objects.get(
                code=request.data["code"],phone=request.data["phone"]
            )

        except:

            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        if exits:

            user = User.objects.get(phone=int(request.data["phone"]))
            user.set_password = request.data["password"]
            user.save()

            return Response(status=status.HTTP_202_ACCEPTED)

        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
