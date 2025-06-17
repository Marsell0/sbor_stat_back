from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeacherCreateSerializer
from .models import User
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login

@api_view(['POST'])
def create_teacher(request):
    username = request.data.get('username')
    password = request.data.get('password')
    pck = request.data.get('pck')

    if not all([username, password, pck]):
        return Response({'error': 'Необходимо указать имя, пароль и ПЦК'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь с таким именем уже существует'}, status=400)

    user = User(username=username, role='teacher', pck=pck)
    user.set_password(password)
    user.save()

    return Response({'message': f'Преподаватель {username} создан в ПЦК {pck}'})

    

@api_view(['POST'])
def get_teachers_by_pck(request):
    pck = request.data.get('pck')
    if not pck:
        return Response({'error': 'ПЦК не указано'}, status=400)

    teachers = User.objects.filter(role='teacher', pck=pck).values('id', 'username', 'date_joined')
    return Response(list(teachers))



@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username)
    print(password)

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
    

@api_view(['POST'])
def get_teachers_by_pck(request):
    pck = request.data.get('pck')
    if not pck:
        return Response({'error': 'ПЦК не указано'}, status=400)

    teachers = User.objects.filter(pck=pck, role='teacher')
    data = [{'id': t.id, 'username': t.username} for t in teachers]
    return Response(data)


@api_view(['POST'])
def assign_pck_head(request):
    user_id = request.data.get('user_id')
    pck = request.data.get('pck')

    if not user_id or not pck:
        return Response({'error': 'ID пользователя и ПЦК обязательны'}, status=400)

    existing = User.objects.filter(role='chairman', pck=pck).first()
    if existing:
        return Response({'error': f'Уже есть председатель ПЦК {pck} ({existing.username})'}, status=400)

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден'}, status=404)

    user.role = 'chairman'
    user.pck = pck
    user.save()

    return Response({'message': f'Пользователь {user.username} назначен председателем {pck}'})


@api_view(['POST'])
def create_pck_head(request):
    username = request.data.get('username')
    password = request.data.get('password')
    pck = request.data.get('pck')

    if not all([username, password, pck]):
        return Response({'error': 'username, password и pck обязательны'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Пользователь с таким именем уже существует'}, status=400)

    if User.objects.filter(role='chairman', pck=pck).exists():
        return Response({'error': f'В ПЦК {pck} уже есть председатель'}, status=400)

    user = User(
        username=username,
        role='chairman',
        pck=pck
    )
    user.set_password(password) 
    user.save()

    return Response({'message': f'Председатель {username} создан для ПЦК {pck}'})


@api_view(['GET'])
def list_chairman(request):
    heads = User.objects.filter(role='chairman').values('id', 'username', 'pck')
    return Response(list(heads))


@api_view(['POST'])
def remove_chairman(request):
    user_id = request.data.get('user_id')
    try:
        user = User.objects.get(id=user_id, role='chairman')
        user.role = 'teacher'
        user.save()
        return Response({'message': f'{user.username} снят с должности'})
    except User.DoesNotExist:
        return Response({'error': 'Председатель не найден'}, status=404)


@api_view(['DELETE'])
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({'message': 'Пользователь удален'})
    except User.DoesNotExist:
        return Response({'error': 'Пользователь не найден'}, status=404)


