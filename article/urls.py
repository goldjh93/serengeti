from django.urls import path
from .views import new, detail, edit, destroy, new_comment, create_comment, like, commentlike

app_name = 'article'

urlpatterns = [
    path("new/", new, name="new"),
    path("<int:id>", detail, name="detail"),
    path("edit/<int:id>", edit, name="edit"),
    path("destroy/<int:id>", destroy, name="destroy"),
    path("new_comments/<int:id>", new_comment, name="new_comment"),
    path("create/<int:id>", create_comment, name="create_comment"),
    path("like/<int:id>", like, name="likes"),
    path("comments/<int:id>/likes", commentlike, name="commentlikes"), 
]