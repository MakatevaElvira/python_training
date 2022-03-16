import pytest

from application import Application
from contact import Contact

@pytest.fixture()
def app(request):
    fixture = Application()
    #request.addfinalizer(fixture.destroy())
    return fixture

def test_add_contact(app):
        app.login(username="admin", password="secret")
        app.create_contact(Contact(
            name="Elvira",
            middle_name="Heder1",
            company="Footer1",
            home_phone="+79000",
            email="mai@mail.ru"))
        app.logout()
