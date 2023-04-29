from django.urls import path
from django.urls import path,include
import app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app1/',include('app1.urls')),
    
]