# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Grop1", header="Heder1", footer="Footer1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)+1 == len(new_groups)


def test_add_group2(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="Grop2", header="Heder1", footer="Footer1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
