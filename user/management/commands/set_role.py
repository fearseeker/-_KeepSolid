from django.core.management.base import BaseCommand
from user.models import Account

class Command(BaseCommand):
    help = 'Устанавливает роль пользователя (админ или клиент)'

    def add_arguments(self, parser):
        parser.add_argument('email', type=str)
        parser.add_argument('role', type=str, choices=['admin', 'client'])

    def handle(self, *args, **kwargs):
        email = kwargs['email']
        role = kwargs['role']
        try:
            user = Account.objects.get(email=email)
            if role == 'admin':
                user.is_staff = True
            else:
                user.is_staff = False
            user.save()
            self.stdout.write(self.style.SUCCESS(f'Роль пользователя {email} изменена на {role}'))
        except Account.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Пользователь {email} не найден'))
