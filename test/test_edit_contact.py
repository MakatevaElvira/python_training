from model.contact import Contact


def test_edit_first_contact(app):
    old_contacts = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Precondition name"))
    edited_contact = Contact(
        name="Elvira Edited",
        middle_name="middle_name edited",
        last_name= "famil",
        company="company Edited",
        home_phone="+7900033",
        email="mai@mail.ru")
    edited_contact.id = old_contacts[0].id
    app.contact.edit_first(edited_contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts)  == len(new_contacts)
    old_contacts[0] = edited_contact
    assert sorted(old_contacts,key=Contact.id_or_max)== sorted(new_contacts,key=Contact.id_or_max)
