# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from account.views import (
    AccountViewSet,
    CreateAccountView,
    OwnerAPIView
)

from category.views import CategoryViewSet
from service.views import ServiceViewSet
from order.views import OrderViewSet
from comment_to.views import CommentViewSet

router = routers.DefaultRouter()
router.register(r"accounts", AccountViewSet, base_name='account')
router.register(r"services", ServiceViewSet, base_name='service')
router.register(r"categories", CategoryViewSet, base_name='category')
router.register(r"orders", OrderViewSet, base_name='order')
router.register(r"comments", CommentViewSet, base_name='comment')

v1_patterns = [
    url(r'^auth/', obtain_jwt_token),
    url(r'^register/', CreateAccountView.as_view()),
    url(r'^me/$', OwnerAPIView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls'))
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(v1_patterns, namespace='v1')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
