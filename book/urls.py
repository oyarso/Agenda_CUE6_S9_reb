from django.urls import path
from .views import IndexPageView, menuView,logout_view, login_view, mostrar, datosform_view, widget_view, boardsform_view, registro_view

urlpatterns = [ 
path('', IndexPageView.as_view(), name='index'), 
path('menu/',  menuView, name='menu'),     
path('book/', mostrar, name='book'),

path('login/', login_view, name="login"), 
path('mostrar/',  mostrar, name='mostrar'), 
path('datosform/',  datosform_view, name='datos_form'), 
path('widgetform/',  widget_view, name='widgetform'), 
path('boardsform/',  boardsform_view, name='boardsform'),  
path('registro/', registro_view, name="registro"),    
path('inputbook/', widget_view, name='widgetform'), 
path('logout/', logout_view, name="logout"), 
]


