class Contactbook:

  def _init_(self):
    self._contacts = dict()

  def add_contact(self, name, phone_number):
    self._contacts[name] = phone_number

  def get_number(self, name):
    return self._contacts.get(name)
