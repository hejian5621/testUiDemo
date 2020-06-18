import os

class ProjectFolderLocation:

    @staticmethod
    def ToObtainPosition():
        address  = os.path.dirname(os.path.realpath(__file__))
        address=address[:-8]
        return address