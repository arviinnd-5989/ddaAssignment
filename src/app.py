from flask import Flask, request, jsonify
from event import get_events, create_event, get_event, update_event, delete_event
from organizer import get_organizers, create_organizer, get_organizer, update_organizer, delete_organizer
from vendor import get_vendors, create_vendor, get_vendor, update_vendor, delete_vendor
from attendee import get_attendees, create_attendee, get_attendee, update_attendee, delete_attendee
from attendeephno import get_attendeesphno, create_attendeephno, get_attendeephno, update_attendeephno, delete_attendeephno
from venue import get_venues, create_venue, get_venue, update_venue, delete_venue
from registration import get_registrations, create_registration, get_registration, update_registration, delete_registration
from agreement import get_agreements, create_agreement, get_agreement, update_agreement, delete_agreement
from attendedby import get_attendedbys , create_attendedby, get_attendedby, update_attendedby, delete_attendedby

app = Flask(__name__)

# URLs for event table
app.add_url_rule('/events', methods=['GET'], view_func=get_events)
app.add_url_rule('/events', methods=['POST'], view_func=create_event)
app.add_url_rule('/events/<event_id>', methods=['GET'], view_func=get_event)
app.add_url_rule('/events/<event_id>', methods=['PUT'], view_func=update_event)
app.add_url_rule('/events/<event_id>', methods=['DELETE'], view_func=delete_event)

# URLs for organizer table
app.add_url_rule('/organizers', methods=['GET'], view_func=get_organizers)
app.add_url_rule('/organizers', methods=['POST'], view_func=create_organizer)
app.add_url_rule('/organizers/<organizer_id>', methods=['GET'], view_func=get_organizer)
app.add_url_rule('/organizers/<organizer_id>', methods=['PUT'], view_func=update_organizer)
app.add_url_rule('/organizers/<organizer_id>', methods=['DELETE'], view_func=delete_organizer)

# URLs for vendor table
app.add_url_rule('/vendors', methods=['GET'], view_func=get_vendors)
app.add_url_rule('/vendors', methods=['POST'], view_func=create_vendor)
app.add_url_rule('/vendors/<vendor_id>', methods=['GET'], view_func=get_vendor)
app.add_url_rule('/vendors/<vendor_id>', methods=['PUT'], view_func=update_vendor)
app.add_url_rule('/vendors/<vendor_id>', methods=['DELETE'], view_func=delete_vendor)

# URLs for attendee table
app.add_url_rule('/attendees', methods=['GET'], view_func=get_attendees)
app.add_url_rule('/attendees', methods=['POST'], view_func=create_attendee)
app.add_url_rule('/attendees/<attendee_id>', methods=['GET'], view_func=get_attendee)
app.add_url_rule('/attendees/<attendee_id>', methods=['PUT'], view_func=update_attendee)
app.add_url_rule('/attendees/<attendee_id>', methods=['DELETE'], view_func=delete_attendee)

# URLs for attendee phone number table
app.add_url_rule('/attendeesphno', methods=['GET'], view_func=get_attendeesphno)
app.add_url_rule('/attendeesphno', methods=['POST'], view_func=create_attendeephno)
app.add_url_rule('/attendeesphno/<attendee_id>', methods=['GET'], view_func=get_attendeephno)
app.add_url_rule('/attendeesphno/<attendee_id>', methods=['PUT'], view_func=update_attendeephno)
app.add_url_rule('/attendeesphno/<attendee_id>', methods=['DELETE'], view_func=delete_attendeephno)

# URLs for venue table
app.add_url_rule('/venues', methods=['GET'], view_func=get_venues)
app.add_url_rule('/venues', methods=['POST'], view_func=create_venue)
app.add_url_rule('/venues/<venue_id>', methods=['GET'], view_func=get_venue)
app.add_url_rule('/venues/<venue_id>', methods=['PUT'], view_func=update_venue)
app.add_url_rule('/venues/<venue_id>', methods=['DELETE'], view_func=delete_venue)

# URLs for registration table
app.add_url_rule('/registrations', methods=['GET'], view_func=get_registrations)
app.add_url_rule('/registrations', methods=['POST'], view_func=create_registration)
app.add_url_rule('/registrations/<registration_id>', methods=['GET'], view_func=get_registration)
app.add_url_rule('/registrations/<registration_id>', methods=['PUT'], view_func=update_registration)
app.add_url_rule('/registrations/<registration_id>', methods=['DELETE'], view_func=delete_registration)

# URLs for agreement table
app.add_url_rule('/agreements', methods=['GET'], view_func=get_agreements)
app.add_url_rule('/agreements', methods=['POST'], view_func=create_agreement)
app.add_url_rule('/agreements/<vendor_id>/<organizer_id>', methods=['GET'], view_func=get_agreement)
app.add_url_rule('/agreements/<vendor_id>/<organizer_id>', methods=['PUT'], view_func=update_agreement)
app.add_url_rule('/agreements/<vendor_id>/<organizer_id>', methods=['DELETE'], view_func=delete_agreement)

# URLs for agreement table
app.add_url_rule('/attendedbys', methods=['GET'], view_func=get_attendedbys)
app.add_url_rule('/attendedbys', methods=['POST'], view_func=create_attendedby)
app.add_url_rule('/attendedbys/<event_id>/<attendee_id>', methods=['GET'], view_func=get_attendedby)
app.add_url_rule('/attendedbys/<event_id>/<attendee_id>', methods=['PUT'], view_func=update_attendedby)
app.add_url_rule('/attendedbys/<event_id>/<attendee_id>', methods=['DELETE'], view_func=delete_attendedby)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port='5000',debug=True)