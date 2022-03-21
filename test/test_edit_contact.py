from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(name="Precondition name"))
    app.contact.edit_first(Contact(
        name="Elvira Edited",
        middle_name="middle_name edited",
        company="company Edited",
        home_phone="+7900033",
        email="mai@mail.ru"))
