from django.urls import path
from myapp import views

urlpatterns=[
    path('form/',views.form_view,name='form'),
    path('display/',views.display_view, name='articles'),
    path('specific/<int:id>',views.display_specific_view,name='specific')
]