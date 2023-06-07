from rest_framework import filters
from rest_framework import viewsets
from .serializers import SaleSerializer
from .models import Sale
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework import generics, permissions
from .serializers import UserSerializer

class SaleViewAdd(generics.ListCreateAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        ntab_slug = self.kwargs['ntab_slug']
        return Sale.objects.filter(ntab=ntab_slug)

class ProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args,  **kwargs):
        return Response({
            "user": UserSerializer(request.user, context=self.get_serializer_context()).data,
        })


class PageNumberSetPagination(pagination.PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    #ordering = 'sum_gp'

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
    queryset = Sale.objects.all().order_by('sum_gp')
    lookup_field = 'id'
    pagination_class = PageNumberSetPagination