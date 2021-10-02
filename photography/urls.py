from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('update', views.update, name='update'),
    path('nupdate/<str:pk>', views.nupdate, name='nupdate'),
    path('main', views.main, name='main'),
    path('main/<str:pk>', views.mainvisit, name='mainvisit'),
    path("new", views.new, name='new'),
    path('edit', views.edit, name='edit'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('dashboardvisit/<str:pk>', views.dashboardvisit, name='dashboardvisit'),

]
