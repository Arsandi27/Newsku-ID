from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from.import views
from .views import all_categories, category_news, index_login, logout, news_page, search, register,home

urlpatterns = (
    [
    path('', home, name='home'),
    path('login/', index_login, name='login'),
    path('logout-account/', logout, name='logout_account'),
    path('news/<int:news_id>/', views.detail_news, name='detail_news'),
    path('search/', search, name='search'),
    path('register/', register, name='register'),   
    path('news/', news_page, name='news_page'),
    path('categories/', all_categories, name='all_categories'),
    path('categories/<str:category_name>/', category_news, name='category_news'),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
)