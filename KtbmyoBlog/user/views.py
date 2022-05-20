from django.shortcuts import  render,redirect
from . forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib import messages

# Create your views here.
def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)

        newUser.save()
        login(request,newUser)
        messages.info(request,'Başarıyla Kayıt Oldunuz...')
        return redirect("index")
            
    context = {"form" : form}
    return render(request,"register.html",context)



def loginUser(request):
    form = LoginForm(request.POST or None)
    context = {
        "form" : form
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)

        if user is None : #böyle bir kullanıcı yoksa
            messages.info(request,"Kullanıcı Adı veya Parola Hatalı")
            return render(request,"login.html",context)
        #Kullanıcı varsa user varsa if blogu çalışmaz
        messages.info(request,"Başarıyla Giriş Yaptınız")
        login(request,user)
        return redirect("index")
    #form is valid değilse yani bir hata ile karsılasıldıysa
    return render(request,"login.html",context)

def logoutUser(request):
    logout(request)
    messages.info(request,"Başarıyla Çıkış Yapıldı")
    return redirect("index")
    
