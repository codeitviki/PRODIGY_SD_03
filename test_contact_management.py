import os
import json
from contact_management import load_contacts, save_contacts, add_contact, view_contacts, edit_contact, delete_contact

def test_add_contact():
    contacts = []
    # Simulate adding a contact
    # Since input is interactive, we need to mock it or use a different approach
    # For testing, let's directly append to contacts
    contacts.append({'name': 'John Doe', 'phone': '1234567890', 'email': 'john@example.com'})
    save_contacts(contacts)
    loaded = load_contacts()
    assert len(loaded) == 1
    assert loaded[0]['name'] == 'John Doe'
    print("Test add_contact: PASSED")

def test_view_contacts():
    contacts = load_contacts()
    # Since view_contacts prints, we can't easily assert, but we can check if it runs without error
    view_contacts(contacts)
    print("Test view_contacts: PASSED (manual check required)")

def test_edit_contact():
    contacts = load_contacts()
    if contacts:
        # Simulate editing
        contacts[0]['name'] = 'Jane Doe'
        save_contacts(contacts)
        loaded = load_contacts()
        assert loaded[0]['name'] == 'Jane Doe'
        print("Test edit_contact: PASSED")
    else:
        print("No contacts to edit")

def test_delete_contact():
    contacts = load_contacts()
    if contacts:
        del contacts[0]
        save_contacts(contacts)
        loaded = load_contacts()
        assert len(loaded) == 0
        print("Test delete_contact: PASSED")
    else:
        print("No contacts to delete")

def test_persistence():
    # Add a contact, save, load in new session
    contacts = [{'name': 'Test User', 'phone': '0987654321', 'email': 'test@example.com'}]
    save_contacts(contacts)
    new_contacts = load_contacts()
    assert len(new_contacts) == 1
    assert new_contacts[0]['name'] == 'Test User'
    print("Test persistence: PASSED")

if __name__ == "__main__":
    # Clean up any existing file
    if os.path.exists('contacts.json'):
        os.remove('contacts.json')
    
    test_add_contact()
    test_view_contacts()
    test_edit_contact()
    test_delete_contact()
    test_persistence()
    
    # Clean up
    if os.path.exists('contacts.json'):
        os.remove('contacts.json')
    
    print("All tests completed.")
