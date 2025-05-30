from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apps.users.models import User
from django.utils.dateparse import parse_date
from django.db.models import Prefetch
from datetime import datetime
from .models import Report
from .serializers import ReportSerializer
import calendar
from rest_framework import status
import io
import openpyxl
from django.http import HttpResponse

# функции админа
@api_view(['GET'])
def pck_report(request):
    month = request.GET.get('month')  # формат: 'YYYY-MM'
    if not month:
        return Response({'error': 'Параметр month обязателен'}, status=400)

    try:
        year, month_num = map(int, month.split('-'))
        start_date = datetime(year, month_num, 1).date()
        last_day = calendar.monthrange(year, month_num)[1]
        end_date = datetime(year, month_num, last_day).date()
    except:
        return Response({'error': 'Некорректный формат месяца'}, status=400)

    reports = Report.objects.filter(
        checked_by_head=True,
        date_created__range=(start_date, end_date),
        user__groups__name='ПЦК'
    ).prefetch_related('criteria', 'user')

    serializer = ReportSerializer(reports, many=True)
    return Response(serializer.data)

# не работает, нужно будет доделать(не выдает excel)

@api_view(['GET'])
def pck_report_excel(request):
    month = request.GET.get('month')
    if not month:
        return Response({'error': 'Параметр month обязателен'}, status=400)

    try:
        year, month_num = map(int, month.split('-'))
        start_date = datetime(year, month_num, 1).date()
        last_day = calendar.monthrange(year, month_num)[1]
        end_date = datetime(year, month_num, last_day).date()
    except:
        return Response({'error': 'Некорректный формат месяца'}, status=400)

    reports = Report.objects.filter(
        checked_by_head=True,
        date_created__range=(start_date, end_date),
    ).prefetch_related('criteria', 'user')

    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = 'Отчет ПЦК'
    ws.append(['Преподаватель', 'Мероприятие', 'Критерии'])

    for report in reports:
        criteria_names = ', '.join([c.name for c in report.criteria.all()])
        ws.append([str(report.user), report.event_name, criteria_names])

    buffer = io.BytesIO()
    wb.save(buffer)
    buffer.seek(0)

    response = HttpResponse(
        buffer,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="pck_report_{month}.xlsx"'
    return response

# функции председателя
class ReportsByPCKView(APIView):

    def get(self, request):

        # Получение месяца и года из query-параметров
        month = request.query_params.get('month')
        year = request.query_params.get('year')

        if not month or not year:
            return Response({'detail': 'Укажите месяц и год в параметрах запроса'}, status=400)

        try:
            month = int(month)
            year = int(year)
        except ValueError:
            return Response({'detail': 'Неверный формат месяца или года'}, status=400)

        # Фильтрация по ПЦК, дате создания и проверке
        reports = Report.objects.filter(
            teacher__pck=request.user.pck,
            checked=True,
            created_at__year=year,
            created_at__month=month
        ).select_related('teacher').prefetch_related('criteria')

        serialized = ReportSerializer(reports, many=True)
        return Response(serialized.data)
    
@api_view(['POST'])
def create_report(request):
    # if request.user.role != 'teacher':
    #     return Response({'detail': 'Нет прав'}, status=status.HTTP_403_FORBIDDEN)
    print(f"Преподаватель  {User.objects.get(id=4)}")
    try:
        
        
        teacher = User.objects.get(id=4, role='teacher')
    except:
        return Response({'detail': 'Преподаватель не найден'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ReportSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=teacher)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)