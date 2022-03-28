from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_contact_page(self):
        wd = self.app.wd
        self.app.navigation.home()

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
        self.app.fill_field("lastname", contact.last_name)
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

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
            text = element.find_element_by_xpath("./td[3]").text
            tex2 = element.find_element_by_xpath("./td[2]").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(name=text, last_name = tex2, id = id))
        return contacts
