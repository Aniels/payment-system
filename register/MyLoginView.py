from django.shortcuts import render
from django.contrib.auth.views import LoginView


class MyLoginView(LoginView):
    template_name = 'authenticate/login.html'

    def form_valid(self, form):
        # Perform the login
        print('valid correct')
        username = form.cleaned_data['username']
        self.request.session['username'] = username
        return render(self.request, 'authenticate/profile.html')
