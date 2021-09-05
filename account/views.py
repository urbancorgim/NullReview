from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserCreationForm
from django.contrib import auth
from django.contrib.auth import authenticate, login
from review.models import Review
from movie.models import Pick


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        print(request.user.id)
        return render(request, 'account/index.html')
    else:
        return redirect('account:login')


def signup(request):
    """
    계정생성
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('master:index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'account/signup.html', context)


@login_required(login_url='account:login')
def review(request):
    page = request.GET.get('page', '1')
    if page == '':
        page = '1'
    page = int(page)
    review_list = Review.objects.filter(author=request.user.id).order_by('-create_date')
    num = 10
    paginator = Paginator(review_list, num)
    review_list = paginator.page(page)
    start_index = 1
    for i in reversed(range(1, page + 1)):
        if i % num == 1:
            start_index = i
            break

    max_index = len(paginator.page_range)
    end_index = start_index + num
    if end_index >= max_index:
        end_index = max_index

    page_range = range(start_index, end_index)

    return render(request, 'account/review.html', {'review_list': review_list, 'page_range': page_range})


@login_required(login_url='account:login')
def pick(request):
    page = request.GET.get('page', '1')
    if page == '':
        page = '1'
    page = int(page)
    pick_list = Pick.objects.filter(user=request.user.id).order_by('-pick_date')
    num = 10
    paginator = Paginator(pick_list, num)
    pick_list = paginator.page(page)
    start_index = 1
    for i in reversed(range(1, page + 1)):
        if i % num == 1:
            start_index = i
            break

    max_index = len(paginator.page_range)
    end_index = start_index + num
    if end_index >= max_index:
        end_index = max_index

    if end_index == 1:
        end_index = 2;

    page_range = range(start_index, end_index)

    context = {
        'pick_list': pick_list,
        'page_range': page_range
    }

    return render(request, 'account/pick.html', context)


@login_required(login_url='account:login')
def change_nickname(request, user_id, nickname):
    pass