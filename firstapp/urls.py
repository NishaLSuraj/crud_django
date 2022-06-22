from django.urls import path
from firstapp import views

urlpatterns = [
    
    path('',views.home),
    path('update/<int:todo_id>/',views.update,name="update"),
]
