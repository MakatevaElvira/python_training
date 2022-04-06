import re


def test_phones_on_home_page_new(app):
    contact_from_home_page = app.contact.get_contact_list_with_allPhones()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones == app.contact.merge_phones_like_on_homePage(contact_from_edit_page)


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.home_phone == app.contact.clear(contact_from_edit_page.home_phone)
    assert contact_from_home_page.work_phone == app.contact.clear(contact_from_edit_page.work_phone)
    assert contact_from_home_page.mobile_phone == app.contact.clear(contact_from_edit_page.mobile_phone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.home_phone == contact_from_edit_page.home_phone
    assert contact_from_view_page.work_phone == contact_from_edit_page.work_phone
    assert contact_from_view_page.mobile_phone == contact_from_edit_page.mobile_phone




