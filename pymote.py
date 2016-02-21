from libcec import pyCecClient


class pyMote:
    """docstring for pyMote"""

    def __init__(self):
        self.lib = pyCecClient()
        self.input_value = None

    def power_off(self):
        self.lib.ProcessCommandTx("BF:36")

    def set_input(self, value=None):
        if value == 1:
            self.lib.ProcessCommandTx("4f:82:10:00")
        elif value == 2:
            self.lib.ProcessCommandTx("4f:82:20:00")
        elif value == 3:
            self.lib.ProcessCommandTx("4f:82:30:00")
        elif value == 4:
            self.lib.ProcessCommandTx("4f:82:40:00")

    def volume_inc(self):
        self.lib.ProcessCommandTx("70:44:00")
        self.lib.ProcessCommandTx("70:45")

    def mute(self):
        self.lib.ProcessCommandTx("F5:44:43")

    def tx(self, message=False):
        if message:
            self.lib.ProcessCommandTx(message)

if __name__ == '__main__':

    # http://www.cec-o-matic.com/
    tv = pyMote()
    # tv.power_off()
    tv.set_input(1)
    # tv.volume_inc()
    # tv.mute()