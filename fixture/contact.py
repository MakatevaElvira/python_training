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
        self.init_contact_edition_by_index(0)

    def init_contact_edition_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//*[@title='Edit']")[index].click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def fill_contact_form(self, contact):
        self.app.fill_field("firstname", contact.name)
        self.app.fill_field("middlename", contact.middle_name)
        self.app.fill_field("lastname", contact.last_name)
        self.app.fill_field("company", contact.company)
        self.app.fill_field("home", contact.home_phone)
        self.app.fill_field("email", contact.email)

    def return_home(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home page").click()

    # @staticmethod
    def create(self, contact):
        self.init_contact_creation()
        self.fill_contact_form(contact)
        self.app.submit()
        self.return_home()
        self.contact_cash = None

    def edit_first(self, contact):
        self.edit_by_index(contact, 0)

    def edit_by_index(self, contact, index):
        self.open_contact_page()
        self.init_contact_edition_by_index(index)
        self.fill_contact_form(contact)
        self.app.update()
        self.return_home()
        self.contact_cash = None

    def delete_first(self):
        self.delete_by_index(0)

    def delete_by_index(self, index):
        self.open_contact_page()
        self.init_contact_edition_by_index(index)
        self.app.delete()
        self.app.navigation.home()
        self.contact_cash = None

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    """кеширование трудоемкой операции"""
    contact_cash = None

    def get_contact_list(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                text = element.find_element_by_xpath("./td[3]").text
                tex2 = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cash.append(Contact(name=text, last_name=tex2, id=id))
        return list(self.contact_cash)
