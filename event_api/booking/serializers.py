

from booking.models import Booking
from rest_framework import serializers
class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model=Booking

        fields="__all__"

        read_only_fields=['user','status','amount','created_at']
    def validate(self,data):
        event=data['event']
        seats=data['seats']
        if event.available_seats<seats:

            raise serializers.ValidationError("seats are not  available")

        return data