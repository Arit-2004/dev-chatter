from django.shortcuts import render,get_object_or_404,redirect
from .models import Tweet 
from .forms import TweetFrom , UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.db.models import Q


# Create your views here.

def index(request):
      query = request.GET.get('q','').strip()
      tweets = Tweet.objects.all().order_by('created_at')
      if query:
         tweets = tweets.filter(
              Q(content__icontains=query)|
              Q(user__username__icontains=query)
          )
      if not tweets.exists():
        return render(request, 'no_result.html', {'query': query})
      return render(request, 'index.html', {'tweets' : tweets , 'query':query})

@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetFrom(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('index')
    else:
      form = TweetFrom()
    return render(request, 'tweet_form.html', {'form':form})   
       
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk = tweet_id , user = request.user)
    if request.method == 'POST':
        form = TweetFrom(request.POST , request.FILES, instance=tweet)
        if form.is_valid():
            tweet=form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('index')
    else:
       form = TweetFrom(instance=tweet)
    return render(request, 'tweet_form.html', {'form':form})   

@login_required
def tweet_delete(request,tweet_id):
    tweet = get_object_or_404(Tweet , pk = tweet_id , user = request.user)
    if request.method == 'POST':
        tweet.delete()
        return redirect('index')
    return render(request , 'tweet_confirm_delete.html', {'tweet' : tweet})


# Authentication 

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
           user = form.save(commit=False)
           user.set_password(form.cleaned_data['password1'])
           user.save()
           login(request,user)
           return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request , 'registration/register.html', {'form' : form})
    
