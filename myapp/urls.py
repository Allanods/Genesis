
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
   
 path('admin/', admin.site.urls),

path('details/', views.details, name='details'),

path('blog/', views.blog, name='blog'),

path('', views.home, name='home'),

path('portfolio/', views.portfolio, name='portfolio'),

path('services/', views.services, name='services'),

path('starter/', views.starter, name='starter'),

path('show/', views.show, name='show'),

path('delete/<int:id>', views.delete),

path('edit/<int:id>', views.edit),

]
