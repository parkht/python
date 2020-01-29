from django.shortcuts import render
from .models import Question


# Create your views here. (java = controller)
def index(request):
    return render(request,'polls/index.html')


def test(request):
    # 삽입 : save()
    # q = Question(question_text='좋아하는 색은', pub_date='2020-01-27')
    # q.save()  #  저장
    #
    # q = Question(question_text='좋아하는 음식은', pub_date='2020-01-27')
    # q.save()
    #
    # q = Question(question_text='좋아하는 만화는', pub_date='2020-01-27')
    # q.save()
    #
    # q = Question(question_text='좋아하는 색깔은', pub_date='2020-01-27')
    # q.save()

    # 수정 : save(), id = ''가 입력이 되면 수정이 된다.
    # q = Question(id=5, question_text='좋아하는 만화는', pub_date='2020-01-28')
    # q.save()

    # 조회
    # qlist = Question.objects.all()
    # qlist = Question.objects.all().order_by('-id')  # -는 역순으로 정렬
    # print(type(qlist))
    # for q in qlist:
    #     print(q.question_text, q.pub_date)

    # 삭제
    # q = Question.objects.get(id=2)
    # q.delete()

    return render(request, 'polls/test.html')


def insert(request):
    q = Question(question_text='가고 싶은 곳은?', pub_date='2020-01-28')
    q.save()
    return render(request, 'polls/insert.html')


def list(request):
    qlist = Question.objects.all()
    temp = {'qs' : qlist}
    return render(request, 'polls/list.html', temp)