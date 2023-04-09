from django.shortcuts import render
from rest_framework.views import APIView
import os
# from rest_framework.permissions import IsAuthenticated <=권한 추가 시 사용
"""
* APIView : 
기존에는 Django Rest Framework(DRF)에서 제공하는 "@api_view"데코레이터를 사용해서 Django view를 RESTful API view로 변환하였는데,
아래는 APIView를 사용해서 클래스로 view를 관리했다.
APIView를 사용해서 view를 구성할 경우 각 method를 함수단위로 나눠서 관리할 수 있기 떄문에 좀 더 깔끔하고 간결한 코드를 구성할 수 있고,
해당 view에 접근할 수 있는 권한을 쉽게 제한할 수 있다. 

* Templates
settings 파일에서 'TEMPLATES'의 'DIRS'에 templates 경로를 지정해놓으면, 아래와 같이 app/main.html과 같이 template경로를 바로 연결해서
찾을 수 있다.
"""

class Main(APIView):
    # permission_classes = [IsAuthenticated] -> [IsAuthenticated] : 권한정보
    def get(self, request):
        return render(request, 'app/main.html')
        #Django view에서 HTML 템플릿을 반환하려면 render 함수를 사용해야 한다.

"""
Django에서 'render()' 함수를 사용하면, 기본적으로 'settings.py'파일의 'TEMPLATES'설정을 참조한다.

1) 'APP_DIRS' : 
    첫번째, 'True'로 설정하면, 각 앱의 'templates'폴더를 찾아 템플릿 파일을 검색한다. 
    이 경우, 각 앱의 디렉토리에 'templates'폴더를 만들어 템플릿 파일을 저장하고 이를 인식해 랜더링한다.
    두번째, 'False'로 설정하면 root directory또는 중앙 집중식 디렉토리에 위치한 templates을 찾아 랜더링 한다.
2) 'DIRS' : 프로젝트 전체에서 사용되는 템플릿 파일을 저장할 수 있는 추가적인 디렉토리를 지정한다. 이 경우 지정된 경로에 있는 템플릿 파일이 사용된다.

즉, render() 함수를 호출할 떄, Django는 가장 먼저 'DIRS'에 지정된 경로를 검색하고, 그 다음 'APP_DIRS'를 통해 각 앱의 templates폴더를
검색한다. 이 과정에서 템플릿 파일을 찾으면, 해당 파일을 사용해 랜더링한다.
"""