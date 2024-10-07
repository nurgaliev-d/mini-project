from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin 
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('users/', include('users.urls')),
    path('home/', views.home, name='home'),  # Home page URL
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
