import markdown
from .models import *
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.utils.html import strip_tags
from django.shortcuts import render, get_object_or_404, HttpResponse
from eastnotes.settings import base
import os


# 文章列表页父类
class ArticleListView(ListView):
    template_name = 'blog/index.html'  # 指定页面模板
    context_object_name = 'posts'           # 指定传参变量名
    paginate_by = base.ARTICLE_PAGINATE_BY  # 指定单页文章数量

    def get_queryset(self):
        return Post.objects.filter(status='p')


# 首页
class IndexView(ArticleListView):
    pass


# 归档页
class ArchivesView(ArticleListView):
    template_name = 'blog/archives.html'
    paginate_by = None


# 标签页
class TagsView(ListView):
    model = Tag
    template_name = 'blog/tags.html'
    context_object_name = 'tags'


# 各标签下文章列表
class TagListView(ArticleListView):
    template_name = 'blog/tag_list.html'

    def get_queryset(self):
        tag = get_object_or_404(Tag, pk=self.kwargs.get('pk'))
        self.tag_name = tag.name
        return Post.objects.filter(tag=tag, status='p')

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name
        return super(TagListView, self).get_context_data(**kwargs)


# 分类页
class Categories(ArticleListView):
    template_name = 'blog/category_list.html'
    paginate_by = None

    def get_context_data(self, **kwargs):
        self.cate_count = Category.objects.all().count()
        kwargs['cate_count'] = self.cate_count
        return super(Categories, self).get_context_data(**kwargs)


# 各分类下的文章列表
class CategoryView(ArticleListView):
    template_name = 'blog/category.html'

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        self.cate_name = cate.name
        return Post.objects.filter(category=cate, status='p')

    def get_context_data(self, **kwargs):
        kwargs['cate_name'] = self.cate_name
        return super(CategoryView, self).get_context_data(**kwargs)


def article(request, pk):
    post = get_object_or_404(Post, pk=pk,)
    author = User.objects.get(id=post.author_id)
    category = Category.objects.get(id=post.category_id)
    post.increase_views()  # 阅读量加1
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
        'markdown.extensions.fenced_code',

    ])

    post.body = md.convert(post.body)
    if strip_tags(md.toc).strip() == '':
        post.toc = ''
    else:
       post.toc = md.toc

    # 获取相关文章
    relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]

    context = {}
    context['post'] = post
    context['author'] = author
    context['category'] = category
    context['relative_posts'] = relative_posts
    return render(request, 'blog/article.html', context)


class JobsArticleListView(ListView):
    template_name = 'Article/Articles.html'
    context_object_name = 'lists'
    paginate_by = base.Article_Jobs_PAGINATE_BY

    def get_queryset(self):
        return Article.objects.all()


class ArticleView(ListView):
    pass


class ArticleListView(ListView):
    template_name = 'Article/Article_list.html'

    def get_queryset(self):
        tag = get_object_or_404(ArticleTag, pk=self.kwargs.get('pk'))
        self.tag_name = tag.name
        return Article.objects.filter(tag=tag)

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name
        return super(ArticleListView, self).get_context_data(**kwargs)


# 影单页
class JobssView(JobsArticleListView):
    template_name = 'Jobs/Jobss.html'

    def get_queryset(self):
        return Jobs.objects.all()


# 各标签下影单列表
class JobsListView(JobsArticleListView):
    template_name = 'Jobs/Jobs_list.html'

    def get_queryset(self):
        tag = get_object_or_404(JobsTag, pk=self.kwargs.get('pk'))
        self.tag_name = tag.name
        return Jobs.objects.filter(tag=tag)

    def get_context_data(self, **kwargs):
        kwargs['tag_name'] = self.tag_name
        return super(JobsListView, self).get_context_data(**kwargs)


class CoursesView(ListView):
    template_name = 'course/courses.html'
    context_object_name = 'courses'

    def get_queryset(self):
        return Courses.objects.all()


def messages(request):
    messages = Messages.objects.get(pk=1)
    return render(request, 'blog/messages.html', {'messages': messages})


# def course(request, pk):
#     course = get_object_or_404(Courses, pk=pk)
#     return render(request, 'course/course.html', context={'course': course})


# def course_article(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     author = User.objects.get(id=post.author_id)
#     category = Category.objects.get(id=post.category_id)
#     post.increase_views()  # 阅读量加1
#     md = markdown.Markdown(extensions=[
#         'markdown.extensions.extra',
#         'markdown.extensions.codehilite',
#         'markdown.extensions.toc',
#     ])
#     post.body = md.convert(post.body)
#     if strip_tags(md.toc).strip() == '':
#         post.toc = ''
#     else:
#         post.toc = md.toc
#
#     # 获取相关文章
#     relative_posts = Post.objects.filter(category_id=post.category_id, status='p').exclude(pk=pk).order_by('?')[:4]
#
#     context = {}
#     context['post'] = post
#     context['author'] = author
#     context['category'] = category
#     context['relative_posts'] = relative_posts
#     context['course'] = post.courses_set.first()
#     return render(request, 'course/course.html', context)


def file_test(request):
    file_path = os.path.join(base.STATIC_ROOT, "1.txt")
    file = open(file_path, "rb")
    response = HttpResponse(file)
    print(file)
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    response['Content-Disposition'] = 'attachment;filename=1.txt'
    return response



