import re

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

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//tr[@name='entry']/td[7]")[index].click()

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
                all_phones = element.find_element_by_xpath("./td[6]").text.splitlines()
                print("second!!!= " + all_phones[1])
                self.contact_cash.append(Contact(name=text, last_name=tex2, id=id,
                                                 home_phone=all_phones[0],
                                                 mobile_phone=all_phones[1],
                                                 work_phone=all_phones[2]))
        return list(self.contact_cash)

    def get_contact_list_size(self):
            wd = self.app.wd
            self.open_contact_page()
            elements = wd.find_elements_by_xpath("//tr[@name='entry']")
            return len(elements)

    def get_contact_list_with_allPhones(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                text = element.find_element_by_xpath("./td[3]").text
                tex2 = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_xpath("./td[6]").text
                print("second!!!= " + all_phones[1])
                self.contact_cash.append(Contact(name=text, last_name=tex2, id=id,
                                                 all_phones=all_phones))
        return list(self.contact_cash)

    def get_contact_list_full(self):
        if self.contact_cash is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cash = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                name = element.find_element_by_xpath("./td[3]").text
                last_name = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_xpath("./td[4]").text
                all_emails = element.find_element_by_xpath("./td[5]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                print("second!!!= " + all_phones[1])
                self.contact_cash.append(Contact(name=name, last_name=last_name, id=id,
                                                 address=address, all_emails=all_emails,
                                                 all_phones=all_phones))
        return list(self.contact_cash)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.init_contact_edition_by_index( index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        return (Contact(name=name, last_name=last_name, id=id, home_phone=home,
                        mobile_phone=mobile, work_phone=work))

    def get_contact_info_from_edit_page_full(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.init_contact_edition_by_index( index)
        name = wd.find_element_by_name("firstname").get_attribute("value")
        last_name = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        e_mail = wd.find_element_by_name("email").get_attribute("value")
        e_mail2 = wd.find_element_by_name("email2").get_attribute("value")
        e_mail3 = wd.find_element_by_name("email3").get_attribute("value")
        return (Contact(name=name, last_name=last_name, id=id,address=address,
                        home_phone=home,mobile_phone=mobile, work_phone=work,
                        email=e_mail,email2=e_mail2,email3=e_mail3))


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_page()
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text)
        if home_phone != None:
            print(home_phone.group(1))
        else:
            print('None!')
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return (Contact( home_phone=home_phone,
                         mobile_phone=mobile_phone,
                         work_phone=work_phone))

    def clear(self, string):
        return re.sub("[() -]", "", string)

    # работа с данными в функциональном стиле= СКЛЕЙКА
    def merge_phones_like_on_homePage(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           (contact.home_phone, contact.mobile_phone, contact.work_phone)))))

    # работа с данными в функциональном стиле= СКЛЕЙКА
    def merge_emails_like_on_homePage(self, contact):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           (contact.email, contact.email2, contact.email3)))))




