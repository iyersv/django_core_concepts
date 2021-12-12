from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
# Create your views here.
from .models import PostModel
from django.contrib.auth.decorators import login_required

from blog.forms import PostModelForm

def home(request):
    return HttpResponse('Home Blog Page')

def post_model_robust_view(request,pk=None):
    obj = None
    context = {}
    success_message = 'A new post was created'
    template = "blog/detail-view.html"

    if pk is None:
        template ="blog/create-view.html"

    if pk is not None:
        obj = get_object_or_404(PostModel,id=pk)
        context={
            "object_list":obj
        }
    if "update" in request.get_full_path():
        template = 'blog/update-view.html'

    if "delete" in request.get_full_path():
        template = "blog/delete-view.html"
        if request.method=="POST":
            obj.delete()
            return HttpResponseRedirect("/blog/")

    if "update" in request.get_full_path() or "create" in request.get_full_path():
        form = PostModelForm(request.POST or None, instance=obj)
        context["form"] = form
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            if obj is not None:
                return HttpResponseRedirect(f'blog/{obj.id}')
            context["form"] = PostModelForm()

    return render(request,template,context)

def post_model_create_view(request):

    form= PostModelForm(request.POST or None)

    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.title)
        print(form.cleaned_data)
        obj.save()
        messages.success(request,'Successfully Saved a new blog')
        return HttpResponseRedirect(f'/blog/{obj.id}')
    context ={
        'form' : form
    }
    template="blog/create_view.html"
    return render(request, template, context)


def post_model_update_view(request,pk=None):
    qs = get_object_or_404(PostModel, id=pk)
    form= PostModelForm(request.POST or None,instance=qs)
    context ={
        'obj'  : qs,
        'form' : form
    }
    if form.is_valid():
        obj = form.save(commit=False)
        print(obj.title)
        print(form.cleaned_data)
        obj.save()
        messages.success(request,'Updated blog')
        return HttpResponseRedirect(f'/blog/{obj.id}')

    template="blog/update_view.html"
    return render(request, template, context)

def post_model_delete_view(request,pk):
    qs = get_object_or_404(PostModel,id=pk)
    if request.method == 'POST':
        qs.delete()
        return HttpResponseRedirect(f'/blog/')
    template="blog/delete-view.html"
    context={
        "object_list":qs
    }
    # return HttpResponse("test")
    return render(request,template,context)


def post_model_detail_view(request,pk):
    qs = get_object_or_404(PostModel,id=pk)
    context ={

    }
    template="blog/detail-view.html"
    context={
        "object_list":qs
    }
    # return HttpResponse("test")
    return render(request,template,context)

def post_model_list_view(request):
    qs = PostModel.objects.all()
    print(qs)
    template="blog/list-view.html"
    context={
        "object_list":qs
    }
    # return HttpResponse("test")
    return render(request,template,context)