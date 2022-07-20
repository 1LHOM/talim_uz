from django.db import models


class CourseCategory(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name='Название')
    description = models.CharField(max_length=255, verbose_name='Описание', blank=True)

    def __str__(self):
        return self.name

    # class Meta показывает кастомную имя для этого меделья в Админке
    class Meta:
        verbose_name = 'категория курсов'
        verbose_name_plural = 'категории курсов'


class Course(models.Model):
    category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE, verbose_name='Категория')
    name = models.CharField(max_length=128, verbose_name='Имя курса')
    image = models.ImageField(upload_to='course_images', verbose_name='Изображение курса')
    short_description = models.CharField(max_length=128, verbose_name='Короткое описание')
    description = models.TextField(verbose_name='Описание курса')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена', default=0)
    teacher = models.CharField(max_length=128, verbose_name='Преподаватель', blank=True)
    lessons_list = models.JSONField(null=True, verbose_name='Список уроков')
    lesson_data = models.JSONField(null=True, verbose_name='Данные курса')

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class News(models.Model):
    name = models.CharField(max_length=128, verbose_name='Заголовок новости')
    image = models.ImageField(upload_to='news_images', verbose_name='Изображение новости')
    short_desc = models.CharField(max_length=500, verbose_name='Короткое описание')
    full_text = models.TextField(verbose_name='Полный текст новости')
    # published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата пупликации')
    author = models.CharField(max_length=128, verbose_name='Автор')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'




