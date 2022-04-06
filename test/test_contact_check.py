from random import randrange


def test_check_contacts_on_home_page(app):
    contacts_size = app.contact.get_contact_list_size()
    index = randrange(contacts_size)
    contact_from_home_page = app.contact.get_contact_list_full()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page_full(index)
    assert contact_from_home_page.name == contact_from_edit_page.name
    assert contact_from_home_page.last_name == contact_from_edit_page.last_name
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones == app.contact.merge_phones_like_on_homePage(contact_from_edit_page)
    assert contact_from_home_page.all_emails == app.contact.merge_emails_like_on_homePage(contact_from_edit_page)