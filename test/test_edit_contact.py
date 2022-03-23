from model.contact import Contact


def test_edit_first_contact(app):
    old_contact = app.contact.get_contact_list()
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Precondition name"))
    app.contact.edit_first(Contact(
        name="Elvira Edited",
        middle_name="middle_name edited",
        company="company Edited",
        home_phone="+7900033",
        email="mai@mail.ru"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)  == len(new_contact)
