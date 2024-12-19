from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    categorylist = [
        (1, '질문 게시판'),
        (2, '자유 게시판'),
        (3, '토론 게시판'),
        (4, '공지 사항'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_question')
    subject = models.CharField(max_length = 200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')
    category = models.IntegerField(choices=categorylist, default=1)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True,
                                 on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
