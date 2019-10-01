from django.urls import path,include
from mvp import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('mvp1/', views.UserCreate.as_view()),
]
