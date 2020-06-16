from django.shortcuts import reverse,redirect
from .models import Comment
from apps.comment.form import CommentForm


# 添加评论
def update_comment(request):
    referer = request.META.get('HTTP_REFERER', reverse('blog:index'))
    comment_form = CommentForm(request.POST, user=request.user)
    if comment_form.is_valid():
        comment = Comment()
        comment.user = comment_form.cleaned_data['user']
        comment.text = comment_form.cleaned_data['text']
        comment.content_object = comment_form.cleaned_data['content_object']
        parent = comment_form.cleaned_data['parent']
        if not parent is None:
            comment.root = parent.root if not parent.root is None else parent
            comment.parent = parent
            comment.reply_to = parent.user
        comment.save()
    return redirect(referer+'#comment')
