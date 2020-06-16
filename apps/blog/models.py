# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.html import strip_tags
import django.utils.timezone as timezone
from mdeditor.fields import MDTextField


# 创建博文分类的表
class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='分类名称')

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "文章分类"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:category', kwargs={'pk': self.pk})


# 创建文章标签的表
class Tag(models.Model):
	# name是标签名的字段
	name = models.CharField('标签名称',max_length=100)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "文章标签"
		verbose_name_plural = verbose_name

	def get_absolute_url(self):
		return reverse('blog:tag_list', kwargs={'pk': self.pk})


# 创建文章的类
class Post(models.Model):

	# 发表状态
	PUBLISH_STATUS = (
		('p', '文章页'),
		('c', '教程页'),
		('d', '草稿箱'),
		('r', '回收站'),
	)

	# 是否置顶
	STICK_STATUS = (
		('y', '置顶'),
		('n', '不置顶'),
	)

	title = models.CharField('标题', max_length=100, unique=True)
	body = MDTextField('正文')
	created_time = models.DateTimeField('创建时间', default=timezone.now)
	modified_time = models.DateTimeField('修改时间', auto_now=True)
	excerpt = models.CharField('摘要', max_length=200, blank=True, )
	views = models.PositiveIntegerField('阅读量', default=0)
	words = models.PositiveIntegerField('字数', default=0)
	category = models.ForeignKey(Category, verbose_name='文章分类', on_delete=models.CASCADE)
	tag = models.ManyToManyField(Tag, verbose_name='标签类型', blank=True)
	author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)
	status = models.CharField('文章状态', max_length=1, choices=PUBLISH_STATUS, default='p')

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title

	def get_user(self):
		return self.author

	# 阅读量增加1
	def increase_views(self):
		self.views += 1
		self.save(update_fields=['views'])

	def save(self, *args, **kwargs):
		if not self.excerpt:
			self.excerpt = strip_tags(self.body).replace("&nbsp;", "").replace("#", "")[:150]
		self.words = len(strip_tags(self.body).replace(" ", "").replace('\n', ""))
		super(Post, self).save(*args, **kwargs)

	class Meta:
		verbose_name = "添加文章"
		verbose_name_plural = verbose_name
		ordering = ['-created_time']


class ArticleCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="分类名称")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "论文分类"
		verbose_name_plural = verbose_name


class ArticleTag(models.Model):
	name = models.CharField(max_length=100, verbose_name="标签")

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:Article_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "论文标签"
		verbose_name_plural = verbose_name


class Article(models.Model):
	name = models.CharField("论文名", max_length=100)
	author = models.CharField("论文来自", max_length=100)
	category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name="论文分类")
	tag = models.ManyToManyField(ArticleTag, verbose_name="论文标签")
	cover = models.ImageField("网络模型图", upload_to='Articles', blank=True)
	created_time = models.DateField("添加时间", null=True, default=timezone.now)
	time_consuming = models.CharField("阅读初始时间", max_length=100)
	pid = models.CharField("文章ID", max_length=100, blank=True)
	def __str__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pid})
	class Meta:
		verbose_name = "添加论文"
		verbose_name_plural = verbose_name
		ordering = ['-pk']
class JobsCategory(models.Model):
	name = models.CharField(max_length=100, verbose_name="项目分类")

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "项目分类"
		verbose_name_plural = verbose_name


class JobsTag(models.Model):
	name = models.CharField(max_length=100,verbose_name="标签名称",blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:Article_list', kwargs={'pk': self.pk})

	class Meta:
		verbose_name = "项目标签"
		verbose_name_plural = verbose_name


class Jobs(models.Model):
	name = models.CharField("项目名称", max_length=100)
	director = models.CharField("项目来自", max_length=100)
	actor = models.CharField("项目作者", max_length=100)
	category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name="项目分类")
	tag = models.ManyToManyField(ArticleTag, verbose_name="项目标签")
	cover = models.ImageField("计划书", upload_to='Articles', blank=True)
	release_time = models.DateField("开始时间")
	pid = models.CharField("文章ID", max_length=100, blank=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:article', kwargs={'pk': self.pid})

	class Meta:
		verbose_name = "添加项目"
		verbose_name_plural = verbose_name
		ordering = ['-pk']


class Messages(models.Model):
	name = models.CharField(max_length=100,verbose_name="给我留言")
	admin = models.ForeignKey(User,verbose_name='站长',on_delete=models.CASCADE,blank=True,null=True)

	def get_absolute_url(self):
		return reverse('blog:messages')

	def get_user(self):
		return self.admin

	class Meta:
		verbose_name = "网站留言"
		verbose_name_plural = verbose_name


class MeanList(models.Model):

	STATUS = (
		('y', '显示'),
		('n', '隐藏'),
	)

	title = models.CharField("菜单名称", max_length=100)
	link = models.CharField("菜单链接", max_length=100, blank=True, null=True,)
	icon = models.CharField("菜单图标", max_length=100, blank=True, null=True,)
	status = models.CharField('显示状态', max_length=1, choices=STATUS, default='y')

	class Meta:
		verbose_name = "菜单栏"
		verbose_name_plural = verbose_name