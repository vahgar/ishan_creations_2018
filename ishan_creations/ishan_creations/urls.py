from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Examples:
    url(r'^$', 'index.views.index', name='homepage'),
    url(r'^icbc$', 'index.views.icbc', name='icbc'),
    url(r'^categories$', 'entity.views.list_city', name='categories'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^entity/', include('entity.urls', namespace='entity')),

]
if settings:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
