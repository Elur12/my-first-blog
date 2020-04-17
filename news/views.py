from django.shortcuts import render
from django.utils import timezone
from .models import Post, Town, zakaz
from django.shortcuts import redirect
from .forms import TownForm, ZakazForm

def post_list(request):
    posts = Post.objects.order_by('-published_date')
    return render(request, 'news/post_list.html', {'posts': posts[0]})
def newbox(request):
    if request.method == "POST":
        form = TownForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            town = Town.objects.order_by('-id')
            print(town)
            return render(request, 'news/id_Town.html', {'town': town[0]})
    else:
        form = TownForm()
    return render(request, 'news/newbox.html', {'form': form})
def news(request):
    posts = Post.objects.order_by('-published_date')
    print(posts)
    return render(request, 'news/news.html', {'posts': posts})
def newzakaz(request):
    if request.method == "POST":
        form = ZakazForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            town = zakaz.objects.order_by('-id')
            return render(request, 'news/cod_otsl.html', {'town': town[0]})
    else:
        form = ZakazForm()
    return render(request, 'news/newzakaz.html', {'form': form})
