from .taskbase import TaskBase
from datetime import datetime


class Time(TaskBase):
    def __init__(self):
        self.name = 'Time'

    def Dict_Init(self, data):
        data[self.name] = []

    def Extract(self, *args):
        file_path = args[0]
        data = args[1]
        time = datetime.strptime(('20' + file_path[19:36]), '%Y.%m.%d-%H.%M.%S')
        data[self.name].append(time)

    def case_nan(self, *args):
        file_path = args[0]
        data = args[1]
        time = datetime.strptime(('20' + file_path[19:36]), '%Y.%m.%d-%H.%M.%S')
        data[self.name].append(time)
