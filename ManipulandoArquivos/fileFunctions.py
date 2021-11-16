import os
#Sistema de arquivos no servidor.
class fileManipulation:
    def __init__(self):
        self._path = self.getPath()

    # 1 - read Method (file)
    def readFile(self, nome):
        file = self._path + nome
        show = open(file, 'r+')
        print("File Readed")
        return show.read()

    # 2 - rename Method (file)
    def renameFile(self, nome, new_nome):
        file = self._path + nome
        rename_file = self._path + new_nome
        os.rename(file, rename_file)
        print("File Renamed!")

    #3 - create Method (file)
    def createFile(self, nome):
        file = self._path + nome
        open(file, 'w')
        print("File Created!")

    #4 - remove Method (file)
    def removeFile(self, nome):
        file = self._path + nome
        os.remove(file)
        print("File Removed")

    def getPath(self):
        path = os.getcwd().split("\\")
        path.pop()
        return "\\".join(path) + "\\UsedData\\"