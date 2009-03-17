"""
A management command which deletes expired service tickets (e.g.,
from the database.

Calls ``ServiceTickets.objects.delete_expired_users()``, which
contains the actual logic for determining which accounts are deleted.

"""

from django.core.management.base import NoArgsCommand
from django.core.management.base import CommandError
from django.conf import settings

import datetime

from cas_provider.models import ServiceTicket

class Command(NoArgsCommand):
    help = "Delete expired service tickets from the database"

    def handle_noargs(self, **options):
        tickets = ServiceTicket.objects.all()
        for ticket in tickets:
            expiration = datetime.timedelta(minutes=settings.CAS_TICKET_EXPIRATION)
            if datetime.datetime.now() > ticket.created + expiration:
                print "Deleting %s..." % ticket.ticket
                ticket.delete()
            else:
                print "%s not expired..." % ticket.ticket