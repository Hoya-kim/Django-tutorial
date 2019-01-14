from django.db import models
from django.utils import timezone


class Post(models.Model):  # models은 Post가 장고 모델임을 의미. 이 코드 때문에 장고는 Post가 DB에 저장되어야 한다고 알게 됨.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)  # ForeignKey : 다른 모델에 대한 링크를 의미.
    title = models.CharField(max_length=200)  # CharField : 글자 수가 제한된 텍스트를 정의할 때 사용. 글 제목같이 짧은 문자열 정보를 저장할 때 사용.
    text = models.TextField()  # TextField : 글자 수에 제한이 없는 긴 텍스트를 위한 속성.
    created_date = models.DateTimeField(  # DateTimeField : 날짜와 시간을 의미
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
