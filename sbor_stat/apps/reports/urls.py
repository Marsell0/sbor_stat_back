from django.urls import path
from .views import pck_report, pck_report_excel, ReportsByPCKView, create_report, user_reports

urlpatterns = [
    path('api/pck-report/', pck_report),
    path('api/pck-report/excel/', pck_report_excel),
    path('api/by-pck/', ReportsByPCKView.as_view()),
    path('api/create_report/', create_report),
    path('api/user_reports/', user_reports),
]