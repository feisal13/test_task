from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from .models import News
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

def index(request):
    return render(request, 'news/home_page.html')

def detail(request, news_id):
    try:
        a = News.objects.get(id = news_id)
    except:
        raise Http404('Not found')

    comments = a.comment_set.order_by('-id')[:10]
    # a.comment_set.create(author_name="", comment_text = request.POST['text'], pub_date = timezone.now)
    return render(request, 'news/post.html', {'news': a, 'comments': comments})

def leave_comment(request, news_id):
    try:
        a = News.objects.get(id = news_id)
    except:
        raise Http404('Not found')

    a.comment_set.create(author_name=request.user, comment_text = request.POST['text'], pub_date = timezone.now())
    return HttpResponseRedirect(reverse('detail', args=(a.id,)))
#
# class Register(FormView):
#     form_class = UserCreationForm
#     success_url = 'register/'
#     template_name = 'mysite/register.html'
#
#     def form_valid(self, form):
#         form.save()
#         return super(Register, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return super(Register, self).form_invalid(form)