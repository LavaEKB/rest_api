from rest_framework import filters
from rest_framework import viewsets
from .serializers import SaleSerializer
from .models import Sale
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import generics, permissions
from .serializers import UserSerializer
from django.db import connection
from rest_framework.decorators import api_view, permission_classes

class SaleViewAdd(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        ntab_slug = self.kwargs['ntab_slug']
        return Sale.objects.filter(ntab=ntab_slug)

@api_view(['GET', 'POST']) 
@permission_classes((permissions.AllowAny,))
def Sp_Accept_Amcom_PayView(request):
    if request.method == 'GET':
        params = (777, 8888, 10, 1, 100, '01.01.2023',1,2)
        print(params)

        try:
            cursor = connection.cursor()
            cursor.execute("{CALL dbo.sp_accept_amcom_pay (%s, %s, %s, %s, %s, %s, %s, %s)}", params)
            cursor.cancel() 
        
        except Exception:
            print('Ошибка')
        return Response(status=500)

    if request.method == 'POST':
        params = (request.POST.get('fcard'), request.POST.get('ncard'), request.POST.get('amcom'),
                  request.POST.get('kassid'), request.POST.get('sum'), request.POST.get('data'),
                  request.POST.get('vid'), request.POST.get('kol'))
        print(params)
        try:
            cursor = connection.cursor()
            cursor.execute("{CALL dbo.sp_accept_amcom_pay (%s, %s, %s, %s, %s, %s, %s, %s)}", params)
            cursor.cancel() 
        
        except Exception:
            print('Ошибка')
        return Response(status=500)
    return Response(status=500)

class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    #ordering = 'id'

class NtabDetailView(generics.ListAPIView):
    serializer_class = SaleSerializer
    pagination_class = PageNumberSetPagination

    def get_queryset(self):
        ntab_slug = self.kwargs['ntab_slug']
        return Sale.objects.filter(ntab=ntab_slug)

class SaleViewSet(viewsets.ModelViewSet):

    search_fields = ['ntab', 'sum_gp']
    filter_backends = (filters.SearchFilter,)

    serializer_class = SaleSerializer
    queryset = Sale.objects.all().order_by('-id')
    lookup_field = 'id'
    pagination_class = PageNumberSetPagination
