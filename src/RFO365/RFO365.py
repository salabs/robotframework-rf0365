from salabsutils import DynamicRobotApiClass
from pyo365 import Account, MailBox
from robot.api.deco import keyword

class RFO365(DynamicRobotApiClass):
    def __init__(self, user_name, user_password):
        self.user_name = user_name
        self.user_password = user_password


    @keyword
    def do_do_do_do_not(self):
        pass

