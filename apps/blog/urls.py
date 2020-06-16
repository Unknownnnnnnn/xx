from django.urls import path
from . import views
app_name = "blog"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),

    path('archives/', views.ArchivesView.as_view(), name='archives'),
    path('post/<int:pk>', views.article, name='article'),

    path('categories/', views.Categories.as_view(), name='categories'),
    path('category/<int:pk>', views.CategoryView.as_view(), name='category'),

    path('tags/', views.TagsView.as_view(), name='tags'),
    path('tag/<int:pk>', views.TagListView.as_view(), name='tag_list'),

    path('Articles/', views.ArticlesView.as_view(), name='Articles'),
    path('Article_list/<int:pk>', views.ArticleListView.as_view(), name='Article_list'),

    path('Jobss/', views.JobssView.as_view(), name='Jobss'),
    path('Jobs_list/<int:pk>', views.JobsListView.as_view(), name='Jobs_list'),

    path('messages/', views.messages, name='messages'),

    path('download/', views.file_test, name='download'),

]