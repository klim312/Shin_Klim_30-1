"""
URL configuration for hw project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from products.views import main_view, products_view, products_detail_view, category_view
from user.views import register_view, login_view, logout
from django.conf.urls.static import static
from hw import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_view),
    path('products/', products_view),
    path('category/', category_view),
    path('products/<int:id>/', products_detail_view),
    path('user/register/', register_view),
    path('user/login/', login_view),
    path('user/logout/', logout),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
