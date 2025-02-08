from django.shortcuts import render

# django.views.generic から import TemplateViewをインポート
from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー
    '''
    # index.htmlをレンダリングする
    template_name = 'index.html'
    