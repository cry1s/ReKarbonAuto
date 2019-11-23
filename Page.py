class Page:
    pages = 0
    rows = 20
    def __init__(self, number: int):
        Page.pages += 1
        self.number = number


    def close(self):
        pass


    def show(self, number):
        self.close()
        pass

    @staticmethod
    def minus():
        Page.pages-=1
