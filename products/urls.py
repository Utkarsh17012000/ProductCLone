from django.urls import path
from . import views

urlpatterns = [
    path('',views.products_view,name="products"),
    path('create/',views.create_view,name="create"),
    path('<int:product_id>/',views.detail_view,name="detail"),
    path('<int:product_id>/upvote/',views.upvote_view,name="upvote"),
]