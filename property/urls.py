
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
    path('<int:income_id>/update_income/', views.update_income, name='update_income'),
    path('<int:income_id>/delete_income/', views.delete_income, name='delete_income'),
    path('<int:expense_id>/update_expense/', views.update_expense, name='update_expense'),
    path('<int:expense_id>/delete_expense/', views.delete_expense, name='delete_expense'),
    path('<int:owner_id>/owner/', views.owner_view, name='owner'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


