from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^category_search$', 'entity.views.category_search', name='category_search'),
    url(r'^category/(?P<id>\d+)/$', 'entity.views.category_wise', name="category_wise"),
    url(r'^(?P<id>\d+)/$', 'entity.views.entity_full', name="entity_full"),
]
