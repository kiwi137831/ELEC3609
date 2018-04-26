from django.shortcuts import render, render_to_response, redirect
from .forms import LoginForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required

#after login, store all information in session for further use
@login_required
def dashboard(request):
    request.session['user_id']= request.user.id
    request.session['user_university'] = request.user.university
    request.session['user_nickname'] = request.user.nick_name
    request.session['user_status'] = request.user.status
    request.session['is_login'] = "true"
    return redirect('http://127.0.0.1:8000/homepage/'+ str(request.user.id))


#this is function that user will call for registration
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request,
                          'account/register_done.html',
                          {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'account/register.html',
                  {'user_form': user_form})
