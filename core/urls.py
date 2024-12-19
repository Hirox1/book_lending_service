from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view  # Ensure correct import
from drf_yasg import openapi
from rest_framework import permissions

# Define the schema view for Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="Book Lending Service API",
        default_version='v1',
        description="API documentation for the Book Lending Service",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],  # Corrected to use a list
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', include('books.urls')),  # Correct API path for books
    path('api/users/', include('users.urls')),  # Correct API path for users
    path('api/requests/', include('requests.urls')),  # Correct API path for requests
    # Swagger UI path
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
