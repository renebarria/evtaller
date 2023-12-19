from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('productos/', views.lista_productos, name='lista_productos'),
    path('agregar/', views.agregar_productos, name='agregar_productos'),
    path('carro/', views.carroneitor, name='carroneitor'),
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),
    path('producto/<int:pk>/', views.producto_detalle, name='producto_detalle'),
    path('agregar_al_carro/<int:product_id>/', views.agregar_al_carro, name='agregar_al_carro'),
    path('eliminar/<int:product_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('editar/<int:product_id>/', views.editar_producto, name='editar_producto'),
    path('reseñas/', views.reseñas, name='reseñas'),
    path('agregar_resena/<int:product_id>/', views.agregar_resena, name='agregar_resena'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    
    
    path('register/', register, name='register'),
    

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)