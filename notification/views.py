from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination
from .models import Notification
from .serializers import NotificationSerializer


class NotificationPagination(PageNumberPagination):
    page_size = 10  # Customize based on your preference


class NotificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notification.objects.filter(
        deleted=False
    )  # Exclude soft-deleted notifications
    serializer_class = NotificationSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["read"]  # Allow filtering by 'read' status
    pagination_class = NotificationPagination

    @action(detail=True, methods=["post"])
    def mark_as_read(self, request, pk=None):
        notification = self.get_object()
        notification.mark_as_read()
        return Response(
            {"status": "Notification marked as read"}, status=status.HTTP_200_OK
        )

    @action(detail=False, methods=["post"])
    def mark_all_as_read(self, request):
        notification_ids = request.data.get("notification_ids", [])
        notifications = Notification.objects.filter(
            id__in=notification_ids, deleted=False
        )
        updated_count = notifications.update(read=True)
        return Response(
            {"status": f"{updated_count} notifications marked as read"},
            status=status.HTTP_200_OK,
        )

    @action(detail=True, methods=["post"])
    def soft_delete(self, request, pk=None):
        notification = self.get_object()
        notification.soft_delete()
        return Response(
            {"status": "Notification soft deleted"}, status=status.HTTP_200_OK
        )
