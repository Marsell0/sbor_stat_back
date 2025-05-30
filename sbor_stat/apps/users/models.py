from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Убираем ненужные поля от наследования
    first_name = None
    last_name = None
    last_login = None
    is_superuser = None
    is_staff = None
    email = None
    created_at = None
    is_active = None
    date_joined = None

    # Роли пользователей
    ROLE_ADMIN = 'admin'
    ROLE_PCK = 'chairman'
    ROLE_TEACHER = 'teacher'
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Администратор'),
        (ROLE_PCK, 'Председатель ПЦК'),
        (ROLE_TEACHER, 'Преподаватель'),
    ]

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default=ROLE_TEACHER,
        help_text='Роль пользователя в системе'
    )

    # Принадлежность к ПЦК
    PCK_IT = 'it'
    PCK_ECO = 'eco'
    PCK_GEN = 'gen'
    PCK_CRE = 'cre'
    PCK_CHOICES = [
        (PCK_IT, 'Информационные технологии'),
        (PCK_ECO, 'Экономические дисциплины'),
        (PCK_GEN, 'Общеобразовательные дисциплины'),
        (PCK_CRE, 'Креативные индустрии'),
    ]

    pck = models.CharField(
        max_length=3,
        choices=PCK_CHOICES,
        null=True,
        blank=True,
        help_text='Принадлежность пользователя к ПЦК'
    )

    # Убираем username help_text, отображаемю строку
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"