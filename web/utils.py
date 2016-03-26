from location import Location
import os


class Utils(object):

    locations = {
        '1': Location('palma_de_mallorca', 'mallorca', 'mallorca'),
        '2': Location('sevilla', 'sevilla', 'sevilla'),
        '3': Location('madrid', 'madrid', 'madrid'),
    }

    @classmethod
    def get_location(cls, location_id):
        return cls.locations.get(location_id)

    @classmethod
    def remove_file(cls, path):
        if os.path.isfile(path):
            os.remove(path)

    @classmethod
    def get_file_content(cls, path):
        if os.path.isfile(path):
            f = open(path, 'r')
            text = f.read()
            f.close()
            return text
        else:
            return None
