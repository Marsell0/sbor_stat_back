from django.urls import path
from .views import RegisterTeacherView, teacher_list, login_view, get_user_info


urlpatterns = [
    path('api/register-teacher/', RegisterTeacherView.as_view(), name='register-teacher'),
    path('api/teachers/', teacher_list),
    path('api/login/', login_view),
    path('api/user-info/', get_user_info),
]