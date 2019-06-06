from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import HelloForm
from django.shortcuts import redirect

# Create your views here.

def index(request):
    data = Post.objects.all()
    params = {
        'title': 'みんなの投稿の一覧',
        'data': data,
    }
    return render(request, 'hello/index.html', params)

def create(request):
    params = {
        'title': '投稿フォーム',
        'form': HelloForm(),
    }
    if (request.method == 'POST'):
        name = request.POST['name'] 
        title = request.POST['title']
        text = request.POST['text']
        post = Post(name=name, title=title, text=text)
        post.save()
        return redirect(to='/hello')
    return render(request, 'hello/create.html', params)