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

    # scienceカテゴリの一覧ページのURLパターン
    path(
        # sicenceカテゴリの一覧ページのURLは「science-list」
        'science-list/',
        # viewsモジュールのScienceViewを実行
        views.ScienceView.as_view(),
        # URLパターンの名前を'science_list'にする
        name='science_list'
    ),

    # dailylifeカテゴリの一覧ページのURLパターン
    path(
        # dailylifeカテゴリの一覧ページのURLは「dailylife-list」
        'dailulife-list/',
        # viewsモジュールのDailylifeViewを実行
        views.DailylifeView.as_view(),
        # URLパターンの名前を'dailylife_list'にする
        name='dailylife_list'
    ),

    # musicカテゴリの一覧ページのURLパターン
    path(
        # musicカテゴリの一覧ページのURLは「music-list」
        'music_list',
        # viewsモジュールのMusicViewを実行
        views.MusicView.as_view(),
        # URLパターンの名前を'music_list'にする
        name='music_list'
    ),

]