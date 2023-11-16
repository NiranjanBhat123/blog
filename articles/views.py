# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
def article_list(request):
    articles = Article.objects.all()
    context = {'articles':articles}
    return render(request,'articles/article_list.html',context)





