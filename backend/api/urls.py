from django.urls import path
from . import views

urlpatterns=[
    path('<int:pk>',views.ProductDetailAPIView.as_view()),
    path('create/',views.ProductCreateAPIView.as_view()),
    path('detail/',views.ProductListAPIView.as_view()),
]