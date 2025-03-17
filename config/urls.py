from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),  # Admin interface URLs
    path("", include("apps.core.urls")),  # Your main app URLs
    path("accounts/", include("apps.accounts.urls", namespace="accounts")),
    path("marketplace/", include("apps.marketplace.urls", namespace="marketplace")),
    path("shop/", include("apps.shop.urls", namespace="shop")),
    path("blog/", include("apps.blog.urls", namespace="blog")),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)