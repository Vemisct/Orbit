from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HeartBlock.urls')),
    path('', include('EventsBlock.urls')),
    path('forum/', include('ForumBlock.urls')),
    path('', include('AnnBlock.urls')),
    path('portfolio/', include('PortfolioBlock.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)