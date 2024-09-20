from django.urls import path

from users.api.views import ObtainTokenPairView, UserAPI

urlpatterns = [
    path('login', ObtainTokenPairView.as_view()),
    path('register', UserAPI.as_view({'post': 'create'})),
    path('telegram', UserAPI.as_view({'post': 'create'}))
]
