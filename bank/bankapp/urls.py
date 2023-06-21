from django.urls import path

from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('kyc', views.index, name='index'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('kyc',views.kyc,name='kyc'),
    path('logout', views.logout, name='logout'),
    # path('dropdown', views.index, name='index'),
    path('dropdown', views.kyc, name='kyc'),
    path('fetch-state', views.fetch_state, name='fetch_state'),
    # path('fetch-city', views.fetch_city, name='fetch_city'),
    # path('add/', views.person_create_view, name='person_add'),
    # # path('<int:pk>/', views.person_update_view, name='person_change'),
    # path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),

]