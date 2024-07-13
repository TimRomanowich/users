from django.shortcuts import render, redirect 
from django.contrib import messages
from django.views import View

from .forms import RegisterForm

def home(request):
    return render(request, 'users/home.html')

"""
IF request is GET, create new instance of empty form
If request if POST, create new instance of form with POST data
   Then check if form is valid by calling form.is_valid()
   If form is valid, process clean form data save to database
"""
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'users/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            "Notify user if account creation succesful"
            messages.success(request, f'Account created for {username}')

            return redirect(to='/')

        return render(request, self.template_name, {'form': form})
