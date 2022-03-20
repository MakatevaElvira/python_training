from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first(Contact(
        name="Elvira Edited",
        middle_name="middle_name edited",
        company="company Edited",
        home_phone="+7900033",
        email="mai@mail.ru"))
