from django.urls import path
from .views import RegisterTeacherView, teacher_list

urlpatterns = [
    path('api/register-teacher/', RegisterTeacherView.as_view(), name='register-teacher'),
    path('api/teachers/', teacher_list),
]