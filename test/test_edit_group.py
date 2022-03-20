from model.group import Group


def test_edite_first_group(app):
    app.group.edit_first(Group(name="GropEdited",header="headerEdited",footer="footerEdited"))

def test_edite_first_group_name(app):
    app.group.edit_first(Group(name="New name"))
