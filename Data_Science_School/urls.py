from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from accounts.views import ContactView, CoursesView, HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('accounts.urls')),
    
    #site pages
    path ('',HomeView.as_view(template_name='home.html'),name='home'),
    path ('about/',TemplateView.as_view(template_name='about.html'),name='about'),
    path ('privacy-policy/',TemplateView.as_view(template_name='privacy_policy.html'),name='policy'),
    path ('terms/',TemplateView.as_view(template_name='terms.html'),name='terms'),
    path ('courses/',CoursesView.as_view(template_name='courses.html'),name='courses'),
    path ('contact/',ContactView.as_view(),name='contact'),
]
