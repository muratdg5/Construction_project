from django.shortcuts import render
from .models import  AltServices,Services,Card,AboutSection,Testimonials,HeroSection,OurProjects,OurProjectsCategory

# Create your views here.

def home(request):

    context={
        'testimonials':Testimonials.objects.all(),
        'herosection':HeroSection.objects.all(),
        'card':Card.objects.filter(is_active=True),
        'services':Services.objects.filter(is_active=True),
        'altservices':AltServices.objects.all(),
        'ourprojectscategory':OurProjectsCategory.objects.all(),
        'ourprojects':OurProjects.objects.all(),
        #sadece ikince veri is activi true
        
    }
    return render(request,'partials/index.html',context)


def about_us(request):
    breadcrumbs='about'
    context={
        'breadcrumbs':breadcrumbs,
        'aboutsection':AboutSection.objects.all(),
        'testimonials':Testimonials.objects.all(),
    }
        
    
    return render(request,'partials/about.html',context)

def  contact_us(request):
    breadcrumbs='contact'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/contact.html',context)

def  blog(request):
    breadcrumbs='blog'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/blog.html',context)


def  blog_details(request):
    context=dict()
    return render(request,'partials/blog-details.html',context)



def  project(request):
    breadcrumbs='project'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/projects.html',context)



def  project_details(request):
    context=dict()
    return render(request,'partials/project-details',context)


def page(request):
    breadcrumbs='Sample Inner Page'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/sample-inner-page.html',context)


def services(request):
    breadcrumbs='services'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/services.html',context)

def  service_details(request):
    breadcrumbs='service details'
    context={
        'breadcrumbs':breadcrumbs,
    }
    return render(request,'partials/service-details.html',context)







