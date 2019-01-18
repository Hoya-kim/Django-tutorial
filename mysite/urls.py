"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
"""
정규표현식(Regex)
Regular expressions의 줄임말
패턴
^ : 문자열이 시작할 때
$ : 문자열이 끝날 때
\d : 숫자
() : 패턴의 부분을 저장할 떄

ex) 예를 들어 http://www.mysite.com/post/12345/ 라는 url이 있다고 하자. 여기서 12345는 post 번호.
뷰마다 모든 글 번호를 일일이 매기는 것은 번거로우므로 정규식으로 url패턴을 만들어 아래와 가팅 매칭시킬 수 있다.
->  ^post/(\d+)/$
 - ^post/ : url이(오른쪽부터) post/로 시작한다.
 - (\d+) : 숫자(한 개 이상)가 있다. 이 숫자로 조회하고 싶은 게시글을 찾을 수 있다.
 - / : /뒤에 문자가 있다.
 - $ : url 마지막이 / 로 끝난다.
 
python에서 정규 표현식을 작성할 때는 항상 문자열 앞에 "r"을 붙인다.
이는 python에게 문자열에 특수 문자가 있음을 알려준다.
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')), # 쟝고는 http://127.0.0.1:8000/으로 들어오는 모든 접속 요청을 blog.urls로 전송해 추가 명령을 찾을 것이다.
]
