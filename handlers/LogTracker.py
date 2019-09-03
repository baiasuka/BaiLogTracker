import sys
import re
from common.RedisConnection import RedisConnection

class Tracker:
    """
    日志检查基类
    """
    def __init__(self, filepath):
        self._filepath = filepath

    def get_pre_line_num(self):
        """
        获取存入Redis里指定日志文件的上一次保存的最后行下标
        :return:
        """
        r_conn = RedisConnection()
        pre_line = r_conn.get(self._filepath)
        if pre_line:
            return pre_line
        else:
            r_conn.set(self._filepath, 0)
            return 0

    def set_pre_line_num(self, line_num):
        """
        设置日志文件对应的最后行
        :param line_num:
        :return:
        """
        r_conn = RedisConnection()
        r_conn.set(self._filepath, line_num)

    def get_new_line(self):
        pre_line_num = self.get_pre_line_num()
        new_lines = []
        last_line = 0
        for cur_line_num, line in enumerate(open(self._filepath, 'r'), start=1):
            if cur_line_num > pre_line_num:
                new_lines.append(line)
            last_line = cur_line_num
        self.set_pre_line_num(last_line)
        return new_lines


class OmsApiTracker(Tracker):
    pass

if __name__ == '__main__':
    print(Tracker('testlog.txt').get_new_line())

