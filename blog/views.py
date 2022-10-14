from contextlib import redirect_stderr
from django.shortcuts import render, get_object_or_404,redirect
from shop.models import Order
from .models import *
from app.views import home
from django.contrib import messages
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from .filter import * 

@csrf_exempt
def detail(request, blog_id):
   
    comment_name = request.POST.get('comment_name')
    comment_mail = request.POST.get('comment_mail')
    comment = request.POST.get('comment')
    if request.method == 'POST':
            data_comment = Comment(comment_name=comment_name,comment_mail=comment_mail,
            comment=comment,blog=Blog.objects.get(pk=blog_id)) 
            data_comment.save()


    blog = get_object_or_404(Blog, pk=blog_id)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        cartItems = order.get_cart_items
    else:
        cartItems = 0




    context = {'blog': blog, 'cartItems': cartItems,
      'recents_blog': Blog.objects.order_by('-published')[0:3],
      'com':Comment.objects.all(),
      'c':Comment.objects.first(),
    }
    return render(request, 'blog/blog-details.html', context)


def blog(request):
    blogs = Blog.objects.all()

    ##filters by categorie
   
    paginator = Paginator(blogs, 4) 
    page = request.GET.get('page')
    blogs = paginator.get_page(page)

    if request.user.is_authenticated:#ida kan user authentifie
        customer = request.user.customer#cree customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)#order get create men customer
        cartItems = order.get_cart_items
    else:
        cartItems = 0
    


    categ=Category.objects.all()
    test = Blog.objects.all()

    context = {'blogs': blogs,'categ':categ,'recents_blog': Blog.objects.order_by('-published')[0:5],
    'ca':Category.objects.all(),'cartItems': cartItems,}

    return render(request, 'blog/blog.html', context)




def cat_blog(request,slug):
    category_blog = Blog.objects.filter(category=slug)
    
    product = get_object_or_404(Category, pk=slug)

    ca=Category.objects.all()
    context={'recents_blog': Blog.objects.order_by('-published')[0:5],
    'slug':category_blog,'ca':ca,
    'product':product,
    }
    return render(request, 'blog/cat_blog.html',context)
    