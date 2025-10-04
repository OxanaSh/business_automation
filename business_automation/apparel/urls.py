from django.urls import path, include
from . import views
from .views import LoginView

urlpatterns = [
    path('apparels/', views.ApparelView.as_view()),
    path('packs/', views.PackView.as_view()),
    path('apparels/<int:pk>', views.ApparelView.as_view()),
    path('get_apparels/', views.AllApparelList.as_view()),
    path('get_apparel_by_barcode/<str:barcode>', views.GetApparelByBarcode.as_view()),
    path('get_pack_by_barcode/<str:barcode>', views.GetPackByBarcode.as_view()),
    path('sell_apparel_by_barcode/<str:barcode>', views.SoldApparel.as_view()),
    path('sell_pack_by_barcode/<str:barcode>', views.SoldPack.as_view()),
    path('get_types/', views.TypeList.as_view()),
    path('get_sizes/', views.SizeList.as_view()),
    path('get_colours/', views.ColourList.as_view()),
    path('get_warehouses/', views.WarehouseList.as_view()),
    path('products/<slug:type_slug>/<slug:product_slug>/', views.ApparelType.as_view()),

    path('login/', LoginView.as_view()),
]