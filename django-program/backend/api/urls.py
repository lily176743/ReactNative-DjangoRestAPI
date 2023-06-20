from django.urls import path
from api import views

urlpatterns = [
    path('', views.NoteList.as_view()),
    path('<int:pk>/', views.NoteDetail.as_view()),

    path('faq/', views.FaqList.as_view()),
    path('faq/<int:pk>/', views.FaqDetail.as_view()),
]