from django.contrib import admin
from django.urls import path, include
# qoshilgan
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap
from blog_app.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}


urlpatterns = [
    path("admin/", admin.site.urls),
    path('blog/', include('blog_app.urls', namespace='blog_app')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)