"""rechstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('index.urls')),
    path('account/',include('account.urls')),
    path('home/',include('home.urls')),
    path('new_entry/',include('new_entry.urls')),
    path('balance_record/',include('balance_record.urls')),
    path('all_transactions/',include('all_transactions.urls')),
    path('manage_ac/',include('manage_ac.urls')),
    path('unique_numbers_id/',include('unique_numbers_id.urls')),
    path('transactions/',include('transactions.urls')),
    path('account_profile/',include('account_profile.urls')),
    path('error_404/',include('error_404.urls')),
    path('forgate/',include('forgate.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
