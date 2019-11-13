# TODO there is no consistency between inch,cm for male and female
# WHY you define the same size variable twice for each method _cm _in


class measure():

    @staticmethod
    def size_topsize():
        return ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ', 'XL - 14 US - 18 UK',
                '2X - 16 US - 20 UK', '3X - 18 US - 22 UK', '4X - 20 US - 24 UK',
                '5X - 22 US - 26 UK']

    @staticmethod
    def size_bottomsize():
        return ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ', 'XL - 14 US - 18 UK',
                '2X - 16 US - 20 UK', '3X - 18 US - 22 UK', '4X - 20 US - 24 UK',
                '5X - 22 US - 26 UK']

    def __init__(self, bust, hip, waist, shoulder, unit):
        self.hip = hip
        self.waist = waist
        self.bust = bust
        self.shoulder = shoulder
        self.unit = unit

        self.topsize = ""
        self.bottomsize = ""

    def rule_topsize_cm(self):
        bustsizes = [81.3, 83.8, 86.4, 89.0, 91.4, 95.2,
                     99.1, 102.9, 107.9, 113.1, 120, 132.5, 143]
        shouldersizes = [35, 37.1, 37.8, 38.4, 39.1,
                         40.0, 41.0, 42.0, 43.2, 45, 47, 49.3, 51]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ', 'XL - 14 US - 18 UK',
                '2X - 16 US - 20 UK', '3X - 18 US - 22 UK', '4X - 20 US - 24 UK',
                '5X - 22 US - 26 UK']

        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.bust >= bustsizes[i]) and (self.bust < bustsizes[i + 1])):
                    return size[i + 1]
            elif ((self.bust >= bustsizes[i])):
                return size[i + 1]
            i = i + 1

        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.shoulder >= shouldersizes[i]) and (self.shoulder < shouldersizes[i + 1])):
                    return size[i]
            elif (self.shoulder >= shouldersizes[i]):
                return size[i]
            i = i + 1
        return size[0]

    def rule_bottomsize_cm(self):

        waistsizes = [61.0, 63.5, 66.0, 68.5, 71.1,
                      74.9, 78.7, 82.6, 87.6, 92.7, 97.5, 105, 110]
        hipsizes = [85, 90.2, 92.7, 95.2, 97.8, 101.6,
                    105.4, 109.2, 114.3, 119.4, 124, 128.5, 132]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ', 'XL - 14 US - 18 UK',
                '2X - 16 US - 20 UK', '3X - 18 US - 22 UK', '4X - 20 US - 24 UK',
                '5X - 22 US - 26 UK']
        res = "none"
        i = 0
        while i < len(size):

            if (i < len(size) - 2):
                if ((self.hip >= hipsizes[i]) and (self.hip < hipsizes[i + 1])):
                    return size[i + 1]

            elif ((self.hip >= hipsizes[i])):
                return size[i + 1]
            i = i + 1
        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.waist >= waistsizes[i]) and (self.waist < waistsizes[i + 1])):
                    return size[i + 1]

            elif ((self.waist >= waistsizes[i])):
                return size[i + 1]
            i = i + 1

        return size[0]

    def rule_topsize_in(self):
        bustsizes = [32, 33, 34, 35, 36, 37.5, 39,
                     40.5, 42.5, 44.5, 46.5, 48.5, 50.5]
        shouldersizes = [14.375, 14.625, 14.875, 15.125,
                         15.375, 15.75, 16.125, 16.5, 17, 17.5, 18, 18.5, 19]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 16 US - 20 UK', '3X - 18 US - 22 UK',
                '4X - 20 US - 24 UK', '5X - 22 US - 26 UK']
        res = "none"
        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.bust >= bustsizes[i]) and (self.bust < bustsizes[i + 1])):
                    return size[i + 1]
            elif ((self.bust >= bustsizes[i])):
                return size[i + 1]
            i = i + 1

        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.shoulder >= shouldersizes[i]) and (self.shoulder < shouldersizes[i + 1])):
                    return size[i + 1]
            elif (self.shoulder >= shouldersizes[i]):
                return size[i + 1]
            i = i + 1
        return size[0]

    def rule_bottomsize_in(self):
        waistsizes = [24, 25, 26, 27, 28, 29.5,
                      31, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5]
        hipsizes = [34.5, 35.5, 36.5, 37.5, 38.5,
                    40, 41.5, 43, 45, 47, 49, 51, 53]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ', 'XL - 14 US - 18 UK',
                '2X - 16 US - 20 UK', '3X - 18 US - 22 UK',
                '4X - 20 US - 24 UK', '5X - 22 US - 26 UK']
        res = "none"
        i = 0
        while i < len(size):

            if (i < len(size) - 2):
                if ((self.hip >= hipsizes[i]) and (self.hip < hipsizes[i + 1])):
                    return size[i + 1]

            elif ((self.hip >= hipsizes[i])):
                return size[i + 1]
            i = i + 1
        i = 0
        while i < len(size):
            if (i < len(size) - 2):
                if ((self.waist >= waistsizes[i]) and (self.hip < waistsizes[i + 1])):
                    return size[i + 1]

            elif ((self.waist >= waistsizes[i])):
                return size[i + 1]
            i = i + 1

        return size[0]

# 88 91 67 40

#
# ob = measure(120, 126, 107, 43, 'cm')
# t = ob.rule_topsize_cm()
# print (t)
# t = ob.rule_bottomsize_cm()
# print (t)

# ob=measure(33,43,33,14.7,'in')
# t=ob.rule_topsize_in()
# print t
# t=ob.rule_bottomsize_in()
# print t
