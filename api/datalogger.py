import csv, os
#from socketIO_client import SocketIO, BaseNamespace


class DataLogger:
    def __init__(self, filename=None, kind='csv'):
        #self.socketIO = SocketIO('159.203.69.117', 3000)
        self.file = None
        self.kind = kind
        if filename is not None:
            directory = os.path.dirname(filename)
            if not os.path.isdir(directory):
                os.makedirs(directory)
            if self.kind == 'dat':
                filename += '.dat'
                self.file = open(filename, 'w')
            elif self.kind == 'csv':
                self.file = open(filename, 'wt')
                self.writer = csv.writer(self.file)

    def __call__(self, string):
        if self.file is not None:
            if self.kind == 'dat':
                self.file.write(string)
            elif self.kind == 'csv':
                self.writer.writerow(string)

        else:
            print string
            #self.socketIO.emit('log', {'raspID': 'a', 'log': string})

    def __del__(self):
        if self.file is not None:
            self.file.close()
