class Calculator:
    def calculate(self, expression):
        self.value = eval(expression)


class Talk(Calculator):
    def talk(self):
        print "Hi,my value is %s" % self.value


class TalkingCalculator(Calculator, Talk):
    pass


t = TalkingCalculator()
t.calculate('4+3*7')
t.talk()
