import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from main_app.models import Course, CourseCategory, News


def index(request):
    news_list = News.objects.all()[:5]

    context = {
        'title': 'Главная',
        'news_list': news_list,
    }
    return render(request, 'main_app/index.html', context)


def courses(request, pk=None):
    categories_list = CourseCategory.objects.all()
    courses_list = None

    if pk is not None:
        if pk == 0:
            courses_list = Course.objects.all()
        else:
            courses_list = Course.objects.filter(category__pk=pk)

    context = {
        'categories_list': categories_list,
        'courses_list': courses_list,
        'title': 'Каталог курсов',
    }
    return render(request, 'main_app/courses.html', context)


@login_required
def my_learnings(request):
    return render(request, 'main_app/my-learnings.html')


@login_required
def example_course(request, pk=None, lesson_num=None):

    if pk == 0:
        return render(request, 'main_app/example-lesson.html')

    context = {
        'current_lesson': get_object_or_404(Course, pk=pk),
        'lesson_num': lesson_num,
    }

    if pk is not None:
        # if pk == 1:

        return render(request, 'main_app/homework.html', context)


def view_post(request, pk=None):
    context = {
        'title': 'Новости',
        'post': get_object_or_404(News, pk=pk)
    }
    return render(request, 'main_app/view-post.html', context)


def view_course(request, pk=None):

    course_object = get_object_or_404(Course, pk=pk)
    if pk is not None:
        context = {
            'title': f'{course_object.name}',
            'course': course_object

        }
        return render(request, 'main_app/view-course.html', context)
    else:
        pass

