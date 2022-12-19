
from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path("get_all_products/",ProductMainModelView.as_view()),
    path("post_products/",ProductMainModelView.as_view()),

    path("add_colour/",ProductColourModelView.as_view()),
    path("view_colour/",ProductColourModelView.as_view()),

    path("add_img/",ProductImageModelView.as_view()),
    path("view_img/",ProductImageModelView.as_view()),

    path("view_one/",One_ProductDetailedView.as_view()),


 ]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
