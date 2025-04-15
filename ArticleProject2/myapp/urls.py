from django.urls import path
from myapp import views

urlpatterns=[
    path('form/',views.form_view,name='form'),
    path('article/',views.article_view,name='article'),
    path('specific/<int:id>',views.specific_view,name='specific')
]