


from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
import uuid
from booking.models import Booking
@receiver(post_save,sender=Booking)
def update_after_status_changes(sender,instance,created,**kwrgs):


    #create ticket code after successfull payment
    if instance.status == "confirmed" and not(instance.ticket_code):

        print("hello")
        code=f"TICK-{uuid.uuid4().hex[:8]}"
        print(code)
        instance.ticket_code=code
        print(instance.ticket_code)

        instance.save(update_fields=['ticket_code'])


        #to decrease available seats count

        event=instance.event

        event.available_seats-=instance.seats

        event.save(update_fields=['available_seats'])

    #restores seats after cancellation
    elif instance.status == "cancelled":

        if instance.ticket_code:

            event=instance.event

            event.available_seats += instance.seats

            event.save(update_fields=['available_seats'])

            instance.ticket_code=""

            instance.save(update_fields=['ticket_code'])


#restores seats after deletion
@receiver(post_delete,sender=Booking)
def update_seats_after_deletion(sender,instance,**kwargs):

    if instance.status =="confirmed" and instance.ticket_code:
        event = instance.event

        event.available_seats += instance.seats

        event.save(update_fields=['available_seats'])







