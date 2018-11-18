from django.contrib import admin
from django.urls import path
from house import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('firstpage/', views.firstpage, name='firstpage'),
    path('signup/', views.signup, name='signup'),
    path('allp/', views.allp, name='allp'),
    path('login/', views.signin, name='signin'),
    path('home/', views.home, name='home'),
    path('logout/', views.signout, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/',views.contact,name='contact'),
    path('faq/',views.faq,name='faq'),
    path('owner_site/',views.owner,name='owner_site'),
    path('owner_site/add_property/',views.add_property,name='add_property'),
    path('owner_site/add_tenant/',views.add_tenant,name='add_tenant'),
    path('tenant_site/',views.tenant,name='tenant_site'),
    path('owner_site/property_details/',views.property_details,name='property_details'),
    path('owner_site/tenant_details/',views.tenant_details,name='tenant_details'),
    path('owner_site/invite/',views.invite,name='invite'),
    path('owner_site/edit_profile/',views.edit_profile,name='edit_profile'),
    path('tenant_site/edit_profile_tenant/',views.edit_profile_tenant,name='edit_profile_tenant'), 
    path('owner_site/del_property/',views.del_prop,name='del_prop'),  
    path('remind_tenant/',views.rent_reminder,name='rent_reminder'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)