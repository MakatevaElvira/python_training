from sys import maxsize


class Contact:
    def __init__(self, name=None, last_name=None, middle_name=None, company=None, home_phone=None, email=None, id=None):
        self.name = name
        self.last_name = last_name
        self.middle_name = middle_name
        self.company = company
        self.home_phone = home_phone
        self.email = email
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.name, self.last_name)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
               and self.name == other.name \
               and self.last_name == other.last_name

    def id_or_max(cont):
        if cont.id:
            return int(cont.id)
        else:
            return maxsize