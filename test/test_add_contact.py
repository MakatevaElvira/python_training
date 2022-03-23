from model.contact import Contact



def test_add_contact(app):
    old_contact = app.contact.get_contact_list()
    app.contact.create(Contact(
        name="Elvira",
        middle_name="Heder1",
        company="Footer1",
        home_phone="+79000",
        email="mai@mail.ru"))
    new_contact = app.contact.get_contact_list()
    assert len(old_contact)+1 == len(new_contact)
