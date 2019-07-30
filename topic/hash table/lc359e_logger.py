class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        status = True
        if len(self.dic) != 0 and message in self.dic:
            if abs(timestamp - self.dic[message]) < 10:
                return False
        self.dic[message] = timestamp
        return status





# Outside of class
# d = {}
# def spm(timestamp, message):
#     status = True
#     if len(d) != 0 and message in d:
#         if abs(timestamp - d[message]) < 10:
#             return False
#
#     d[message] = timestamp
#     return status
