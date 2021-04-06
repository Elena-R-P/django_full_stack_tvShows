from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('shows', views.shows),
    path('shows/new', views.shows_new),
    path('shows/create_new', views.create_new),
    path('shows/details_page/<int:show_id>', views.details_page),
    path('shows/edit_page/<int:show_id>', views.edit_page),
    path('update/<int:show_id>', views.update),
    path('shows/delete/<int:show_id>', views.destroy)
]