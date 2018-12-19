from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

#forms is used for taking input from the site visitors
#In a similar way that a model class’s fields map to database fields, a form class’s fields map to HTML form <input> elements.


#When rendering an object in Django, we generally:

# get hold of it in the view (fetch it from the database, for example)
# pass it to the template context
# expand it to HTML markup using template variables


def register(request):
    if request.method == 'POST': #if the form has been submitted
           form = UserRegisterForm(request.POST) #this is the form which has the request.POST data
           if form.is_valid():
               form.save()
               username = form.cleaned_data.get('username') #formdaki data bir dictionary'ye aktarılıyor. bu cleaned_data ile ona erişiyoruz.
               #username key'ini dictionaryden çektik şimdi. cleaned_data will always only contain a key for fields defined in the Form,
               #even if you pass extra data when you define the Form.
               #When the Form is valid, cleaned_data will include a key and value for all its fields, even if the data didn’t include a
               #value for some optional fields.
               messages.success(request, 'Your account has been created. You can Log In from here.')
               return redirect('login')
    else:
           form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form}) #passing it to the template, what is form dictionary?

@login_required #decorators adds funcitonality to a existing function
def profile(request):
    return render(request, 'users/profile.html')
