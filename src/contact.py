from datacatalogtordf import Contact

def get_contact():
    contact = Contact()
    contact.identifier = "kollektivdata@entur.org"
    contact.name = {'en': 'Entur'}
    contact.email = "kollektivdata@entur.org"
    return contact
