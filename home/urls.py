from django.urls import path
from home import views

app_name = "market"
urlpatterns = [
    path("", views.index, name="home"),
    path("create/", views.create_post),
    path("view/<int:post_id>/", views.view_post),
    path("update/<int:post_id>/", views.update_post),
    path("delete/<int:post_id>", views.delete_post)
]