from .models import Author, Book ,Genre
from django import forms


class Authorform(forms.ModelForm):
    
    class Meta:
            model = Author
            fields = ["name"]

class Booksform(forms.ModelForm):
    class Meta:
         model = Book
         fields = ["title","author","genre"]
         widget = {
              "genre" : forms.CheckboxSelectMultiple()}
         

class Genreform(forms.ModelForm):
     class Meta:
          model = Genre
          fields = ["name"]
              
         
