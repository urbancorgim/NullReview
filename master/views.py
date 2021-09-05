from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from movie.models import Movie
from account.models import User


def index(request):
    return render(request, 'main.html')


def master(request):
    if request.user.is_superuser:
        return render(request, 'master/index.html')
    else:
        return render(request, 'master/master.html')


def movies(request):
    page = request.GET.get('page', '1')
    movie_list = Movie.objects.order_by('-pub_date', 'title')
    paginator = Paginator(movie_list, 10)
    page_obj = paginator.get_page(page)
    context = {
        'page_obj': page_obj
    }

    return render(request, 'master/movies.html', context)


def users(request):
    user_list = User.objects.order_by('-date_joined', 'email')
    context = {
        'page_obj': user_list
    }
    return render(request, 'master/users.html', context)

def superuser(request, user_id):
    user = User.objects.get(pk=user_id)
    if user.is_superuser:
        user.is_superuser = False
    else :
        user.is_superuser = True
    user.save()
    return redirect('master:users')


def active(request, user_id):
    user = User.objects.get(pk=user_id)
    if user.is_active:
        user.is_active = False
    else:
        user.is_active = True
    user.save()
    return redirect('master:users')

