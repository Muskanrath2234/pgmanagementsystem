from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic import  DetailView, UpdateView, DeleteView,ListView
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class PostListView(ListView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'




class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm  # Use the customized form
    template_name = 'create_post.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'
    template_name = 'post_confirm_delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the form data to the database
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post')  # Redirect to the user's profile page
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})



def adminlogin(request):
    if request.method == 'POST':
        adminname = request.POST.get('adminname')
        adminpassword = request.POST.get('adminpassword')

        user = authenticate(request, username=adminname,password= adminpassword)

        if user  and user.is_superuser:

            login(request,user)
            return redirect('post')

        else:

             error_message = 'Invalid username or password. Only superusers can log in.'
             return render(request,'adminlogin.html',{'error_message':error_message})


    return render(request,'adminlogin.html')

def admindash(request):
    return render(request, 'admindash.html')


def register_user(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Account is created.')
            return redirect('user_login')
        else:
            context = {'form': form}
            messages.info(request, 'Invalid credentials')
            return render(request, 'register_page.html', context)

    context = {'form': form}
    return render(request, 'register_page.html', context)

def view_all_users(request):
   users = User.objects.all()
   return render(request,'view_all_users.html',{'users':users})





@login_required
def profilehome(request):
    user = request.user
    return render(request, 'profilehome.html', {'user': user})


@login_required(login_url='user_login')
def editprofile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            username = request.user.username
            messages.success(request, f'{username}, Your profile is updated.')
            return redirect('profilehome')
    else:
        form = ProfileForm(instance=request.user.profile)
    context = {'form': form}
    return render(request, 'editprofile.html', context)

def user_logout(request):
    logout(request)
    return redirect('user_login')


