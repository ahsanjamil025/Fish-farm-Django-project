from django.urls import path
from fishfarm import views


urlpatterns = [
    path('', views.index , name='index'),
     path('ehome', views.eindex , name='ehome'),
    path('signin', views.signin , name='signin'),
    path('signup', views.signup , name='signup'),
    path('index/', views.index , name='index'),
    path('about/', views.about , name='about'),
    path('contact', views.contact , name='contact'),
    path('feedback/', views.feedback , name='feedback'),
    path('sell/', views.sell, name='sell'),
    path('order/', views.order, name='order'),

    path('Setting', views.Settings, name='Setting'),
    path('password', views.password, name='password'),
    path('contactsetting', views.cSettings, name='contactsetting'),

   
    
    

    path('edit/<str:pk>', views.edit , name='edit'),
    path('product/<str:pk>', views.promang , name='product'),
    path('delete/<str:pk>', views.delete, name='delete'),
    path('logout', views.Logouts , name='logout'),

    
    
    #------cart funcation
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    #...... buy
    path('store', views.store, name='store'),
    #...... del
    path('cart/deletecartitem/<int:id>',views.deletecartitem,name='deletecartitem'),
]