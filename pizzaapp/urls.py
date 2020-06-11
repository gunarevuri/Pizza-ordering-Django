from django.contrib import admin
from django.urls import path,include
from .views import home , adminloginview, adminhomepage, adminauthenticateview, adminlogout, addpizza, deletepizza, homepageview, signupuser, userloginview, customerpage, userauthenticate, userlogout,placeorder, myorders, adminorders,acceptorder,declineorder


urlpatterns = [
#-----Admin URLS -------#
	path('admin/', adminloginview, name= 'adminloginview'),
	path('adminauthenticateview', adminauthenticateview, name= 'adminauthenticateview'),
	path('admin/homepage/', adminhomepage, name= 'adminhomepage'),
	path('adminlogout/', adminlogout, name='adminlogout'),
	path('addpizza/', addpizza, name='addpizza'),
	path('deletepizza/<int:id>/', deletepizza, name='deletepizza'),
	path('adminorders/', adminorders, name= 'adminorders'),
	path('acceptorder/<int:pk>/', acceptorder, name='acceptorder'),
	path('declineorder/<int:pk>/', declineorder, name='declineorder'),
#---------Customer URLS------------#
	path('', homepageview, name='homepageview'),
	path('signupuser/', signupuser, name="signupuser"),
	path('loginuser/', userloginview, name = 'userloginview'),
	path('userauthenticate/', userauthenticate, name= 'userauthenticate'),
	path('customer/welcome/', customerpage, name= 'customerpage'),
	path('userlogout/', userlogout, name='userlogout'),
	path('placeorder/', placeorder, name = 'placeorder'),
	path('myorders/', myorders, name= 'myorders'),
	]