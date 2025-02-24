from django.urls import path

from .views import EventListCreateView, EventRetrieveUpdateDestroyView, EventRegistrationView

urlpatterns = [
    path("events/", EventListCreateView.as_view(), name="event-list-create"),
    path("events/<int:pk>/", EventRetrieveUpdateDestroyView.as_view(), name="event-detail"),
    path("event-registration/", EventRegistrationView.as_view(), name="event-registration"),
]
