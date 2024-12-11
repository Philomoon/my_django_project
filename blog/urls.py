from django.urls import path
from . import views

# URLパターンをサカ引きできるように名前をつける
app_name = 'blog'

# URLを登録するための変数

urlpatterns = [
    # リクエストされたURLのページへのフルパス部分が’’（無し）にマッチングした場合
    # ViewsモジュールのIndexViewクラスをインスタンス化する
    path('',views.IndexView.as_view(),name='index'),

    # リクエストされたURLが「blog-detail/レコードのid」の場合は
    # BlogDetailを実行
    path(#詳細ページのURLは「blog-detail/レコードのid/」
        'blog-detail/<int:pk>/',
        #viewsモジュールのBlogDetailを実行
        views.BlogDetail.as_view(),
        # URLパターンの名前を’blog_detail'にする
        name='blog_detail'
        ),


]