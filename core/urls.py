from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view  
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="SereXon",
        default_version="v1",
        description="SereXon-endpoint (API) Project",
        contact=openapi.Contact(email="mwombekilubere@gmail.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/vendor/", include("vendor.api.urls")),
    path(
        "drf-api/docs",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]