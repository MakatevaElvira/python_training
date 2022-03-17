class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # wd.find_element_by_xpath("//a[.='groups']").click()
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")
