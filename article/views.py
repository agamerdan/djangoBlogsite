from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse
from .forms import Articleforms
from django.contrib import messages
from .models import Articles,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
   
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def articles(request):   #Arama işlemi
    keyword=request.GET.get("keyword")
    if keyword:
        articles=Articles.objects.filter(title=keyword)
        return render(request, "articles.html",{"articles": articles})
    articles=Articles.objects.all()
    return render(request, "articles.html",{"articles":articles})

@login_required(login_url="user:login")
def dashboard(request):  #Konturol Paneli
    articles=Articles.objects.filter(autor=request.user)
    context={
        "articles": articles
    }
    return render(request,"dashboard.html", context)

@login_required(login_url="user:login")
def addarticle(request): #Makale ekleme
    form=Articleforms(request.POST or None, request.FILES or None)
    if form.is_valid():
        article=form.save(commit=False)
        article.autor=request.user
        article.save()
        messages.success(request,"Makaleniz Başarıyla Oluşturuldu")
        return redirect("index")
    
    return render(request,"addarticle.html",{"form":form})

def detail(request, id):  
    #article=Articles.objects.filter(id=id).first()
    article=get_object_or_404(Articles,id=id)
    comments=article.comments.all()
    return render(request,"detail.html",{"article":article, "comments":comments})

@login_required(login_url="user:login")
def update(request, id):  #Makale Güncelle
    article=get_object_or_404(Articles,id=id)
    form=Articleforms(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
         article=form.save(commit=False)
         article.autor=request.user
         article.save()
         messages.success(request,"Makaleniz Başarıyla Güncellendi")
         return redirect("article:dashboard")
        
    return render(request, "update.html",{"form":form})

@login_required(login_url="user:login")
def delete(request, id): #Makale Sil
    article=get_object_or_404(Articles,id=id)
    article.delete()
    messages.success(request,"Makaleniz Başarıyla Silindi")
    return redirect("article:dashboard")

#Yorum Ekle
def comment(request, id):
    article=get_object_or_404(Articles,id=id)
    if request.method=="POST":
        comment_autor=request.POST.get("comment_autor")
        comment_content=request.POST.get("comment_content")
        
        newComment=Comment(comment_autor=comment_autor,comment_content=comment_content)
        newComment.article=article
        newComment.save()
    return redirect(reverse("article:detail",kwargs={"id":id}))
        
    
    
