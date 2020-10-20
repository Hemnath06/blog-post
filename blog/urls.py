from django.urls import path
from .views import HomeView, EntryView, CreateEntryView, AddCommentView

urlpatterns = [
    path('', HomeView.as_view(), name="blog-home" ),
    path('entry/<int:pk>/', EntryView.as_view(), name= "entry-detail"),
    path('create_entry/', CreateEntryView.as_view(success_url='/'), name= "create_entry"),
    path('entry/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment")
]
