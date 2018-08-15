from django.shortcuts import render
from datetime import datetime
from .models import Article
from .models import Language


def index(request): #index
    context ={
        'current_date':datetime.now(),
        'title': 'Home'
    }
    return render(request, 'index.html',context)



def about (request): #about
    context ={
        'current_date':datetime.now(),
        'title': 'About'
    }
    return render(request, 'about.html',context)

def news(request): #navigates to news page
    populate_db()
    articles = get_articles()

    context = {
        'articles':articles,
        'current_date':datetime.now(),
        'title':'Tech News'
    }
    #returning a render having a request, go to news.html and pass that context
    return render(request,'news.html',context)
def get_articles():
    result = Article.objects.all() #pylint: disable=E1101
    return result

def populate_db():
    if Article.objects.count()==0: #pylint: disable=E1101
        Article(title = 'First item',content = 'This is the first db item').save()
        Article(title = 'Second item',content = 'This is the second db item').save()
        Article(title = 'Third item',content = 'This is the third db item').save()



def coding (request): #coding
    populate_db()
    languages = get_language()
    context ={
        'languages':languages,  #very important to place inorder to take the datas from the table form models.py
        'current_date':datetime.now(),
        'title': '#include </code>'
    }
    return render(request, 'coding.html',context)
def get_language():
    result = Language.objects.all() #pylint: disable=E1101
    return result

def pop_db():
    if Language.objects.count()==0: #pylint: disable=E1101
        Language(title = 'C programs',content = 'C programs').save()
        Language(title = 'C++ programs',content = 'C++ programs').save()
        Language(title = 'Python programs',content = 'Python programs').save()


#materials
def materials (request): 
    context ={
        'current_date':datetime.now(),
        'title': 'Tools and Materials'
    }
    return render(request, 'materials.html',context)