from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException

from fixture.contact import ContactHelper
from fixture.group import GroupHelper
from fixture.navigation import NavigationHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.navigation = NavigationHelper(self)

    def submit(self):
        wd = self.wd
        wd.find_element_by_name("submit").click()

    def update(self):
        wd = self.wd
        wd.find_element_by_name("update").click()

    def delete(self):
        wd = self.wd
        wd.find_element_by_xpath("//*[@value='Delete']").click()

    def fill_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

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
