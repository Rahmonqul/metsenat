from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Swagger
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="API with Bearer Token",
        default_version='v1',
        description="API с поддержкой Bearer токенов (JWT)",
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('api/', include('students.urls')),
    path('api/', include('sponsor.urls')),
    path('api/', include('sponsorship.urls')),

    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
