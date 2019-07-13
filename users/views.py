from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import UserRegisterForm

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('login')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return HttpResponseRedirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

#
# @app.route("/registration", methods = ['GET','POST'])
# def registration():
#
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     form = RegistrationForm()
#
#     if form.validate_on_submit():
#         hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
#         db.session.execute("INSERT INTO users(username, email, password) VALUES (:username, :email, :password)",
#         {"username":form.username.data, "email":form.email.data, "password":hashed_password})
#         flash(f"Account has been created", "success")
#         db.session.commit()
#         return redirect(url_for("login"))
#
#     return render_template('registration.html', form = form, title = "Registration")
#
#
# @app.route("/login", methods = ['GET','POST'])
# def login():
#     if current_user.is_authenticated:
#         return redirect(url_for('index'))
#
#     form = LoginForm()
#
#     if form.validate_on_submit():
#         user_data = db.session.execute("SELECT * FROM users where username = :username", {"username": form.username.data}).fetchone()
#         if user_data and bcrypt.check_password_hash(user_data.password, form.password.data):
#             login_user(User(user_data.id), remember = form.remember.data)
#             return redirect(url_for('index'))
#
#         flash('Login failed try again', 'warning')
#
#     return render_template('login.html', form = form)
#
#
# @app.route("/logout", methods = ['GET'])
# def logout():
#     logout_user()
#     return redirect(url_for('login'))
