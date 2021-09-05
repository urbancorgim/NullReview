from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from community.models import Board
from django.urls import reverse
from django.utils import timezone
from community.forms import BoardForm
from community.models import *
from django.db.models import Q, Count
from django.views import generic
from django.contrib.auth.decorators import login_required



class IndexView(generic.ListView):
    model = Board
    paginate_by = 10
    template_name = 'community/board_list.html'
    context_object_name = 'board_list'

    def get_queryset(self):
        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        board_list = Board.objects.order_by('-created_date')

        if search_keyword:
            if len(search_keyword) > 1:
                if search_type == 'all':
                    search_board_list = board_list.filter(
                        Q(title__icontains=search_keyword) | Q(content__icontains=search_keyword) | Q(
                            writer__nickname__icontains=search_keyword))
                elif search_type == 'content_type':
                    search_board_list = board_list.filter(content_type__icontains=search_keyword)
                elif search_type == 'title':
                    search_board_list = board_list.filter(title__icontains=search_keyword)
                elif search_type == 'content':
                    search_board_list = board_list.filter(content__icontains=search_keyword)
                elif search_type == 'writer':
                    search_board_list = board_list.filter(writer__nickname__icontains=search_keyword)

                if not search_board_list :
                     messages.error(self.request, '일치하는 검색 결과가 없습니다.')
                return search_board_list
            else:
                messages.error(self.request, '검색어는 2글자 이상 입력해주세요.')
        return board_list

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        paginator = context['paginator']
        page_numbers_range = 10
        max_index = len(paginator.page_range)

        page = self.request.GET.get('page')
        current_page = int(page) if page else 1

        start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
        end_index = start_index + page_numbers_range
        if end_index >= max_index:
            end_index = max_index

        page_range = paginator.page_range[start_index:end_index]
        context['page_range'] = page_range

        search_keyword = self.request.GET.get('q', '')
        search_type = self.request.GET.get('type', '')
        #board_fixed = Board.objects.filter(top_fixed=True).order_by('-created_date')

        if len(search_keyword) > 1:
            context['q'] = search_keyword
        context['type'] = search_type
        #context['board_fixed'] = board_fixed
        return context



# 글 작성
@login_required(login_url='account:login')
def board_post(request):
    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            board = form.save(commit=False)
            board.writer_id = request.user.id
            board.created_date = timezone.now()
            board.save()
            return redirect('community:index')
    else:
        form = BoardForm()
    context = {'form': form}
    return render(request, 'community/board_form.html', context)

# 글 상세보기
def board_detail(request, post_id):
    boardPerPage = Board.objects.order_by('-created_date')

    index = -1
    board_before = None
    board_after = None

    for b in boardPerPage:
        index += 1
        if b.id == post_id:
            board = b
            break
    if index > 0:
        board_before = boardPerPage[index - 1]
    if index < len(boardPerPage)-1:
        board_after = boardPerPage[index + 1]

    context = {
        'board':board,
        'board_after':board_after,
        'board_before':board_before,
    }
    return render(request, 'community/board_detail.html', context)


# 글 삭제
@login_required(login_url='account:login')
def board_delete(request, post_id):
    board = Board.objects.get(id=post_id)
    board.delete()
    messages.success(request, "삭제되었습니다.")
    return redirect('community:index')


# 글 수정
@login_required(login_url='account:login')
def board_modify(request, post_id):
    board = get_object_or_404(Board, id=post_id)

    if request.method == "POST":
        form = BoardForm(request.POST,  request.FILES, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.modified_date = timezone.now()
            board.save()
            return redirect('community:detail', post_id=post_id)
    else:
        form = BoardForm(instance=board)
    context = {'form': form}
    return render(request, 'community/board_modify.html', context)

# Create your views here.
# 글 목록
# def index(request):
#     # boards = {'boards': Board.objects.order_by('-created_date')}
#     # return render(request, 'community/board_list.html', boards)
#
#     page = request.GET.get('page', '1')
#     # 조회
#     board_list = Board.objects.order_by('-created_date')
#
#     # 페이징처리
#     paginator = Paginator(board_list, 10)  # 페이지당 10개씩 보여주기
#     page_obj = paginator.get_page(page)
#     context = {'board_list': page_obj,}
#     return render(request, 'community/board_list.html', context)
# class IndexView(generic.ListView):
#     paginate_by = 10
#
#     def get_context_data(self, **kwargs):
#         context = super(IndexView, self).get_context_data(**kwargs)
#         paginator = context['paginator']
#         page_numbers_range = 10
#         max_index = len(paginator.page_range)
#
#         page = self.request.GET.get('page')
#         current_page = int(page) if page else 1
#
#         start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range
#         end_index = start_index + page_numbers_range
#         if end_index >= max_index:
#             end_index = max_index
#
#         page_range = paginator.page_range[start_index:end_index]
#         context['page_range'] = page_range
#         return context
#
#     def get_queryset(self):
#         return Board.objects.order_by("-created_date")
