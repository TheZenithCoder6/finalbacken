from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class RegisterView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        
        # Validation
        errors = {}
        
        if not username:
            errors['username'] = ['Username is required']
        elif User.objects.filter(username=username).exists():
            errors['username'] = ['Username already exists']
        
        if email:
            if User.objects.filter(email=email).exists():
                errors['email'] = ['Email already exists']
        else:
            errors['email'] = ['Email is required']
        
        if not password:
            errors['password'] = ['Password is required']
        else:
            try:
                validate_password(password)
            except ValidationError as e:
                errors['password'] = list(e.messages)
        
        if errors:
            return Response(errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        
        return Response(
            {
                'message': 'User created successfully',
                'username': user.username,
                'email': user.email
            },
            status=status.HTTP_201_CREATED
        )


# ✅ YEH CHECK ADMIN VIEW ADD KARO (Admin check karne ke liye)
class CheckAdminView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        # Check if user is staff/admin
        is_admin = request.user.is_staff or request.user.is_superuser
        return Response({
            'is_admin': is_admin,
            'username': request.user.username,
            'email': request.user.email
        })