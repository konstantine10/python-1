from django.urls import path

from book import views

urlpatterns=[
    path('',views.SelectBooksView.as_view(),name="selectbooks"),
    path('add',views.AddBookView.as_view,name="addbook")

]