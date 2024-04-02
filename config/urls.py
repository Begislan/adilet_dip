from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("core.urls")),
    path('python/', include("python.urls")),
    path('java/', include("java.urls")),
    path('cisharp/', include("cisharp.urls")),
    path('javascript/', include("javascript.urls")),
    path('kotlin/', include("kotlin.urls")),
    path('html/', include("HTML.urls")),
    path('css/', include("CSS.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
