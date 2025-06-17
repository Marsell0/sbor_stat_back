from django.urls import path
from .views import export_admin_reports_excel, filtered_reports_by_pck, export_reports_excel, create_report, user_reports, report_detail, reports_by_pck, check_report, update_report, get_admin_reports

urlpatterns = [
    path('api/chairman/reports/filter/', filtered_reports_by_pck),
    path('api/chairman/reports/export/', export_reports_excel),
    path('api/create_report/', create_report),
    path('api/user_reports/', user_reports),
    path('api/report/<int:pk>/', report_detail),
    path('api/chairman/reports/', reports_by_pck),
    path('api/chairman/check/<int:report_id>/', check_report),
    path('api/report/<int:report_id>/edit/', update_report),
    path('api/admin/reports/', get_admin_reports),
    path('api/admin/reports/export/', export_admin_reports_excel),


]