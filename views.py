from django.shortcuts import render,HttpResponseRedirect
from testapp.models import BlogModel
from testapp.forms import BlogForm,SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def HomeView(request):
    obj=BlogModel.objects.all()
    context={'blog':obj}
    return render(request,'testapp/home.html',context=context)
def DetailView(request,id):
    emp=BlogModel.objects.get(id=id)
    return render(request,'testapp/detail.html',{'emp':emp})
@login_required()
def addblog(request):
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
           obj=form.save(commit=False)
           obj.author=request.user
           obj.save()
           return HttpResponseRedirect('/myposts')
    return render(request,'testapp/addblog.html',{'form':form})
def signupview(request):
    form=SignUpForm()
    if request.method=='POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{'form':form})
@login_required()
def mypostview(request):
    mypostdata=BlogModel.objects.filter(author=request.user)
    return render(request,'testapp/myposts.html',{'posts':mypostdata})
def updateview(request,id):
    blog=BlogModel.objects.get(id=id)
    form=BlogForm(instance=blog)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,instance=blog)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/myposts')
    return render(request,'testapp/update.html',{'form':form})
def deleteview(request,id):
    emp=BlogModel.objects.get(id=id)
    emp.delete()
    return HttpResponseRedirect('/myposts')
def notfoundview(request,exception):
    return render(request,'testapp/notfound.html',status=404)


