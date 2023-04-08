from django.urls import path

from . import views
# urlpatterns = [
#     path('',views.home, name='home'),
#     path('about',views.about_us, name='about'),
#     path('contact',views.contact_us, name='contact'), 
# ]

urlpatterns = [
    path('',views.home, name='home'),
    path('about', views.about_us, name='about'),
    path('contact', views.contact_us, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blog_details', views.blog_details, name='blog_details'),
    path('project', views.project, name='project'),
    path('project_details', views.project_details, name='project_details'),
    path('page', views.page, name='page'),
    path('service', views.services, name='service'),
    path('service_details', views.service_details, name='service_details'),
]

