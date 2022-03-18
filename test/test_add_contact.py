from model.contact import Contact



def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(
        name="Elvira",
        middle_name="Heder1",
        company="Footer1",
        home_phone="+79000",
        email="mai@mail.ru"))
    app.session.logout()
