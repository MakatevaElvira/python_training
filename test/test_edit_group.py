from random import randrange

from model.group import Group


def test_edite_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    edited_group = Group(name="GropEdited",header="headerEdited",footer="footerEdited")
    edited_group.id = old_groups[0].id
    app.group.edit_first(edited_group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0]= edited_group
    assert sorted(old_groups,key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_edite_first_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    edited_group = Group(name="New name")
    index = randrange(len(old_groups))
    edited_group.id = old_groups[index].id
    app.group.edit_by_index(edited_group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = edited_group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
