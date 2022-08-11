from django.shortcuts import render


posts=[
    {
        'author':'DrenB',
        'title':'Django',
        'content':'Backend Framework',
        'date_posted':'August 10,2022'
    },

    {
        'author': 'Test',
        'title': 'FastApi',
        'content': 'Backend Framework vs Django',
        'date_posted': 'August 11,2022'
    },
]


def home(request):
    context={
        'posts': posts
    }
    return render(request,'blog/home.html', context)


def about(request):
    return render(request,'blog/about.html',{'title':'About'})
