class range():
    def __init__(self, fullsize, unit):
        self.fullsize = fullsize
        self.unit = unit
        self.start_chest_range = 0
        self.end_chest_range = 0
        self.start_shoulder_range = 0
        self.end_shoulder_range = 0
        self.start_seat_range = 0
        self.end_seat_range = 0
        self.start_waist_range = 0
        self.end_waist_range = 0

    def top_range_cm(self):

        chestsizes = [78, 82, 90, 98, 106, 114, 122, 138, 145, 154]
        shouldersizes = [30, 35, 39, 43, 47, 50, 47, 53, 55, 57]
        size = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL']
        index = size.index(self.fullsize)
        if (index > 0) and (index < (len(size) - 1)):
            self.start_chest_range = chestsizes[index - 1] - 6
            self.end_chest_range = chestsizes[index + 1] + 12
            self.start_shoulder_range = shouldersizes[index - 1] - 2
            self.end_shoulder_range = shouldersizes[index + 1] + 4
        elif (index == 0):
            self.start_chest_range = chestsizes[index] - 6
            self.end_chest_range = chestsizes[index + 1] + 12
            self.start_shoulder_range = shouldersizes[index] - 2
            self.end_shoulder_range = shouldersizes[index + 1] + 4
        elif (index == (len(size) - 1)):
            self.start_chest_range = chestsizes[index - 1] - 6
            self.end_chest_range = chestsizes[index] + 12
            self.start_shoulder_range = shouldersizes[index - 1] - 2
            self.end_shoulder_range = shouldersizes[index] + 4

    def bottom_range_cm(self):

        waistsizes = [56, 70, 78, 86, 95, 105, 119, 129, 140, 151]
        seatsizes = [80, 86, 94, 102, 110, 118, 126, 134, 140, 155]
        size = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL']

        index = size.index(self.fullsize)
        if (index > 0) and (index < (len(size) - 1)):
            self.start_seat_range = seatsizes[index - 1] - 10
            self.end_seat_range = seatsizes[index + 1] + 15
            self.start_waist_range = waistsizes[index - 1] - 5
            self.end_waist_range = waistsizes[index + 1] + 10
        elif (index == 0):
            self.start_seat_range = seatsizes[index] - 10
            self.end_seat_range = seatsizes[index + 1] + 15
            self.start_waist_range = waistsizes[index] - 5
            self.end_waist_range = waistsizes[index + 1] + 10
        elif (index == (len(size) - 1)):
            self.start_seat_range = seatsizes[index - 1] - 5
            self.end_seat_range = seatsizes[index] + 15
            self.start_waist_range = waistsizes[index - 1] - 5
            self.end_waist_range = waistsizes[index] + 10

    def convert_to_IN(self):
        if (self.unit.lower() == "in"):
            self.start_chest_range = self.start_chest_range / 2.54
            self.end_chest_range = self.end_chest_range / 2.54
            self.start_shoulder_range = self.start_shoulder_range / 2.54
            self.end_shoulder_range = self.end_shoulder_range / 2.54

            self.start_seat_range = self.start_seat_range / 2.54
            self.end_seat_range = self.end_seat_range / 2.54

            self.start_waist_range = self.start_waist_range / 2.54
            self.end_waist_range = self.end_waist_range / 2.54

    def get_range(self):

        self.top_range_cm()
        self.bottom_range_cm()
        self.convert_to_IN()

#
# ob=range('5XL',"in")
# ob.get_range()
# print ("start chest range " + str(ob.start_chest_range ))
# print "end chest range" + str(ob.end_chest_range )
# print "start shoulder range" + str(ob.start_shoulder_range)
# print "end shoulder range " + str(ob.end_shoulder_range)
# print "start seat range " + str(ob.start_seat_range)
# print "end seat range " + str(ob.end_seat_range )
# print "start waist range " + str(ob.start_waist_range)
# print "end waist range  " + str(ob.end_waist_range)
