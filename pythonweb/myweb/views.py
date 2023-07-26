from django.shortcuts import render

# Create your views here.

# 모델 클래스를 import
from myweb.models import Item

def index(request):
    # 전체 데이터 가져오기
    data = Item.objects.all()
    lemondata = Item.objects.filter(itemname = '레몬')

    return render(request, "index.html", {"data" : data, "lemondata" : lemondata})

# 주소 뒤에 이름이 사용될 때는 그 이름(itemid)을 그대로 사용해줘야 함
# url 뒤에 붙은 패러미터는 2번째 매개변수를 이용해서 가져옴
def detail(request, itemid):
    item = Item.objects.get(itemid = itemid)

    return render(request, 'detail.html', {'item': item})
