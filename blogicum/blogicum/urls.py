from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls', namespace='blog')),
    path('pages/', include('pages.urls', namespace='page')),
    path('admin/', admin.site.urls),
]
