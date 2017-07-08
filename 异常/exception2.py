class Caculator:
    n = False

    def cacl(self, expr):
        try:
            return eval(expr)
        except ZeroDivisionError:
            if self.n:
                print "Division by zero is illegal"

            else:
                raise


c = Caculator()
print c.cacl('10/2')
#c.cacl("10/0")
c.n = True
c.cacl("10/0")
