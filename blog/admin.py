from django.contrib import admin
from .models import  AltServices,Services,Testimonials,AboutSection,HeroSection,Card,OurProjects,OurProjectsCategory
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
        list_display=('name',)
        search_fields=('name','description',)

admin.site.register(Testimonials,BlogAdmin)

admin.site.register(AboutSection)
admin.site.register(HeroSection)
admin.site.register(Card)
admin.site.register(Services)
admin.site.register(AltServices)
admin.site.register(OurProjects)
admin.site.register(OurProjectsCategory)