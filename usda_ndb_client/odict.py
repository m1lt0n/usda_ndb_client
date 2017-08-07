class ODict:
    '''Wrapper to access dict keys as attributes'''

    def __init__(self, d):
        self.__dict__ = d
