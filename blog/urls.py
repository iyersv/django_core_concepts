from django.urls import path

import blog.views as views

urlpatterns = [
    path('',views.post_model_list_view,name='list'),
    path('<int:pk>/',views.post_model_detail_view,name='detail'),
    path('create/',views.post_model_create_view,name='create'),
    path('update/<int:pk>/',views.post_model_update_view,name='update'),
    path('delete/<int:pk>/', views.post_model_delete_view, name='delete'),

]
