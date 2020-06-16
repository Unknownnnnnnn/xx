import xadmin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path,include
from werobot.contrib.django import make_view
from . import views


urlpatterns = [
    path('admin/', xadmin.site.urls, name="admin"),
    path('', include('apps.blog.urls')),
    path('search/', include('haystack.urls')),
    path('mdeditor/', include('mdeditor.urls')),
    path('comment/', include('apps.comment.urls')),
    path('', include('apps.notice.urls')),
    path('', include('apps.myzone.urls')),
    path('notifications/', include('notifications.urls', namespace='notifications')),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # import debug_toolbar
    # urlpatterns.append(path('__debug__/', include(debug_toolbar.urls)))
