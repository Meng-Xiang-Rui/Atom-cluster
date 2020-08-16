import os

from scipy.io import loadmat

from Tasks import TaskList, Time
# from DataProcess.utils import statistics

class process:

    def __init__(self, path, data = None, tasks = None):
        self.tasks = TaskList(tasks if tasks else [])

        # self.tasks.append(Time())
        self.data = data if data else {}
        self.path = path

    def data_extract(self):
        self.tasks.Dict_Init(self.data)
        pic_list = os.listdir(path)[1:]
        for i in range(0, len(pic_list), 2):
            try:
                allinone_path = path + r'\analyResult\03.Reconstruct\params' + pic_list[i][:-7] + r'-fig1\allInOne.mat'
                allinone = loadmat(allinone_path)
            except:
                self.tasks.case_nan(pic_list[i], self.data)
            else:
                self.tasks.Extract(pic_list[i], self.data, allinone)

    def pre_process(self, x):
        """nan => mean"""

        temp = x
        nan_list = []
        for i in range(len(temp)):
            if np.isnan(temp[i]):
                nan_list.append(i)
        mean = np.nanmean(temp)
        for i in nan_list:
            temp[i] = mean
        print(mean)
        return temp

    def Atom_number(self):
        pass

