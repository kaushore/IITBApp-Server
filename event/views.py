from django.shortcuts import render

# Create your views here.
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from models import Event, EventLike, EventViews
from rest_framework.decorators import list_route, detail_route
from serializers import EventReadSerializer, EventWriteSerializer, EventLikeSerializer, EventViewSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST

class EventPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 50

class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    pagination_class = EventPagination

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return EventWriteSerializer
        else:
            return EventReadSerializer

    @list_route(methods=['POST'])
    def like(self, request):
        serializer = EventLikeSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.data['event']
            user = serializer.data['user']
            event_like, created = EventLike.objects.get_or_create(event__id=event, user__id=user, defaults={'event_id' : event, 'user_id': user})
            return Response(EventLikeSerializer(event_like).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @list_route(methods=['POST'])
    def dislike(self, request):
        serializer = EventLikeSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.data['event']
            user = serializer.data['user']
            EventLike.objects.all().filter(event=event).filter(user=user).delete()
            return Response({'status': 'deleted'})
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    @list_route(methods=['POST'])
    def view(self, request):
        serializer = EventViewSerializer(data=request.data)
        if serializer.is_valid():
            event = serializer.data['event']
            user = serializer.data['user']
            event_view, created = EventViews.objects.get_or_create(event__id=event, user_id=user, defaults={'event_id' : event, 'user_id': user})
            return Response(EventViewSerializer(event_view).data)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)