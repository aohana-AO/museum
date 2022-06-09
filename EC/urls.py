from urllib.parse import urlparse
from django.urls import path
from EC import views
urlpatterns = [
    path('EC/',views.IView.as_view(),name='EC'),
    path('product/<int:pk>',views.ItemDetailView.as_view(),name='product'),
    path('additem/<int:pk>',views.addItem,name='additem'),
    path('order/',views.OrderView.as_view(),name='order'),
    path('removeitem/<int:pk>',views.removeItem,name='removeitem'),
    path('removesingleitem/<int:pk>',views.removesingleItem,name='removesingleitem'),
    path('payment/',views.PaymentView.as_view(),name='payment'),
    path('thanks/',views.ThanksView.as_view(),name='thanks'),

    
]
