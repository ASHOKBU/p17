from django.urls import path
app_name='myapp'
from myapp import views
urlpatterns=[
    path('builtin/',views.builtin,name='builtin'),
]
from django.conf import settings
from  django.conf.urls.static import static
if settings.DEBUG == True:
    urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)