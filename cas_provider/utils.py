from random import Random
import string

from models import ServiceTicket, LoginTicket

def _generate_string(length=8, chars=string.letters + string.digits):
    """ Generates a random string of the requested length. Used for creation of tickets. """
    return ''.join(Random().sample(string.letters+string.digits, length))

def create_service_ticket(user, service):
    """ Creates a new service ticket for the specified user and service.
        Uses _generate_string.
    """
    ticket_string = 'ST-' + _generate_string(29) # Total ticket length = 29 + 3 = 32
    ticket = ServiceTicket(service=service, user=user, ticket=ticket_string)
    ticket.save()
    return ticket

def create_login_ticket():
    """ Creates a new login ticket for the login form. Uses _generate_string. """
    ticket_string = 'LT-' + _generate_string(29)
    ticket = LoginTicket(ticket=ticket_string)
    ticket.save()
    return ticket_string