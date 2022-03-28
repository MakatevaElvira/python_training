from sys import maxsize

from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    added_contact = Contact(
        name="Elvirochka",
        middle_name="Heder1",
        last_name ="Familia",
        company="Footer1",
        home_phone="+79000",
        email="mai@mail.ru")
    app.contact.create(added_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)+1 == len(new_contacts)
    old_contacts.append(added_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts,key=Contact.id_or_max)
