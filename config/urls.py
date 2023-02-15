from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeView

urlpatterns = [
    path('custom-admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
    path('account/', include('mysite.account.urls',namespace = 'account')),
    path('company/', include('mysite.company.urls',namespace = 'company')),
    path('order/', include('mysite.order.urls',namespace = 'order')),
    path('comment/', include('mysite.comment.urls',namespace = 'comment')),
    path('project/', include('mysite.project.urls',namespace = 'project')),
    path('',include('django.contrib.auth.urls'))
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
