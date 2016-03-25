
class Location(object):

    def __init__(self, groupon_name, groupalia_name):
        self.id = id
        self.groupon_name = groupon_name
        self.groupalia_name = groupalia_name

    def get_groupon_name(self):
        return self.groupon_name

    def get_groupalia_name(self):
        return self.groupalia_name
