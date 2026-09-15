


from django.db import models


class AttendingTextChoices(models.TextChoices):
    PENDING = 'PENDING', 'Моля, изберете...'
    YES = 'YES', 'С удоволствие ще присъствам'
    NO = 'NO', 'За съжаление няма да мога'