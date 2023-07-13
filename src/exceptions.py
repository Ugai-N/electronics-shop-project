class InstantiateCSVError(Exception):
    def __init__(self, *args):
        self.message = args[0] if args else "Файл item.csv поврежден!!!"

