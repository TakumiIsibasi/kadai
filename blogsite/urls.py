from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user.urls')),
    path('mail/', include('mail.urls')),
    path('post_list/', include('post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
