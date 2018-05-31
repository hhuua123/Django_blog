__author__ = 'hhuua'

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
import markdown
from django.utils.html import strip_tags

# 分类,文章的分类
class Category(models.Model):
    # 分类名
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 标签,文章的标签
class Tag(models.Model):
    # 标签名
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 文章
class Post(models.Model):
    # 文章标题
    title = models.CharField(max_length=70)
    # 文章正文
    body = models.TextField()
    # 文章摘要,设置blank=True，使该字段允许为空
    excerpt = models.CharField(max_length=200, blank=True)
    # 文章创建时间和最后修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    # 分类,为一对多关系,一篇文章只能有一个分类
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 标签,为多对多关系
    tags = models.ManyToManyField(Tag, blank=True)
    # 作者,也是一对多关系,使用User类绑定,User类是从django.contrib.auth.models导入的
    # 该模块是Django中内置的,可以帮助解决登录注册等流程
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 浏览量,在每次进入post页面时加一
    views = models.PositiveIntegerField(default=0)

    # 重写save方法,实现自动从正文中截取摘要
    def save(self, *args, **kwargs):
        if not self.excerpt:
            # 将body中的markdown语法转为html标签，再利用strip_tags方法
            # 去除所有的html标签来获取纯文本
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
            ])
            self.excerpt = strip_tags(md.convert(self.body))[:100]

        super(Post, self).save(*args, **kwargs)

    # 浏览量加一
    def increase_views(self):
        self.views += 1
        # 告诉Django，只更新views的数据,以增加数据库处理速度
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # reverse 函数会解析blog下的detail函数的url,并将传入的self.pk替换该url中的值
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time']
