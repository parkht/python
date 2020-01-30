from django.shortcuts import render
from .models import Member
from django.contrib.auth.hashers import make_password
from django.shortcuts import get_object_or_404


def detail(request, member_id):
    # member = Member.objects.get(id=member_id)
    member = get_object_or_404(Member, pk=member_id)
    return render(request, 'member/detail.html', {'m': member})


def list(request):
    members = Member.objects.all()
    return render(request, 'member/list.html', {'ms': members})

# Create your views here.
def index(request):
    fruit = {'names': ['애플망고', '사각수박', '멜론'],
             'colors': ['red', 'blue', 'white', 'green'],
             'number': [1, 2, 3, 4, 5]}
    return render(request, 'member/index.html', fruit)

# render(request, 템플릿명[사전형객체]
# 템플릿변수 {{변수}}
# 템플릿태그 {% 태그 %}
# 템플릿필터 |
def insert(request):
    if request.method == 'GET':
        return render(request, 'member/insert.html')
    elif request.method == 'POST':
        # DB에 넣어라
        username = request.POST['username']
        pw = request.POST['pw']
        repw = request.POST['repw']
        hp = request.POST['hp']
        email = request.POST['email']
        name = request.POST['name']
        msg = {}  # return은 딕셔너리로
        if pw != repw:
            msg['err'] = "비밀번호를 정확히 입력하세요"
        elif not (username and pw and repw and email and hp and name):
            msg['err'] = '모든 값을 입력하세요'
        else :
            m = Member(
                    username=username,
                    pw=make_password(pw),
                    hp=hp,
                    email=email,
                    name=name
                    )
            m.save()
        return render(request, 'member/insert.html', msg)