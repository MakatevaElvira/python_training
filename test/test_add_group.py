# -*- coding: utf-8 -*-
from sys import maxsize

from model.group import Group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    added_group = Group(name="Grop1", header="Heder1", footer="Footer1")
    app.group.create(added_group)
    assert len(old_groups)+1 == app.group.count()  #"""хеш функция для предварительной проверки"""
    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)


def test_add_group2(app):
    old_groups = app.group.get_group_list()
    added_group = Group(name="Grop1", header="Heder1", footer="Footer1")
    app.group.create(added_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(added_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups,key=Group.id_or_max)

