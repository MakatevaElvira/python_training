from model.group import Group


def test_edite_first_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    app.group.edit_first(Group(name="GropEdited",header="headerEdited",footer="footerEdited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups)  == len(new_groups)

def test_edite_first_group_name(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    app.group.edit_first(Group(name="New name"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
