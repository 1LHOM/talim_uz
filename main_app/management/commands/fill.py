import json

from django.conf import settings
from django.core.management import BaseCommand

# from auth_app.models import SchoolUser
from auth_app.models import SchoolUser
from main_app.models import Course, CourseCategory, News


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)


class Command(BaseCommand):

    def handle(self, *args, **options):
        # news = load_from_json('news')
        # News.objects.all().delete()
        # for cat in news:
        #     News.objects.create(**cat)
        #
        # categories = load_from_json('coursecategory')
        # CourseCategory.objects.all().delete()
        # for cat in categories:
        #     CourseCategory.objects.create(**cat)

        courses = load_from_json('course')
        Course.objects.all().delete()
        for course in courses:
            category_id = course['category']
            _cat = CourseCategory.objects.get(name=category_id)
            course['category'] = _cat
            Course.objects.create(**course)

        # shop_admin = SchoolUser.objects.create_superuser(
        #     username='ilhom',
        #     password='root',
        #     email='ilhomjon.erkinov@mail.ru'
        # )

