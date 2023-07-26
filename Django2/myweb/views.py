from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# 요청을 처리하는 함수의 매개변수는 request
# request 객체 안에는 클라이언트에 대한 정보가 저장되어 있음
def index(request):
    print(request.COOKIES)
    # HttpResponse를 작성하고 안에 태그를 넣어주면 html 출력
    return HttpResponse("<h1 style = 'color:green;'> Hello! </h1>")

# 요청이 오면 tmeplates 디렉토리의 test.html 을 출력
def testhtml(request):
    return render(request, "test.html")

def template(request):
    age = 25
    personData = {"name" : "bob", "addr" : "seoul"}
    data = ['1', '2', '3', 'kim', 'sa']
    # html에 데이터를 전송하고자 하면
    # 세번째 매개변수에 dict를 만들어서
    # 데이터 이름과 데이터를 기재할 수 있음
    # 여기서는 msg, person 이라는 이름으로 데이터를 보냄
    return render(request, "template.html", {"age" : age, "data" : data})