from django.shortcuts import render, redirect
from django.contrib.auth import login, logout,authenticate
from django.views import generic 
from .models import ItemModel,User,Seller,Buyer,cart,Buy
from .forms import SellerSignUpForm, BuyerSignUpForm ,ItemForm
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib import messages
from django.db.models import Q
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
#LIST OF ALL PRODUCT
class ProductListView(generic.ListView):
    model = ItemModel
    
class SellerSignUpView(generic.CreateView):
    model = User
    form_class = SellerSignUpForm
    template_name = 'signup_form.html'
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:home')

class BuyerSignUpView(generic.CreateView):
    model = User
    form_class = BuyerSignUpForm
    template_name = 'signup_form.html'
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('accounts:home')


def LogOut(request):
    logout(request)
    return redirect('accounts:home')

def LogIn(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            try :
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}")
                    if user.is_seller == True :                                
                        return redirect('accounts:sellerview' )
                    else:   
                        return redirect('accounts:buyerview' )                 
                else:
                    messages.error(request, "Invalid username or password.")
                    
            except :
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
        
        return redirect('accounts:login')
    else:
        form = AuthenticationForm()
        return render( request,
                    "login.html",
                    {"form":form})
    
       
def SellerView(request):
    item_list = ItemModel.objects.filter(seller=request.user)
    return render(request,'sellerview.html',{'item_list':item_list})


def BuyerView(request):
    # user = Buyer.objects.get(user=request.user)
    cart_n = cart.objects.filter(user=request.user).all()
    print(cart_n)
    return render(request,'buyerview.html',{'item_list':cart_n})

def ItemFormView(request):
    if request.method == "POST":
        form = ItemForm(request.POST or None, request.FILES or None)
        if form.is_valid() :
            form = form.save(commit=False)
            form.seller = request.user
            form.save()
        else :
            print(form.errors)
        return redirect('accounts:sellerview')
    else :
        form = ItemForm()
        return render(request,'item_form.html',{'form':form})

def AddCartView(request):
    item = ItemModel.objects.get(id=request.POST.get('item_id'))
    if request.user.is_authenticated:
        obj, created = cart.objects.get_or_create(user=request.user,item=item)
        print(obj,created)
        if created :
            is_added = True
        else :
            obj.delete()
            is_added = False
        
        return JsonResponse({'is_added':is_added})

def BuyView(request,pk):
    item = ItemModel.objects.get(id=pk)
    new_item = ItemModel.objects.filter(id=pk)
    new_item.update( quantity = int(item.quantity) - 1)
    if request.user.is_authenticated:
        Buy.objects.get_or_create(user=request.user,item=item)
    return redirect('accounts:home')
    


# Create your views here.

def SearchResultView(request):
    query = request.GET.get('query')
    object_list = ItemModel.objects.filter(
        Q(item_name__icontains=query)
        | Q(item_description__icontains=query)
        | Q(price__icontains=query) | Q(seller__username__icontains=query) 
    )
    rendered_html =  render_to_string('accounts/itemmodel_list.html',{'csrf_token':request.GET.get('csrf'),'itemmodel_list':object_list,
                                                'request':request})
    data = {'rendered_html':rendered_html}
    return JsonResponse(data,safe=False)
        

class ItemUpdateView(generic.UpdateView,LoginRequiredMixin):
    model = ItemModel
    form_class = ItemForm
    success_url = "/"

class ItemDeleteView(generic.DeleteView,LoginRequiredMixin):
    model = ItemModel
    success_url = "/"

