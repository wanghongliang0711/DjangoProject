from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django08 import models


# Create your views here.
def index(request, pid=None, del_pass=None):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET['user_id']
        user_pass = request.GET['user_pass']
        user_post = request.GET['user_post']
        user_mood = request.GET['mood']
    except:
        user_id = None
        message = '如要张贴信息，则每一个字段都要填...'
    if del_pass and pid:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "数据删除成功"
            else:
                message = "密码错误"
    elif user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post.objects.create(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = '成功保存！请记得你的编辑密码[{}]!，信息需经审查后才会显示。'.format(user_pass)
    test = [0,1,2,3]
    return render(request, 'django08/index.html', locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:150]
    moods = models.Mood.objects.all()
    return render(request, 'django08/listing.html', locals())

def posting(request):
    moods = models.Mood.objects.all()
    message = '如要张贴信息，则每一个字段都要填...'
    return render(request, 'django08/posting.html', locals())


