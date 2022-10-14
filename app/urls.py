from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordResetForm, MySetPasswordForm
from django.conf.urls.i18n import i18n_patterns
from django.contrib.auth.models import User

app_name = "app"
# urls hado les urls marbotin b fnctn f view w dik fnct kima di (views.contact) hia li tjib page 
# html w had urls yretournii dik page b ism li raki baghyatah kima 'contact/'  'shop/'  'signup/'


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('delivery/', views.delivery, name='delivery'),
    path('privacy_policy/', views.privacy, name='privacy'),
    path('map/', views.map, name='map'),
    
    path('contact/', views.contact, name='contact'),
    path('shop-grid/', views.shop, name='shop'),
    path('signup/', views.CustomerRegistrationView.as_view(), name='signup'),
    # path('login/', views.loginuser, name='loginuser'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
                                                         authentication_form=LoginForm), name='loginuser'),
    path('logout/', auth_views.LogoutView.as_view(next_page='app:loginuser'), name='logoutuser'),
    path('profile/', views.userprofile, name='userprofile'),
    path('category/<str:type>/', views.category, name='category'),
    path('search/', views.search, name='search')
]
