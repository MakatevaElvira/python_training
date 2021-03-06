from random import randrange

from model.contact import Contact


def test_delete_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Precondition name"))
    app.contact.delete_first()
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[0:1] = []
    assert old_contacts == new_contacts


def test_delete_some_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Precondition name"))
    index = randrange(len(old_contacts))
    app.contact.delete_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index + 1] = []
    assert old_contacts == new_contacts
