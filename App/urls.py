from django.conf.urls import url

from App import views

urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^mine/', views.mine, name='mine'),
    url(r'^market/(\d+)/(\d+)/(\d+)/', views.market, name='market'),
    url(r'^user/', views.user, name='user'),
    url(r'^checkaccount/', views.checkAccount, name='checkaccount'),
    url(r'^createaccount/', views.createAccount, name='createaccount'),
    url(r'^login/', views.login, name='login'),
    url(r'^dologin/', views.doLogin, name='dologin'),
]
