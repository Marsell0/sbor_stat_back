from django.urls import path
from .views import create_teacher, get_teachers_by_pck, login_view, get_user_info, get_teachers_by_pck, assign_pck_head, create_pck_head, list_chairman, remove_chairman, delete_user


urlpatterns = [
    path('api/register-teacher/', create_teacher),
    path('api/teachers/', get_teachers_by_pck),
    path('api/login/', login_view),
    path('api/user-info/', get_user_info),
    path('api/chairman/teachers/', get_teachers_by_pck),
    path('api/admin/assign-chairman/', assign_pck_head),
    path('api/admin/create-chairman/', create_pck_head),
    path('api/admin/pck-chairmans/', list_chairman),
    path('api/admin/remove-chairman/', remove_chairman),
    path('api/admin/delete-user/<int:user_id>/', delete_user),


]