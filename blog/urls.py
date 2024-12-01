from django.urls import path
from . import views

# URLパターンをサカ引きできるように名前をつける
app_name = 'blog'

# URLを登録するための変数
# リクエストされたURLのページへのフルパス部分が’’（無し）にマッチングした場合
# ViewsモジュールのIndexViewクラスをインスタンス化する
urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
]