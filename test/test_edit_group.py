from model.group import Group


def test_edite_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="GropEdited",header="headerEdited",footer="footerEdited"))
    app.session.logout()