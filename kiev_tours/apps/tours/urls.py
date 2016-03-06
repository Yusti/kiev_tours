from django.conf.urls import url

from . import views

app_name = 'tours'
urlpatterns = [
    # ex: /polls/
    url(r'^tours/$', views.toursList, name='tours-list'),
    #url(r'^$', views.IndexView.as_view()),
    # # ex: /polls/5/
    url(r'^tours/(?P<tour_id>[0-9]+)/$', views.toursDetail, name='tours-detail'),
    # url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # # ex: /polls/5/results/
    # # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
