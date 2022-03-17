from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def submit(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def fill_group_form(self, group):
        wd = self.wd
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)

    def open_group_page(self):
        wd = self.wd
        #wd.find_element_by_xpath("//a[.='groups']").click()
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        # open home page
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def return_home(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def init_group_creation(self):
        wd = self.wd
        wd.find_element_by_name("new").click()

    def create_group(self, group):
        wd = self.wd
        self.open_group_page(wd)
        self.init_group_creation(wd)
        self.fill_group_form(wd, group)
        self.submit(wd)
        self.return_group_page(wd)

    def init_contact_creation(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact_form(self, contact):
        wd = self.wd
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.name)
        wd.find_element_by_name("middlename").send_keys(contact.middle_name)
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        wd.find_element_by_name("email").send_keys(contact.email)

    def create_contact(self, contact):
        wd = self.wd
        self.init_contact_creation(wd)
        self.fill_contact_form(wd, contact)
        self.submit(wd)
        self.return_home()


    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def destroy(self):
        self.wd.quit()
