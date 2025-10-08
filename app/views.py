# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect , HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse 


import json
import os


from authlib.integrations.django_client import OAuth

# OAuth Configuration
CONF_URL = ''

oauth = OAuth()
oauth.register(
    name='gaussianaccess',
    client_id='gaussianaccessuat',
    client_secret='M1dQaVPY1TIlwNGljyzikEpp130HPo8uE7QyyfvA',
    server_metadata_url='https://sso-uat.iitb.ac.in/.well-known/openid-configuration',
    client_kwargs={'scope': 'openid'}
)

# Home View (Displays User Information)
def login_page(request):
    user = request.session.get('user')
    if user:
        user = json.dumps(user, indent=2)
    return render(request, 'login.html', context={'user': user})

# Login View (Redirects to OAuth Provider)
def login2(request):
    redirect_uri = request.build_absolute_uri(reverse('auth'))  # Set the redirect URI to the auth view
    state = os.urandom(32).hex()
    nonce = os.urandom(32).hex()
    
    # Store state and nonce in session for later validation
    request.session['state'] = state
    request.session['nonce'] = nonce
    
    # Redirect to the authorization page
    return oauth.gaussianaccess.authorize_redirect(request, redirect_uri, state=state, nonce=nonce)

# Authentication Callback View (Handles OAuth Callback)
# Authentication Callback View
def auth(request):
    try:
        token = oauth.gaussianaccess.authorize_access_token(request)
            #newmade
        user_info = token.get('userinfo')
        if user_info:
            request.session['user'] = user_info
            # request.session['user_email'] = user_info['email']
        else:
            return HttpResponse("Failed to fetch user information.", status=400)
    except Exception as e:
        return HttpResponse(f"Authentication error: {e}", status=500)
    
    # Redirect directly to index.html after successful authentication
    
    return redirect('policy')


# Logout View (Logs User Out)
# Logout View (Logs User Out and Clears Session)
def logout2(request):
    # Clear the user session data
    request.session.pop('user', None)
    request.session.pop('state', None)
    request.session.pop('nonce', None)
    
    # Redirect to the index page (or any other page you want after logout)
    return redirect('policy')




##############################################################################################################
def landing_page(request):
     # Page 1
    return render(request, 'landing.html')

# def login_page(request):
#     # Page 2
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         #user = authenticate(request, username=username, password=password)
#         if username=="rohan" and password=="rohan@123":
#             #login(request, user)
#             return redirect('policy')
#         else:
#             messages.error(request, "Invalid username or password")
#     return render(request, 'login.html')



@login_required
def policy_page(request):
    if request.method == "POST":
        # user clicked "I Accept"
        return redirect('downloads')
    return render(request, 'policy.html')

@login_required
def downloads_page(request):
    return render(request, 'downloads.html')
