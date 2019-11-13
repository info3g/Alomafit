class full_size():
    def __init__(self, weight, height, weightunit, heightunit):
        self.weight = weight
        self.weightunit = weightunit
        self.height = height
        self.heightunit = heightunit

    def convert_to_KG(self):
        if (self.weightunit.lower() == "lb"):
            self.weight = self.weight * 0.454

    def convert_to_CM(self):
        if (self.heightunit.lower() == "in"):
            self.height = self.height * 2.54

    def get_body_mass_ratio(self):
        hinm = self.height / 100.0

        sq = hinm * hinm

        bodymass = self.weight / sq

        if (bodymass > 24.9):
            return 1
        else:
            return 0

    def get_full_size(self):

        self.convert_to_KG()
        self.convert_to_CM()
        bodymass = self.get_body_mass_ratio()

        size = ['XXS - 00 US', 'XS - 0 US - 4 UK', 'S - 2 US - 6 UK',
                'S - 4 US - 8 UK', 'M - 6 US - 10 UK', 'M - 8 US - 12 UK',
                'L - 10 US - 14 UK', 'L - 12 US - 16 UK ',
                'XL - 14 US - 18 UK', '2X - 18 US - 22 UK', '3X - 20 US - 24 UK',
                '4X - 22 US - 26 UK', '5X - 24 US - 28 UK']

        if (self.weight < 45):
            if (self.height < 153):
                return size[0]
            if (self.height >= 153):
                return size[1]

        if (self.weight >= 45) and (self.weight < 55):
            if (self.height >= 157 and self.height <= 165):
                return size[1]
            else:
                return size[2]

        if (self.weight >= 55) and (self.weight < 60):
            return size[2 + bodymass]

        if (self.weight >= 60) and (self.weight < 64):
            if (self.height >= 153 and self.height <= 178):

                return size[3]
            else:

                return size[4 + bodymass]

        if (self.weight >= 64) and (self.weight < 68):
            return size[4 + bodymass]

        if (self.weight >= 68) and (self.weight < 73):
            if (self.height < 155):

                return size[6 + bodymass]
            else:

                return size[4 + bodymass]

        if (self.weight >= 73) and (self.weight < 77):
            if (self.height < 178):

                return size[6 + bodymass]
            else:

                return size[4 + bodymass]

        if (self.weight >= 77) and (self.weight < 82):
            if (self.height < 150):
                return size[8]
            else:

                return size[6 + bodymass]

        if (self.weight >= 82) and (self.weight < 86):
            if (self.height < 160):
                return size[8]
            else:

                return size[6]

        if (self.weight >= 86) and (self.weight < 90):
            if (self.height < 160):
                return size[9]
            elif ((self.height >= 160) and (self.height < 178)):
                return size[8]
            else:
                return size[6 + bodymass]

        if (self.weight >= 90) and (self.weight < 100):
            if (self.height < 165):
                return size[10]
            elif (self.height < 180):
                return size[9]
            else:
                return size[8]

        if (self.weight >= 100) and (self.weight < 110):
            if (self.height < 170):
                return size[11]
            elif (self.height < 185):
                return size[10]
            else:
                return size[9]
        if (self.weight >= 110) and (self.weight < 120):
            if (self.height < 170):
                return size[12]
            elif (self.height < 185):
                return size[11]
            else:
                return size[10]

        if (self.weight >= 120):
            return size[12]

# test full_size
# input in order : weight, height , weight unit,hieght unit
# obj = full_size(100, 164, 'kg', 'cm')
# result = obj.get_full_size()
# print ("standard full size is " + result)
