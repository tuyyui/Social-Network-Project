from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, ProfileUpdateForm
from bs4 import BeautifulSoup
from django.contrib.auth.models import User
from .models import Profile
from urllib.request import urlopen
import re


class RelatedUsers:
    def __init__(self, user, sim):
        self.user = user
        self.sim = sim


# Jaccard similarty formula
def jaccard(a, b):
    a = set(a)
    b = set(b)
    return len(a.intersection(b)) / len(a.union(b))


# def user_list(request):
#   users = ProfileUpdateForm(user=request.user)
#  context={
#     'users': users
# }
# return render(request, 'users/profile.html', {'users': users})
# def send_friend_request(request, id):
# if request.user.is_authenticated():
#     user = get_object_or_404(User, id=id)
#     frequest = Connect.objects

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account Created for {username}! You can now login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def scrape_data(ethnic):
    links = []
    html_page = urlopen("https://www.acf.hhs.gov/orr/site_search/" + ethnic, timeout=40000).read()
    soup = BeautifulSoup(html_page)
    for link in soup.findAll('a', attrs={'href': re.compile("^https://")}):
        links.append(link.get('href'))
    return links


@login_required
def profile(request):
    users = Profile.objects.all().order_by("ethnic").reverse()[0:4]
    rusers = []

    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if p_form.is_valid():
            p_form.save()
            messages.success(request, f'You updated your profile!')
            return redirect('profile')
    else:

        p_form = ProfileUpdateForm(instance=request.user.profile)

        if request.user.is_authenticated:
            current_profile = request.user.profile
            for user in users:

                if user != current_profile:
                    # sim = similarity
                    sim = jaccard([current_profile.ethnic, current_profile.family_size],
                                  [user.ethnic, user.family_size])
                    rusers.append(RelatedUsers(user, sim))
                    rusers = sorted(rusers, key=lambda user: user.sim, reverse=True)
            data = {'users': rusers, 'users_count': User.objects.count(), 'useful_links': scrape_data(request.user.profile.ethnic)}


            context = dict(data=data, p_form=p_form)

            return render(request, "users/profile.html", context)
