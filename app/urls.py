from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('predictor', views.predictor, name='predictor'),
    path('crop_result', views.formInfo, name='crop_result'),
    path('plantde', views.plantde, name='plantde'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
   path('fert_recommend',views.fert_recommend,name='fert_recommend'),
    path('recommendation',views.fert_recommend,name='recommendation'),

]
