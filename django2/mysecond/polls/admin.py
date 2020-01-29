from django.contrib import admin
from .models import Question, Choice


#  한 화면에 입력하기
class ChoiceInline(admin.StackedInline):
    model = Choice
    # 한번에 보여지는 choice 갯수
    extra = 2


# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    # 필드 순서변경
    # fields = ['pub_date','question_text']
    # 필드 분리
    fieldsets = [(None,{'fields':['question_text']}),
                 # ('날짜',{'fields':['pub_date']})
                 # 필드 접기 'classes':['collapse']
                 ('날짜', {'fields': ['pub_date'], 'classes':['collapse']})
                 ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)


