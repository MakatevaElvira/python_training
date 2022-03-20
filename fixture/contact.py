class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        self.app.home()

    def init_first_contact_edition(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@title='Edit']").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.app.fill_field("firstname",contact.name)
        self.app.fill_field("middlename", contact.middle_name)
        self.app.fill_field("company", contact.company)
        self.app.fill_field("home", contact.home_phone)
        self.app.fill_field("email", contact.email)

    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    #@staticmethod
    def create(self, contact):
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.app.submit()
        self.return_home()

    def edit_first(self, contact):
        self.open_contact_page()
        self.select_first_contact()
        self.init_first_contact_edition()
        self.fill_contact_form(contact)
        self.app.update()
        self.return_home()

    def delete_first(self):
        self.open_contact_page()
        self.select_first_contact()
        self.init_first_contact_edition()
        self.app.delete()
        self.app.navigation.home()
