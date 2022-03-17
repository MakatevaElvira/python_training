# -*- coding: utf-8 -*-
from fixture.application import Application
from model.group import Group
import pytest


@pytest.fixture()
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="Grop1", header="Heder1", footer="Footer1"))
    app.session.logout()