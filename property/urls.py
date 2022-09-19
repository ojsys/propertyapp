
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
    path('<int:rent_id>/', views.detail_rent, name='detail_rent'),
    path('<int:rent_id>/update/', views.update_rent, name='update_rent'),
    path('<int:rent_id>/delete/', views.delete_rent, name='delete_rent'),
    path('owner1/', views.owner_one, name='owner1'),
    path('owner2/', views.owner_two, name='owner2'),
    path('owner3/', views.owner_three, name='owner3'),
    path('owner4/', views.owner_four, name='owner4'),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


