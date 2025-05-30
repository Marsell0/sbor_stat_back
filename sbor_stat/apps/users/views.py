from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TeacherCreateSerializer
from .models import User
from rest_framework.decorators import api_view

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