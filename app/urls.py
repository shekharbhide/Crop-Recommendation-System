from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="home"),
    path('predictor', views.predictor, name='predictor'),
    path('crop_result', views.formInfo, name='crop_result'),
    path('plantde', views.plantde, name='plantde')

]
