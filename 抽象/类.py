class Secretive:
    def _inaccessible(self):
        print "you can not see me"

    def accessible(self):
        print "The secretive is that "
        self._inaccessible()


s = Secretive()
s.accessible()

