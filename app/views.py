from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login 
from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken



def landing_view(request):
    return render(request,'landing.html',) 

class RegisterAPIView(APIView):
    def get(self,request):
        return render(request,'register.html')
    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(
                {
                    "message": "User created successfully"
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    
class LoginAPIView(APIView):
        def get(self,request):
             return render(request,'login.html')
        def post(self, request):

            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:
                login(request,user)
                refresh = RefreshToken.for_user(user)
                return redirect('dashboard')

                
                
                return Response(
                    
                    {
                        'message': 'Login successful',

                        'refresh': str(refresh),

                        'access': str(refresh.access_token),
                    },
                    status=status.HTTP_200_OK
                    
                )

            return Response(
                {
                    'error': 'Invalid credentials'
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
class DashboardAPIView(APIView):
     def get(self,request):
          return render(request,'dashboard.html')