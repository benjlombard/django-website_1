from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.generic import ListView
from .forms import EmailPostForm

from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect

from .forms import GenerateRandomUserForm
from .tasks import create_random_user_accounts




from django.views.generic import TemplateView


def post_share(request,post_id):
    post = get_object_or_404(Post,id=post_id,status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request,'blog/post/share.html',{'post':post,'form':form})
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

# Create your views here.
def post_list(request):
    object_list = Post.published.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    #posts = Post.published.all()
    return render(request,'blog/post/list.html',{'posts':posts,'page':page})

def post_detail(request,year,month,day,post):
    post=  get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day = day)
    return render(request,'blog/post/detail.html',{'post':post})






class UsersListView(ListView):
    template_name = 'blog/post/users_list.html'
    model = User


class GenerateRandomUserView(FormView):
    template_name = 'blog/post/generate_random_users.html'
    form_class = GenerateRandomUserForm

    def form_valid(self, form):
        total = form.cleaned_data.get('total')
        create_random_user_accounts.delay(total)
        messages.success(self.request, 'We are generating your random users! Wait a moment and refresh this page.')
        return redirect('blog:users_list')