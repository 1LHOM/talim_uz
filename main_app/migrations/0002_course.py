# Generated by Django 4.0.4 on 2022-06-18 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='')),
                ('image', models.ImageField(upload_to='course_images')),
                ('short_description', models.CharField(max_length=128, verbose_name='Короткое описание')),
                ('description', models.CharField(max_length=500, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.coursecategory')),
            ],
        ),
    ]
