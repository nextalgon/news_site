from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from mainApp.views import TopicView, TeamPage


urlpatterns = [
    path("", views.index, name="index"),
    path("topic/<int:pk>/", TopicView.as_view(), name='davomi'),
    path('category/<int:category_id>/', views.category, name="category"),
    path('team/', TeamPage.as_view(), name='team')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)