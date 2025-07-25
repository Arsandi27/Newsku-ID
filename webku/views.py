from django.shortcuts import redirect, render
from . models import Category, News
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
        else:
            messages.error(request, 'Terjadi kesalahan dalam formulir registrasi. Silakan periksa kembali input Anda.')
    else:
        form = RegisterForm()
    return render(request, 'registration/registrasi.html', {'form': form})
    
def index_login(request):
    request.session.clear()
    logout(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Login gagal. Silakan periksa kembali username dan password Anda.')
        else:
            messages.error(request, 'Username tidak ditemukan.')

    return render(request, 'registration/login.html')

def logout(request):
    if request.method == 'POST':
        request.session.clear()
        return redirect('login')

@login_required(login_url = 'login')
def home(request):
    first_news = News.objects.all()[:3]
    other_news= News.objects.all()[3:]
    categories = Category.objects.all()
    return render(request,'tampilan/home.html',{
        'first_news' : first_news,
        'other_news' : other_news,
        'categories' : categories,
    })

def detail_news(request, news_id):
    news= get_object_or_404(News, pk=news_id)
    related_news = news.get_related_news()
    return render(request, 'tampilan/detail_berita.html', {
        'news': news,
        'related_news' : related_news,
        })


def search(request):
    query = request.GET.get('q')
    results = News.objects.all()
    print(query)
    if query:
        results = results.filter(title__icontains=query)
        print(results)

    return render(request, 'tampilan/search_results.html', {'results': results, 'query': query})



def news_page(request):
    news_list = News.objects.all()
    return render(request, 'tampilan/news_page.html', {'news_list': news_list})


def all_categories(request):
    categories= Category.objects.all()
    return render(request, 'tampilan/all_categories.html', {'categories': categories})


def category_news(request, category_name):
    list_category = News.objects.filter(category__name=category_name)
    return render(request, 'tampilan/category_news.html', {'list_category': list_category, 'category_name': category_name})









