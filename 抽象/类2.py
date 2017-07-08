class MemberCounter:
    member = 0

    def init(self):
        MemberCounter.member += 1
        self.name = "liuxr"


m1 = MemberCounter()
m1.init()
print m1.name
print m1.member
m2 = MemberCounter()
m2.init()
print m2.member
print m1.member
print m1.__class__
print isinstance(m2, MemberCounter)
