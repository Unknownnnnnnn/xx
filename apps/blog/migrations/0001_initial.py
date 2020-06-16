# Generated by Django 2.1.11 on 2020-06-13 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='书名')),
                ('author', models.CharField(max_length=100, verbose_name='作者')),
                ('cover', models.ImageField(blank=True, upload_to='Articles', verbose_name='封面图')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='豆瓣评分')),
                ('created_time', models.DateField(default=django.utils.timezone.now, null=True, verbose_name='添加时间')),
                ('time_consuming', models.CharField(max_length=100, verbose_name='阅读初始时间')),
                ('pid', models.CharField(blank=True, max_length=100, verbose_name='文章ID')),
            ],
            options={
                'verbose_name': '添加图书',
                'verbose_name_plural': '添加图书',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '书单分类',
                'verbose_name_plural': '书单分类',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签')),
            ],
            options={
                'verbose_name': '书单标签',
                'verbose_name_plural': '书单标签',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='分类名称')),
            ],
            options={
                'verbose_name': '文章分类',
                'verbose_name_plural': '文章分类',
            },
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='教程名称')),
                ('cover', models.ImageField(blank=True, upload_to='course', verbose_name='上传封面')),
                ('category', models.CharField(max_length=100, verbose_name='教程分类')),
                ('introduce', models.CharField(blank=True, max_length=200, verbose_name='教程简介')),
                ('status', models.CharField(max_length=50, verbose_name='更新状态')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, null=True, verbose_name='创建时间')),
                ('comments', models.PositiveIntegerField(default=0, verbose_name='评论数')),
                ('numbers', models.PositiveIntegerField(default=0, verbose_name='教程数量')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
            ],
            options={
                'verbose_name': '教程列表',
                'verbose_name_plural': '教程列表',
            },
        ),
        migrations.CreateModel(
            name='MeanList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='菜单名称')),
                ('link', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单链接')),
                ('icon', models.CharField(blank=True, max_length=100, null=True, verbose_name='菜单图标')),
                ('status', models.CharField(choices=[('y', '显示'), ('n', '隐藏')], default='y', max_length=1, verbose_name='显示状态')),
            ],
            options={
                'verbose_name': '菜单栏',
                'verbose_name_plural': '菜单栏',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='给我留言')),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='站长')),
            ],
            options={
                'verbose_name': '网站留言',
                'verbose_name_plural': '网站留言',
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='电影名称')),
                ('director', models.CharField(max_length=100, verbose_name='导演')),
                ('actor', models.CharField(max_length=100, verbose_name='主演')),
                ('cover', models.ImageField(blank=True, upload_to='Articles', verbose_name='上传封面')),
                ('score', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='豆瓣评分')),
                ('release_time', models.DateField(verbose_name='上映时间')),
                ('created_time', models.DateField(default=django.utils.timezone.now, verbose_name='添加时间')),
                ('length_time', models.PositiveIntegerField(default=0, verbose_name='电影时长')),
                ('watch_time', models.DateField(default=django.utils.timezone.now, verbose_name='观看时间')),
                ('pid', models.CharField(blank=True, max_length=100, verbose_name='文章ID')),
            ],
            options={
                'verbose_name': '添加电影',
                'verbose_name_plural': '添加电影',
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='电影分类')),
            ],
            options={
                'verbose_name': '电影分类',
                'verbose_name_plural': '电影分类',
            },
        ),
        migrations.CreateModel(
            name='ArticleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '电影标签',
                'verbose_name_plural': '电影标签',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True, verbose_name='标题')),
                ('body', mdeditor.fields.MDTextField(verbose_name='正文')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
                ('modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('excerpt', models.CharField(blank=True, max_length=200, verbose_name='摘要')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='阅读量')),
                ('words', models.PositiveIntegerField(default=0, verbose_name='字数')),
                ('status', models.CharField(choices=[('p', '文章页'), ('c', '教程页'), ('d', '草稿箱'), ('r', '回收站')], default='p', max_length=1, verbose_name='文章状态')),
                ('stick', models.CharField(choices=[('y', '置顶'), ('n', '不置顶')], default='n', max_length=1, verbose_name='是否置顶')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='文章分类')),
            ],
            options={
                'verbose_name': '添加文章',
                'verbose_name_plural': '添加文章',
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='标签名称')),
            ],
            options={
                'verbose_name': '文章标签',
                'verbose_name_plural': '文章标签',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签类型'),
        ),
        migrations.AddField(
            model_name='Article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ArticleCategory', verbose_name='电影分类'),
        ),
        migrations.AddField(
            model_name='Article',
            name='tag',
            field=models.ManyToManyField(to='blog.ArticleTag', verbose_name='电影标签'),
        ),
        migrations.AddField(
            model_name='courses',
            name='article',
            field=models.ManyToManyField(blank=True, to='blog.Post', verbose_name='教程文章'),
        ),
        migrations.AddField(
            model_name='courses',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='作者'),
        ),
        migrations.AddField(
            model_name='Article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.ArticleCategory', verbose_name='书籍分类'),
        ),
        migrations.AddField(
            model_name='Article',
            name='tag',
            field=models.ManyToManyField(to='blog.ArticleTag', verbose_name='本书标签'),
        ),
    ]