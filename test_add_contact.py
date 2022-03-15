import unittest

from selenium import webdriver

from contact import Contact


class TestAddContact(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.create_contact(wd, Contact(
            name="Elvira",
            middle_name="Heder1",
            company="Footer1",
            home_phone="+79000",
            email="mai@mail.ru"))
        self.return_home(wd)
        self.logout(wd)

    def tearDown(self):
        self.wd.quit()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("%s" % username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("%s" % password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def init_contact_creation(self, wd):
        wd.find_element_by_link_text("add new").click()

    def submit(self, wd):
        wd.find_element_by_name("submit").click()

    def fill_contact_form(self, wd, contact):
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").send_keys(contact.email)

    def create_contact(self, wd, contact):
        self.init_contact_creation(wd)
        self.fill_contact_form(wd, contact)
        self.submit(wd)

    def return_home(self, wd):
        wd.find_element_by_link_text("home page").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()


if __name__ == "__main__":
    unittest.main()
