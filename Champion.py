class Champion :

    '''Base Class for Champions'''

    count = 0

    def __init__(self, key, name, title) :
        self.key = key
        self.name = name
        self.title = title
        Champion.count += 1
    
    def return_name(self) :
        return self.name

    def return_key(self) :
        return self.key

    def return_title(self) :
        return self.title