from django.urls import path, include
from . import views

app_name = 'shop'
urlpatterns = [
	path('', views.product_list, name='product_list'),
	path('high/', views.high_to_low, name='high_to_low'),
	path('low/', views.low_to_high, name='low_to_high'),
	path('new/', views.new_to_old, name='new_to_old'),
	path('old/', views.old_to_new, name='old_to_new'),
	path('specials/', views.product_specials, name='specials'),
	path('search/', include('haystack.urls')),
	path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
	path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
]
