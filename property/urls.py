
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rent import views


admin.site.site_header = "Veritas"
admin.site.site_title = "Veritas Admin Portal"
admin.site.index_title = "Welcome to Veritas Portal"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.backend, name='backend'),
    path('login/', include('django.contrib.auth.urls')),
    path('rent_roll/', views.rent_roll, name='rent_roll'),
    path('add_rent/', views.add_rent, name='add_rent'),
    path('property_info/', views.property_info, name='property_info'),
    path('property_info_roll/', views.property_info_roll, name='property_info_roll'),
    path('financials/', views.financials, name='financials'),
    path('add_income/', views.add_income, name='add_income'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('update_rent/', views.update_rent, name='update_rent'),
    path('delete_rent/', views.delete_rent, name='delete_rent'),
    path('clyentel/', views.builder, name='builder'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


