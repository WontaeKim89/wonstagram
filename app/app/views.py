from django.shortcuts import render
from rest_framework.views import APIView
# from rest_framework.permissions import IsAuthenticated <=권한 추가 시 사용
"""
기존에는 Django Rest Framework(DRF)에서 제공하는 "@api_view"데코레이터를 사용해서 Django view를 RESTful API view로 변환하였는데,
아래는 APIView를 사용해서 클래스로 view를 관리했다.
APIView를 사용해서 view를 구성할 경우 각 method를 함수단위로 나눠서 관리할 수 있기 떄문에 좀 더 깔끔하고 간결한 코드를 구성할 수 있고,
해당 view에 접근할 수 있는 권한을 쉽게 제한할 수 있다. 
"""

class Main(APIView):
    # permission_classes = [IsAuthenticated] -> [IsAuthenticated] : 권한정보
    def get(self, request):
        return render(request, 'wonstagram/app/templates/app/main.html')
        #Django view에서 HTML 템플릿을 반환하려면 render 함수를 사용해야 한다.