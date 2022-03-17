class GroupHelper:

    def __init__(self, app):
        self.app = app

    def fill_group_form(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)


    def init_group_creation(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def return_group_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def create(self, group):
        wd = self.app.wd
        self.app.navigation.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, group)
        self.app.submit(wd)
        self.return_group_page(wd)
