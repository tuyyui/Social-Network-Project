from django.shortcuts import render
from django.http import HttpResponse
from .forms import SnippetForm
from django.contrib.auth.forms import UserCreationForm
from django.template.loader import render_to_string



# Create your views here.



#def snippet_detail(request):
   # if request.method == 'POST':
    #    form = SnippetForm(request.POST)
     #   if form.is_valid():
      #      form.save()
    #form = SnippetForm()
    #return render(request, 'form.html', context={'form': form})


