from django.shortcuts import render

posts = [
    {
        'author': 'Shreeji Patel',
        'title' : 'First Post',
        'content' : 'First Post Content',
        'date_posted': 'August 27, 2019'
    },
    {
        'author': 'Someone Patel',
        'title' : 'Second Post',
        'content' : 'Second Post Content',
        'date_posted': 'August 27, 2019'
    }
]

def home(request):
    context= {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

