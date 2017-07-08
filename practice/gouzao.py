class Bird(object):
    def __init__(self):
        self.x = True

    def eat(self):
        if self.x:
            print "Ahhhhh"
            self.x = False
        else:
            print "NO ,thanks!"


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird, self).__init__()
        self.song = "ADad"

    def sing(self):
        print self.song


bird1 = SongBird()
bird1.sing()
bird1.eat()
bird1.eat()
