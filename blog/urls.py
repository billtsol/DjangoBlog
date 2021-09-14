from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler400, handler403, handler404, handler500

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BlogApp.urls')),
]

handler400 = 'BlogApp.views.bad_request'
handler403 = 'BlogApp.views.permission_denied'
handler404 = 'BlogApp.views.page_not_found'
handler500 = 'BlogApp.views.server_error'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)