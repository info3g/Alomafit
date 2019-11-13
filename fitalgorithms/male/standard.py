# To change this license header, choose License Headers in Project Properti


class measure():

    @staticmethod
    def size_topsize():
        return ['XXS', 'XS', 'XS', 'S', 'S',
                'M', 'M', 'L', 'L', 'XL', 'XL', 'XXL', 'XXL', 'XXL', '3XL', '4XL', '5XL']

    def size_bottomsize():
        return ['XS - 34', 'XS - 36', 'S 38', 'S 40', 'M 42', 'M 44',
                'L 46', 'L 48', 'XL 50', 'Xl 52', 'XXl 54', '3Xl 56', '4Xl 58', '5Xl 60']

    def __init__(self, chest, hip, waist, unit):
        self.hip = hip
        self.waist = waist
        self.chest = chest

        self.unit = unit

        self.topsize = ""
        self.bottomsize = ""

    def run(self):
        self.convert_to_CM()

    def rule_topsize_cm(self):

        chestsizes = [78, 82, 86, 90, 94, 98, 102, 106,
                      110, 114, 118, 122, 126, 130, 138, 145, 154]

        size = ['XXS', 'XS', 'XS', 'S', 'S',
                'M', 'M', 'L', 'L', 'XL', 'XL', 'XXL', 'XXL', 'XXL', '3XL', '4XL', '5XL']

        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.chest >= chestsizes[i]) and (self.chest < chestsizes[i + 1])):
                    return size[i + 1]
            elif ((self.chest >= chestsizes[i])):
                return size[i + 1]
            i = i + 1

        return size[0]

    def rule_bottomsize_cm(self):

        waistsizes = [70, 74, 78, 82, 86, 90, 95,
                      100, 105, 110, 119, 129, 140, 151]
        hipsizes = [86, 90, 94, 98, 102, 106, 110,
                    114, 118, 122, 126, 134, 140, 155]
        size = ['XS - 34 ', 'XS - 36', 'S 38', 'S 40', 'M 42', 'M 44',
                'L 46', 'L 48', 'XL 50', 'Xl 52', 'XXl 54', '3Xl 56', '4Xl 58', '5Xl 60']
        res = "none"

        i = 0

        i = 0

        while i < len(size):
            if (i < len(size) - 2):
                if ((self.waist >= waistsizes[i]) and (self.waist < waistsizes[i + 1])):
                    return size[i + 1]

            elif ((self.waist >= waistsizes[i])):
                return size[i + 1]
            i = i + 1
        while i < len(size):

            if (i < len(size) - 2):
                if ((self.hip >= hipsizes[i]) and (self.hip < hipsizes[i + 1])):
                    return size[i + 1]

            elif ((self.hip >= hipsizes[i])):
                return size[i + 1]
            i = i + 1

        return size[0]

    def convert_to_CM(self):
        if (self.unit.lower() == "in"):
            self.hip = hip * 2.54
            self.waist = waist * 2.54
            self.chest = chest * 2.54

# 88 91 67 40


# ob = measure(151, 134, 138, 'cm')
# ob.run()
# t = ob.rule_topsize_cm()
# print ("top standard size : " + t)
# t = ob.rule_bottomsize_cm()
# print ("bottom standard size : " + t)


# ob=measure(33,43,33,14.7,'in')
# t=ob.rule_topsize_in()
# print t
# t=ob.rule_bottomsize_in()
# print t
