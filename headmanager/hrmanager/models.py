from django.db import models


class Vacancy(models.Model):
    STATUS_CHOICES = [
        ('searching', 'Поиск'),
        ('closed', 'Закрыто'),
        ('waiting_response', 'Ожидание ответа')
    ]

    PRIORITY_CHOICES = [
        ("high", 'Высокий'),
        ('medium', 'Средний'),
        ('low', 'Низкий')
    ]

    post = models.CharField(max_length=255, verbose_name='Должность')
    company = models.CharField(max_length=255, verbose_name='Компания')
    description = models.CharField(max_length=255, verbose_name='Описание')
    e_mail = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=255, verbose_name='Номер телефона')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, verbose_name='Статус')
    priority = models.CharField(max_length=255, choices=PRIORITY_CHOICES, verbose_name='Приоритет')
    hr_manager = models.CharField(max_length=255, verbose_name='Ответственный HR')
    file = models.FileField(upload_to="vacancys_files/$Y/%m/$d/", verbose_name='Файл', null=True, blank=True)
    show = models.BooleanField(default=True)
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = "Вакансии"
        ordering = ['time_creat', 'time_update']


class Candidate(models.Model):

    STATUS_CHOICES = [
        ('in_progress', 'В обработке'),
        ('wait_response', 'Ожидание ответа'),
        ('sened_offer', 'Оффер отправлен'),
        ('need_call', 'Требуется звонок'),
        ('rejection', 'Отказ'),
        ('closed', 'Вакансия закрыта'),
        ('test_task', "Тест отправлен")
    ]

    post = models.CharField(max_length=255, verbose_name='Должность')
    name = models.CharField(max_length=255, verbose_name='ФИО')
    estimation = models.IntegerField(verbose_name='Оценка')
    e_mail = models.EmailField(verbose_name='Email')
    phone_number = models.CharField(max_length=255, verbose_name='номер телефона')
    status = models.CharField(max_length=255, choices=STATUS_CHOICES, verbose_name='Статус')
    hr_manager = models.CharField(max_length=255, verbose_name='Ответсвенный HR')
    in_archive = models.BooleanField(default=False)
    time_creat = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name = 'Кандидат'
        verbose_name_plural = 'Кандидаты'
        ordering = ['time_creat', 'time_update']
