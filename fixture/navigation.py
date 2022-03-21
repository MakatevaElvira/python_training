class NavigationHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        # open home page
        wd = self.app.wd
        wd.get("http://localhost/addressbook/index.php")

    def home(self):
        # open home page
        wd = self.app.wd
        if not (wd.current_url.endswith("index.php") and len(
                wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0):
            wd.find_element_by_link_text("home").click()
