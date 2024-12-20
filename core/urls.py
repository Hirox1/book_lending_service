from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Define the schema view for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Book Lending Service API",
        default_version='v1',
        description="API documentation for the Book Lending Service",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Allow public access
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),  # Books app endpoints
    path('api/users/', include('users.urls')),  # Users app endpoints
    path('api/requests/', include('requests.urls')),  # Requests app endpoints
    path('api/auth/', include('authori.urls')),  # Include routes from the authori app (authentication)
    # JWT Authentication endpoints (if not handled by authori app)
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Swagger UI path
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
