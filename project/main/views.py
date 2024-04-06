from django.shortcuts import render

# Create your views here.

def mainpage(request):
    context = {
        'generation': 12,
        'members': ['현아', '영심이', '티준'],
        'info':{'weather': '좋음', 'feeling': '배고픔(?)', 'note': '아기사자 화이팅!'},
        'sessions':['장고는 MTV 패턴을 기반으로 한 프레임워크이다.', 'MTV 패턴에는 Model, Template, View가 있다.',
                   'Model은 데이터, View는 요청에 따른 적절한 로직 수행, Template은 인터페이스를 의미한다.']
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    return render(request, 'main/secondpage.html')