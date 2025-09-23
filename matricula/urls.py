"""
URL configuration for matricula project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from alunos import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.listar_alunos, name='listar_alunos'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'), 
    path('<int:id>/detalhar/', views.detalhar_aluno, name='detalhar_aluno'),   
    path('editar/<int:id>/', views.editar_aluno, name='editar_aluno'),
    path('excluir/<int:id>/', views.excluir_aluno, name='excluir_aluno'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
