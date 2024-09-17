from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSetTests(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.notification_1 = Notification.objects.create(message="Test 1", read=False)
        self.notification_2 = Notification.objects.create(message="Test 2", read=True)

    def test_get_notifications(self):
        """
        Test retrieving notifications
        """
        url = reverse("notification-list")
        response = self.client.get(url)
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_mark_as_read(self):
        """
        Test marking a notification as read
        """
        url = reverse(
            "notification-mark-as-read", kwargs={"pk": self.notification_1.pk}
        )
        response = self.client.post(url)
        self.notification_1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.notification_1.read)

    def test_mark_all_as_read(self):
        """
        Test marking all notifications as read
        """
        url = reverse("notification-mark-all-as-read")
        response = self.client.post(
            url, {"notification_ids": [self.notification_1.id, self.notification_2.id]}
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.notification_1.refresh_from_db()
        self.notification_2.refresh_from_db()
        self.assertTrue(self.notification_1.read)
        self.assertTrue(self.notification_2.read)

    def test_soft_delete_notification(self):
        """
        Test soft deleting a notification
        """
        url = reverse("notification-soft-delete", kwargs={"pk": self.notification_1.pk})
        response = self.client.post(url)
        self.notification_1.refresh_from_db()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(self.notification_1.deleted)
