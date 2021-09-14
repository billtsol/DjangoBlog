from django.urls import path
from .views import Home  ,posts,postView,Contact,AboutUs,logOutUser ,categoryView , logInView,registerView

urlpatterns = [
    path('', Home , name='Home'),
    path('posts/', posts , name='posts'),
    path('post/<id>/', postView , name='postView'),
    path('contact/', Contact , name='Contact'),
    path('aboutUs/', AboutUs , name='AboutUs'),
    path('posts/tag/<name>', categoryView , name='categoryView'),
    path('login/', logInView , name='Login'),
    path('register/', registerView , name='Register'),
    path('logOutUser/', logOutUser , name='logOutUser'),
]