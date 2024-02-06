from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

from .models import Member
# Create your views here.
def index(request):
    # return HttpResponse("This is home Page")
    
    if request.user.is_anonymous:
        return redirect('/loginUser')
    
    members= Member.objects.all()
    return render(request,'index.html',{"members":members})


def loginUser(request):
    print(request.method)  # Print the request method to the console for debugging
    if request.method == "POST":
        # If the request method is POST, it means the user has submitted the login form
        name = request.POST.get('username')  # Retrieve username from the POST data
        password = request.POST.get('password')  # Retrieve password from the POST data
        user = authenticate(username=name, password=password)  # Attempt to authenticate the user
        if user is not None:
            print(user)
            login(request,user)
            return redirect('/')
        else:
            # If authentication fails, render the login page again (possibly showing an error message)
            return render(request, 'login.html') 
    else:
        # If the request method is not POST (e.g., GET), render the login page
        return render(request, 'login.html')
            
     

def logoutUser(request):
    logout(request)
    return render(request,'login.html')


from .models import Member  # Assuming you have a model named Member

def createPost(request):
    if request.method == 'POST' and not request.user.is_anonymous:
        description = request.POST.get('description')
        name = request.user.username  # Retrieve the username directly
        print(name)
        member = Member(firstname=name, description=description)
        member.save()
        print(member)
        # Handle form submission, possibly saving the form data to the database
        return redirect('/')
    return render(request, 'create_post.html')

def deletePost(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    
    elif request.method == 'POST':
        # Fetch parameters from request.GET for query parameters
        _id = request.GET.get('_id')  # Fetch the _id parameter from the URL
        _name = request.GET.get('_name')  # Fetch the _name parameter from the URL
        
        try:
            mypost = Member.objects.get(id=_id)  # Retrieve the specific post
            firstname = mypost.firstname
            if request.user.username==firstname:
                mypost.delete()
            
        except Member.DoesNotExist:
            
            return HttpResponse("Post not found", status=404)

          # Print the post to the console for debugging
        # Delete the post
        return redirect('/') 
    

def change(request):
    if request.user.is_anonymous:
        return redirect('/loginUser')
    
    elif request.method == 'POST':  
        id= request.GET.get('_id')
        try:
            mypost = Member.objects.get(id=id)
            data= request.POST.get('data')
            firstname= mypost.firstname
            if request.user.username==firstname and data is not None:
               mypost.description=data
               mypost.save()

        except Member.DoesNotExist or data is None:
            
            return HttpResponse("Post not found", status=404)   

    return redirect('/')      
   

    
