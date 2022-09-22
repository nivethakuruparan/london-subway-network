class Line():
    def __init__(self, num):
        self.num = num
        self.name = ''
        self.colour = ''
        self.stripe = ''
    
    def set_name(self, name):
        self.name = name

    def set_colour(self, col):
        self.colour = col

    def set_stripe(self, str):
        self.stripe = str
    
    def get_name(self):
        return self.name

    def get_colour(self):
        return self.coloir

    def get_stripe(self):
        return self.stripe
        