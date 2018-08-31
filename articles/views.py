from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import articles_News, articles_Analyse, articles_Tutorial

# Create your views here.
def articles_list(request):
    articleAnalyse = articles_Analyse.objects.all().order_by('-date')
    articleNews = articles_News.objects.all().order_by('-date')
    articleTutorial = articles_Tutorial.objects.all().order_by('-date')
    
    paginator = Paginator(articleAnalyse,17)
    page = request.GET.get('page')
    try:
        articleAnalyse = paginator.page(page)
    except PageNotAnInteger:
        articleAnalyse = paginator.page(1)
    except EmptyPage:
        articleAnalyse = paginator.page(paginator.num_pages)



    paginator = Paginator(articleTutorial,17)
    page = request.GET.get('page')
    try:
        articleTutorial = paginator.page(page)
    except PageNotAnInteger:
        articleTutorial = paginator.page(1)
    except EmptyPage:
        articleTutorial = paginator.page(paginator.num_pages)


    paginator = Paginator(articleNews,17)
    page = request.GET.get('page')
    try:
        articleNews = paginator.page(page)
    except PageNotAnInteger:
        articleNews = paginator.page(1)
    except EmptyPage:
       articleNews = paginator.page(paginator.num_pages)


    

  
  
    return render(request, 'articles_list.html', {'articleA':articleAnalyse,'articleN':articleNews,'articleT':articleTutorial })

def articles_details_N(request, slug):
    articleN = get_object_or_404(articles_News, slug=slug)
    return render(request, 'articles_details.N.html',{'articleN':articleN})



def articles_details_A(request, slug):
    articleA = get_object_or_404(articles_Analyse, slug=slug)
    return render(request, 'articles_details.A.html',{'articleA':articleA})

def articles_details_T(request, slug):
    articleT = get_object_or_404(articles_Tutorial, slug=slug)
    return render(request, 'articles_details.T.html',{'articleT':articleT})