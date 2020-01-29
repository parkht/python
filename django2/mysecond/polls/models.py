from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=100)  # 좋아하는 색은?
    pub_date = models.DateTimeField('date published')
    # table의 이름을 변경
    class Meta:
        db_table='question'
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
