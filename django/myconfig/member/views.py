from django.shortcuts import render
from .models import Member
from django.contrib.auth.hashers import make_password


# Create your views here.
def list(request):
    mlist = Member.objects.all()
    temp = {'ml':mlist}
    return render(request, 'member/list.html', temp)


def insert(request):
    if request.method == 'GET':
        return render(request, 'member/insert.html')
    elif request.method == 'POST':
        # DB에 넣어라
        username = request.POST['username']
        pw = request.POST['pw']
        repw = request.POST['repw']
        hp = request.POST['hp']
        name = request.POST['name']
        msg = {}  # return은 딕셔너리로
        if pw != repw:
            msg['err'] = "비밀번호를 정확히 입력하세요"
        elif not (username and pw and hp and name):
            msg['err'] = '모든 값을 입력하세요'
        else :
            m = Member(
                username=username,
                pw=make_password(pw),
                hp=hp,
                name=name
            )
            m.save()
        return render(request, 'member/insert.html', msg)