from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeacherCreateSerializer
from .models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login

# регистрация преподавателя председателем
class RegisterTeacherView(APIView):
    def post(self, request):
        print(request.data)
        
        serializer = TeacherCreateSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Преподаватель создан'}, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def teacher_list(request):

    teachers = User.objects.filter(role='teacher', pck="it")
    return Response([
        {'role': t.role, 'username': t.username} for t in teachers
    ])


@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Введите имя пользователя и пароль'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)

    if not user.check_password(password):
        return Response({'error': 'Неверный пароль'}, status=status.HTTP_401_UNAUTHORIZED)

    return Response({
        'username': user.username,
        'role': user.role,
        'pck': user.pck
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_user_info(request):
    username = request.data.get('username')

    if not username:
        return Response({'error': 'Имя пользователя не указано'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.get(username=username)
        return Response({
            'username': user.username,
            'role': user.role,
            'pck': user.pck
        })
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)