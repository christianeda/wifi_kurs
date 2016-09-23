class Rechteck:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def seite1(self):
        s1 = abs(self.p1[1] - self.p2[1])
        return s1

    def seite2(self):
        s2 = abs(self.p1[0] - self.p2[0])
        return s2

    def umfang(self):
        return (2 * self.seite1()) + (2 * self.seite2())

    def flaeche(self):
        return self.seite1() * self.seite2()


if __name__ == '__main__':
    r1 = Rechteck((6, 9), (4, 5))
    print('Der Umfang ist {}'.format(r1.umfang()))
    print('Die Flaeche ist {}'.format(r1.flaeche()))
