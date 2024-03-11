from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate,login
from django.http import HttpResponseNotFound
from django.contrib.auth import logout
#from our users form
from users.forms import UserCreationForm

# Create your views here.
class Register(View):
    template_name = 'registration/register.html'

    # GET
    def get(self,request):
        context ={
            'form': UserCreationForm(),
        }
        return render(request, self.template_name, context)
    

    #POST
    def post(self,request):
        
        #take data from Usercreationform
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')     
            user = authenticate(username = username, password = password)
            login(request, user)
            

            return redirect('home')
        context = {
            'form' : form
        }

        return render(request, self.template_name, context)
    
    #Logout
def logout_view(request):
    logout(request)

#Exception 404
def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1> There is no similar page</h1></hr><a href='http://127.0.0.1:8000/'> Home</a>")

    #Exception 403
def IncorrectLogin(request,exception):
    return HttpResponseNotFound("<a href='login'> Try again</a>")