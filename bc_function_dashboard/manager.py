from unittest import result
from .dashboard_manager import Dashboard

class Manager:

    def __init__(self):
        pass

    def get_details(self,user_id):
        try:
           dashboard_object = Dashboard()
           result = dashboard_object.get_dash_board(user_id)
           return result
        except Exception as e:
            pass
        finally:
            pass
