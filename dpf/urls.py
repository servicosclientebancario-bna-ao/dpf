from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

from dados import views

urlpatterns = [
    path('abubacar-1930.@/', admin.site.urls),  # URL para o Django admin
    path('validadorDocumento/validarDocumento/', views.validar_documento, name='validarDocumento'),  # URL para a view validar_documento
    path('validadorDocumento/dadosDocumento/', views.dados_documento, name='dadosDocumento'),  # URL para a view dados_documento
]

# Redirecionar todas as outras URLs para 'validadorDocumento/validarDocumento/'
urlpatterns += [
    re_path(r'^.*$', RedirectView.as_view(url='/validadorDocumento/validarDocumento/', permanent=False)),
]

# Servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
