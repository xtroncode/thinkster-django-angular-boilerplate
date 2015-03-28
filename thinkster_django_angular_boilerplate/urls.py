from django.conf.urls import patterns, url, include

from thinkster_django_angular_boilerplate.views import IndexView

from rest_framework import routers

from authentication.views import AccountViewSet

router = routers.SimpleRouter()
router.register(r'accounts',AccountViewSet)


urlpatterns = patterns(
    '',
    url(r'^api/v1/',include(router.urls)),
  url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^.*$', IndexView.as_view(), name='index'),
)
