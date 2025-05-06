from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import SignUpForm, LoginForm


def home(request):
    return render(request, 'main/layout.html')


def about(request):
    return render(request, 'main/about.html')


def code(request):
    categories = ["cat1", "cat2", "cat3", "cat4", "cat5", "cat6", "cat7", "cat8"]
    return render(request, 'main/code.html', {'categories': categories})


def courses(request):
    courses = [
        {
            'image': 'course-1.jpg',
            'title': 'HTML Course for Beginners',
            'rating': '4.5',
            'learners': '83.5k+ learners',
            'duration': '2.0 Hrs',
        },
        {
            'image': 'course-2.jpg',
            'title': 'CSS Complete Guide',
            'rating': '4.6',
            'learners': '65.2k+ learners',
            'duration': '3.5 Hrs',
        },
        {
            'image': 'course-3.jpg',
            'title': 'JavaScript Essentials',
            'rating': '4.7',
            'learners': '92.3k+ learners',
            'duration': '4.0 Hrs',
        },
        {
            'image': 'course-4.jpg',
            'title': 'Python for Data Science',
            'rating': '4.8',
            'learners': '120k+ learners',
            'duration': '5.5 Hrs',
        },
        # Add more courses as needed
    ]
    return render(request, 'main/courses.html', {'courses': courses})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Account created successfully! You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, 'Login successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid email or password')
    else:
        form = LoginForm()
    return render(request, 'main/login.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('login')
