from django.urls import path, include, re_path
from .views import home_view, search_words, WordListAPIView
# from django.contrib.auth.views import LoginView

urlpatterns = [
    re_path(r'^api/search', WordListAPIView.as_view(), name='search_api'),
    # re_path(r'^words/get/(?P<pk>\w+)/$', word_detail , name='word_detail'),
    re_path(r'^searchbar/$', search_words, name='search_words'),
    re_path(r'^$', home_view, name='home')
]