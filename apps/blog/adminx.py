# -*- coding:utf-8 -*-
import xadmin
from .models import *
from xadmin import views


# 此类可以定义admin后台显示的字段，比如文章列表显示标题，创建时间，
class PostAdmin(object):
    # 展示的字段
    list_display = ['id', 'title', 'created_time', 'category', 'status']
    # 按文章名进行搜索
    search_fields = ['title']
    # 筛选
    list_filter = ['id', 'title', 'created_time', 'category', 'status']
    # 修改图标
    model_icon = 'fa fa-refresh'
    # 修改默认排序
    ordering = ['-id']

    # 设置只读字段
    readonly_field = ['']

    # 不显示某一字段
    exclude = ['']

    list_display_link = ['title']

    # style_fields = {'body':'ueditor'}


class CategoryAdmin(object):
    list_display = ['id','name']
    search_fields = ['name']
    model_icon = 'fa fa-list'


class TagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-tag'



class ArticleAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-refresh'

class ArticleCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-list'

class ArticleTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-tag'

class JobsAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-refresh'

class JobsCategoryAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-list'

class JobsTagAdmin(object):
    list_display = ['id', 'name']
    search_fields = ['name']
    model_icon = 'fa fa-tag'


class MeanListAdmin(object):
    list_display = ['id', 'title', 'link', 'icon', 'status']
    search_field = ['title']
    model_icon = 'fa fa-list'

class MessagesAdmin(object):
    list_display = ['id', 'name']
    model_icon = 'fa fa-pencil-square'

xadmin.site.register(Post,PostAdmin)
xadmin.site.register(Category,CategoryAdmin)
xadmin.site.register(Tag,TagAdmin)
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(ArticleCategory,ArticleCategoryAdmin)
xadmin.site.register(ArticleTag,ArticleTagAdmin)
xadmin.site.register(Jobs,JobsAdmin)
xadmin.site.register(JobsCategory,JobsCategoryAdmin)
xadmin.site.register(JobsTag,JobsTagAdmin)
xadmin.site.register(Messages,MessagesAdmin)
xadmin.site.register(MeanList,MeanListAdmin)


# 修改xadmin的基础配置
class BaseSetting(object):
    # 允许使用主题
    enable_themes = True
    use_bootswatch = True


# 修改xadmin的全局配置
class GlobalSetting(object):
    site_title = '未知的小博客后台'
    site_footer = '2020.6.14'

    # Models收起功能
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(views.BaseAdminView,BaseSetting )