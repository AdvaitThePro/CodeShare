class Loggable:
    def __init__(self):
        self.title = ""
    
    def log(self):
        print("Log message from " + self.title)

class Connection:
    def __init__(self):
        self.server = ""
    
    def connect(self):
        print("Connecting to database on" + self.server)

class sqlDatabase(Connection, Loggable):
    def __init__(self):
        self.title = "SQL Connection Demo"
        self.server = "play.advaitthepro.mc"

class framework(item):
    if isinstance(item, Connection):
        item.connect()

    if isinstance(item, Loggable):
        item.log()