from django.urls import path
from .import views
urlpatterns=[
    path('addauthor',views.addauthor,name = 'addauthor'),
    path('addbooks/',views.addbooks, name ='addbooks'),
    path('author/',views.author,name = 'author'),
    path('books/',views.books,name='books'),
    path('deleteAuthor/<int:pk>',views.deleteAuthor,name ="deleteAuthor"),
    path('deleteBook/<int:pk>',views.deleteBook,name ="deleteBook"),
    path('addgenre/',views.addgenre, name = 'addgenre'),
    path('genre/',views.genre,name='genre'),
    path('',views.home,name='home'),
    path('update/<int:pk>/edit',views.update, name='update'),
]
