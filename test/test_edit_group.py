from model.group import Group


def test_edite_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    app.group.edit_first(Group(name="GropEdited",header="headerEdited",footer="footerEdited"))

def test_edite_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Precondition name"))
    app.group.edit_first(Group(name="New name"))
