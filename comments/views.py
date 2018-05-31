from django.shortcuts import render, get_object_or_404, redirect
from blog.models import Post
from .forms import CommentForm

def post_comment(request, post_pk):
    # 获取主键为post_pk的文章,如无法获取,则直接抛出404页面
    post = get_object_or_404(Post, pk=post_pk)
    # 该API设计为用户提交评论,因此只接受post
    if request.method == 'POST':
        # from提交的内容保存在request.POST中,使用CommentForm方法
        form = CommentForm(request.POST)
        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 使用commit=False,只把form转为comment对象,暂时不存储到数据库
            comment = form.save(commit=False)
            # 将评论和被评论的文章关联起来。
            comment.post = post
            # 最终将评论数据保存进数据库，调用模型实例的 save 方法
            comment.save()
            # 使用重定向,当redirect函数接受到一个Model实例时,会调用Model的'get_absolute_url'方法,并重定向到返回的url
            return redirect(post)
        else:
            # comment_set方法将会获取与该post相关联的所有comment对象
            comment_list = post.comment_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            # 返回context用于渲染表单
            return render(request, 'blog/detail.html', context=context)
    # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
    return redirect(post)