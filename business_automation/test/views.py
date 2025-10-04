from django.shortcuts import render

posts = [
    {
        'author': 'Corey',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'John',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'August 27, 2018'
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'test/home.html', context, )

def about(request):
    return render(request, 'test/about.html',{'title': 'About'})
