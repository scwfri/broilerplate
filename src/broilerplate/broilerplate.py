import pathlib
import tomli

class Broil:

    def __init__(self, broil_file):
        self.broil_pan = pathlib.Path(broil_file)
        self.broils = self._parse_broil_pan(self.broil_pan)

    def _parse_broil_pan(self, broil_pan):
        """Parse broil pan configuration
        """
        with open(self.broil_pan.absolute(), 'rb') as f:
            pan = tomli.load(f)

        return pan

    def cook(self, plan):
