import sys


class range():
    def __init__(self, fullsize, unit):
        self.fullsize = fullsize
        self.unit = unit
        self.start_bust_range = 0
        self.end_bust_range = 0
        self.start_shoulder_range = 0
        self.end_shoulder_range = 0
        self.start_hip_range = 0
        self.end_hip_range = 0
        self.start_waist_range = 0
        self.end_waist_range = 0

    def top_range_cm(self):

        bustsizes = [70, 81, 83, 86, 89, 91, 95,
                     99, 102, 107, 120, 132.5, 143, 145]
        shouldersizes = [30, 35, 37, 37, 38, 39,
                         40, 41, 42, 43, 47, 49.3, 51, 52]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 18 US - 22 UK', '3X - 20 US - 24 UK',
                '4X - 22 US - 26 UK', '5X - 24 US - 28 UK']
        index = size.index(self.fullsize)
        if (index > 0) and (index < (len(size) - 1)):
            self.start_bust_range = bustsizes[index - 1] - 6
            self.end_bust_range = bustsizes[index + 1] + 6
            self.start_shoulder_range = shouldersizes[index - 1] - 2
            self.end_shoulder_range = shouldersizes[index + 1] + 3
        elif (index == 0):
            self.start_bust_range = bustsizes[index] - 6
            self.end_bust_range = bustsizes[index + 1] + 6
            self.start_shoulder_range = shouldersizes[index] - 2
            self.end_shoulder_range = shouldersizes[index + 1] + 3
        elif (index == (len(size) - 1)):
            self.start_bust_range = bustsizes[index - 1] - 6
            self.end_bust_range = bustsizes[index] + 6
            self.start_shoulder_range = shouldersizes[index - 1] - 2
            self.end_shoulder_range = shouldersizes[index] + 3

    def bottom_range_cm(self):

        waistsizes = [58, 61, 63, 66, 68, 71,
                      74, 78, 82, 87, 105, 110, 120, 120]
        hipsizes = [80, 85, 90, 92, 95, 97, 101,
                    105, 109, 114, 125, 130, 140, 140]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 18 US - 22 UK',
                '3X - 20 US - 24 UK', '4X - 22 US - 26 UK', '5X - 24 US - 28 UK']

        index = size.index(self.fullsize)
        if (index > 0) and (index < (len(size) - 1)):
            self.start_hip_range = hipsizes[index - 1] - 2
            self.end_hip_range = hipsizes[index + 1] + 5
            self.start_waist_range = waistsizes[index - 1] - 5
            self.end_waist_range = waistsizes[index + 1] + 12
        elif (index == 0):
            self.start_hip_range = hipsizes[index] - 2
            self.end_hip_range = hipsizes[index + 1] + 5
            self.start_waist_range = waistsizes[index] - 5
            self.end_waist_range = waistsizes[index + 1] + 12
        elif (index == (len(size) - 1)):
            self.start_hip_range = hipsizes[index - 1] - 2
            self.end_hip_range = hipsizes[index] + 5
            self.start_waist_range = waistsizes[index - 1] - 5
            self.end_waist_range = waistsizes[index] + 12

    def top_range_in(self):
        print(self)
        sys.stdout.flush()
        bustsizes = [27.6, 31.9, 32.7, 33.9, 35.0, 35.8, 37.4, 39.0, 40.2, 42.1, 47.2, 52.2, 56.3, 57.1]
        shouldersizes = [11.8, 13.8, 14.6, 14.6, 15.0, 15.4, 15.7, 16.1, 16.5, 16.9, 18.5, 19.4, 20.1, 20.5]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 18 US - 22 UK', '3X - 20 US - 24 UK',
                '4X - 22 US - 26 UK', '5X - 24 US - 28 UK']

        index = size.index(self.fullsize)
        if (index > 0) and (index < len(size) - 1):
            self.start_bust_range = bustsizes[index - 1] - 2.4
            self.end_bust_range = bustsizes[index + 1] + 2.4
            self.start_shoulder_range = shouldersizes[index - 1] - 0.8
            self.end_shoulder_range = shouldersizes[index + 1] + 1.2
        elif (index == 0):
            self.start_bust_range = bustsizes[index] - 2.4
            self.end_bust_range = bustsizes[index + 1] + 2.4
            self.start_shoulder_range = shouldersizes[index] - 0.8
            self.end_shoulder_range = shouldersizes[index + 1] + 1.2
        elif (index == (len(size) - 1)):
            self.start_bust_range = bustsizes[index - 1] - 2.4
            self.end_bust_range = bustsizes[index] + 2.4
            self.start_shoulder_range = shouldersizes[index - 1] - 0.8
            self.end_shoulder_range = shouldersizes[index] + 1.2

    def bottom_range_in(self):
        waistsizes = [22.8, 24.0, 24.8, 26.0, 26.8, 28.0, 29.1, 30.7, 32.3, 34.3, 41.3, 43.3, 47.2, 47.2]
        hipsizes = [31.5, 33.5, 35.4, 36.2, 37.4, 38.2, 39.8, 41.3, 42.9, 44.9, 49.2, 51.2, 55.1, 55.1]
        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 18 US - 22 UK', '3X - 20 US - 24 UK',
                '4X - 22 US - 26 UK', '5X - 24 US - 28 UK']

        index = size.index(self.fullsize)
        if (index > 0) and (index < len(size) - 1):
            self.start_hip_range = hipsizes[index - 1] - 0.8
            self.end_hip_range = hipsizes[index + 1] + 2.0
            self.start_waist_range = waistsizes[index - 1] - 2.0
            self.end_waist_range = waistsizes[index + 1] + 4.7
        elif (index == 0):
            self.start_hip_range = hipsizes[index] - 0.8
            self.end_hip_range = hipsizes[index + 1] + 2.0
            self.start_waist_range = waistsizes[index] - 2.0
            self.end_waist_range = waistsizes[index + 1] + 4.7
        elif (index == (len(size) - 1)):
            self.start_hip_range = hipsizes[index - 1] - 0.8
            self.end_hip_range = hipsizes[index] + 2.0
            self.start_waist_range = waistsizes[index - 1] - 2.0
            self.end_waist_range = waistsizes[index] + 4.7

    def get_range(self):

        if (self.unit == 'cm'):
            self.top_range_cm()
            self.bottom_range_cm()

        elif (self.unit == 'in'):
            self.top_range_in()
            self.bottom_range_in()

# ob = range('5X - 24 US - 28 UK', "cm")
# ob.get_range()
# print "start bust range " + str(ob.start_bust_range)
# print "end bust range" + str(ob.end_bust_range)
# print "start shoulder range" + str(ob.start_shoulder_range)
# print "end shoulder range " + str(ob.end_shoulder_range)
# print "start hip range " + str(ob.start_hip_range)
# print "end hip range " + str(ob.end_hip_range)
# print "start waist range " + str(ob.start_waist_range)
# print "end waist range  " + str(ob.end_waist_range)
