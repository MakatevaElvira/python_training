from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        wd = self.app.wd
        self.app.fill_field("group_name", group.name)
        self.app.fill_field("group_header", group.header)
        self.app.fill_field("group_footer", group.footer)

    def fill_group_name(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group)

    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        self.init_group_creation()
        self.fill_group_form(group)
        self.app.submit()
        self.return_group_page()
        self.group_cash = None

    def select_first(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def submit_deletion(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()

    def submit_edition(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.app.navigation.open_group_page()
        self.select_by_index(index)
        self.submit_deletion()
        self.return_group_page()
        self.group_cash = None

    def edit_first(self, group):
        self.edit_by_index(group,0)

    def edit_by_index(self, group, index):
        self.app.navigation.open_group_page()
        self.select_by_index(index)
        self.submit_edition()
        self.fill_group_form(group)
        self.app.update()
        self.return_group_page()
        self.group_cash = None

    def count(self):
        wd = self.app.wd
        self.app.navigation.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    """?????????????????????? ???????????????????? ????????????????"""
    group_cash = None

    def get_group_list(self):
        if self.group_cash is None:
            wd = self.app.wd
            self.app.navigation.open_group_page()
            self.group_cash = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cash.append(Group(name=text, id=id))
        return list(self.group_cash)
