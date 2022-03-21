# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="Grop1", header="Heder1", footer="Footer1"))
    

def test_add_group2(app):
    app.group.create(Group(name="Grop2", header="Heder1", footer="Footer1"))
