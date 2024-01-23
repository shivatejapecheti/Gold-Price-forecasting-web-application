from django.urls import path
from . import views
# from goldpresentprice import views 
# from contactform import views

urlpatterns = [


    # path('', views.home, name="Home-Page"),
    
    path('', views.home, name="home"),
    path('information/', views.information, name="information"),
    path('gold-price/', views.gold_price, name="gold_price"),
    # path('gold-price/', views.gold_price, name="gold-price"),
    path('plots/', views.plots_view, name='plots'),


    path('', views.home, name="home"),
    path('gold-price/', views.gold_price, name="gold_price"),
    path('gold-price/home.html', views.home, name='gold_home'),


    path('set-cookie/', views.set_cookie, name="set_cookie"),  # Link to set_cookie function
    path('get-cookie/', views.get_cookie, name="get_cookie"),  # Link to get_cookie function


    path('set-user-timezone/', views.set_user_timezone, name="set_user_timezone"),
    path('get-user-timezone/', views.get_user_timezone, name="get_user_timezone"),

    path('info.html', views.info_page, name='info_page'),
    path('gold-price/', views.gold_price_view, name='gold_price_view'),


    # path('set-favorite-metrics/', views.set_favorite_metrics, name='set_favorite_metrics'),
    # path('get-favorite-metrics/', views.get_favorite_metrics, name='get_favorite_metrics'),
    # path('store-session-data/', views.store_session_data, name='store_session_data'),
    # path('get-session-data/', views.get_session_data, name='get_session_data'),

    # path('gold-present-price/', views.gold_present_price, name='gold_present_price'),
    
]