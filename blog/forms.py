#Este es el formulario donde se crean los posts sin tener que entrar al panel de administracion
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post 	#manda llamar al modelo post
        fields = ('title', 'text',)  #manda llamar los atributos de titulo y texto del modelo post