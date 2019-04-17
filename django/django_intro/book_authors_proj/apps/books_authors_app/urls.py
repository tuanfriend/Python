from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^process_book$', views.addbook),
    url(r'^books/(?P<id>[0-9]+)$', views.viewbook),
    url(r'^add_auth', views.addauth),
    url(r'^authors$', views.auth_page),
    url(r'^process_auth', views.addauthor),
    url(r'^authors/(?P<id>[0-9]+)$', views.viewauth),
    url(r'^add_book', views.add_auth_form)
]