from django.urls import path
from . import views

# URLパターンをサカ引きできるように名前をつける
app_name = 'photo'

# URLパターンを登録するための変数
# photoアプリへのアクセスはviewsモジュールのIndexViewにリダイレクトする
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]

