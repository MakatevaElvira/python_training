class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").send_keys(contact.email)

    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    #@staticmethod
    def create(self, contact):
        wd = self.app.wd
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.app.submit()
        self.return_home()
