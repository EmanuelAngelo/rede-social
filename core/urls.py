from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('', lambda request: redirect('account/login/', permanent=True)), #redireciona para a página de login
]
