from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SaleViewSet, NtabDetailView, ProfileView, SaleViewAdd, Sp_Accept_Amcom_PayView

router = DefaultRouter()
router.register('sales', SaleViewSet, basename='sales')

urlpatterns = [
    path("", include(router.urls)),
    path("ntab/<slug:ntab_slug>/", NtabDetailView.as_view()),
    path('profile/', ProfileView.as_view()),
    path("addsale/", SaleViewAdd.as_view()),
    path("viewsale/<slug:ntab_slug>/", SaleViewAdd.as_view()),
    path("spaccept/", Sp_Accept_Amcom_PayView),
    
]