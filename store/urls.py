from django.urls import include, path

from store import views


urlpatterns = [    
    path('', views.product, name='main'),
    path('contacts', views.contacts, name='contacts'),
    path('catalog', views.catalog, name='catalog'),
    path('login', views.login, name='account_login'),
    path('logout', views.logout, name='account_logout'),
    path('signup', views.signup, name='account_signup')
]