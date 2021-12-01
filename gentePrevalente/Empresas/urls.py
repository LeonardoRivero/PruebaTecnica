from django.urls import path, include
from .views import EmpresaDetail, EmpresaList,ArchivosEmpresaList,ArchivosEmpresaDetail
from . import views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
template_patterns = [
    path('', TemplateView.as_view(template_name="index.html"), name='index'),
    path('aprob_empresas/', TemplateView.as_view(template_name="aprobacion_empresas.html"), name='aprob_empresas'),
    path('agregar_empresa/', TemplateView.as_view(template_name="agregar_empresa.html"), name='agreg_empresa'),
    
    # path('camera/list/', TemplateView.as_view(template_name="camera_list.html"), name="list"),
    # path('camera/create/', TemplateView.as_view(template_name="camera_create.html")),
    # path('camera/<int:pk>/edit/', TemplateView.as_view(template_name="camera_edit.html")),
    # path('camera/<int:pk>/delete/', TemplateView.as_view(template_name="camera_delete.html")),
]
urlpatterns = [
    path('api/empresa/all/', EmpresaList.as_view()),
    path('api/empresa/<int:pk>/', EmpresaDetail.as_view()),
    path('api/archivos/all/', csrf_exempt(ArchivosEmpresaList.as_view())),
    path('api/archivos/<int:pk>/', csrf_exempt(ArchivosEmpresaDetail.as_view())),
    path('api/estado_empresa/all/', csrf_exempt(ArchivosEmpresaList.as_view())),
    path('', include(template_patterns)),
]
