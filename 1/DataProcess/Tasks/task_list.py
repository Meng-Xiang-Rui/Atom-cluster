from .taskbase import TaskBase
from collections.abc import MutableSequence


class TaskList(TaskBase, MutableSequence):
    def __init__(self, tasks):
        self.name = 'TaskList'
        self.tasks = list(tasks)

    def __len__(self):
        return len(self.tasks)

    def __getitem__(self, key):
        return self.tasks[key]

    def __setitem__(self, key, value):
        if isinstance(value, TaskBase):
            self.tasks[key] = value
        else:
            raise TypeError(
                "value must be an instance of DataProcess.Tasks.TaskBase"
            )

    def __delitem__(self, index):
        del self.tasks[index]

    def __iter__(self):
        return iter(self.tasks)

    def __add__(self, other):
        return TaskList(self.tasks + other.tasks)

    def insert(self, index, value):
        if isinstance(value, TaskBase):
            self.tasks.insert(index, value)
        else:
            raise TypeError(
                "value must be an instance of DataProcess.Tasks.TaskBase"
            )

    def Dict_Init(self, data):
        for tb in self.tasks:
            tb.Dict_Init(data)

    def case_nan(self, *args):
        for tb in self.tasks:
            tb.case_nan(*args)

    def Extract(self, data, *args):
        for tb in self.tasks:
            tb.Extract(*args)

    def Analysis(self, *args):
        for tb in self.tasks:
            tb.Analysis(*args)