from rest_framework import generics  # <- import generics
from .models import Event  # <- don't forget your models
from .serializers import EventSerializer  # <- or serializers
from rest_framework import permissions
from events.permissions import IsOwnerOrReadOnly


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsOwnerOrReadOnly]