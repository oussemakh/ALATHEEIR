from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import articles_list, articles_details_A,articles_details_N,articles_details_T

urlpatterns = [
    url(r'^$', articles_list, name="articles-list"),
    url(r'^one(?P<slug>[\w-]+)/$',articles_details_A, name="articles-details-A"),
    url(r'^two(?P<slug>[\w-]+)/$',articles_details_N, name="articles-details-N"),
    url(r'^three(?P<slug>[\w-]+)/$',articles_details_T, name="articles-details-T"),
]
