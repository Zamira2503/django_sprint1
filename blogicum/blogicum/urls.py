from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('blog.urls')),
    path('posts/<int:id>/', include('blog.urls')),
    path('category/<slug:category_slug>/', include('blog.urls')),
    path('<slug:category_slug>/', include('blog.urls')),
    path('pages/about/', include('pages.urls')),
    path('pages/rules/', include('pages.urls')),
    path('admin/', admin.site.urls),
]
