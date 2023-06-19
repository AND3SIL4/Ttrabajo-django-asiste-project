from django.urls import path
from . import views

urlpatterns = [
  path('', views.landing, name='landing'),
  path('home/', views.home, name='home'),
  path('logout/', views.logout_user, name='logout'),
  path('register/', views.register_user, name='register'),
  path('record/<int:pk>', views.aprendiz_view, name='aprendiz'),
  path('delete_record/<int:pk>', views.delete_record, name='delete_record'),
  path('add_record', views.add_record, name='add_record'),
  path('update_record/<int:pk>', views.update_record, name='update_record'),
  path('olvido_pass/', views.olvido_pass, name='olvido_pass'),
]
