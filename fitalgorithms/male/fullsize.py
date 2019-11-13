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

        if (bodymass > 25.1):
            return 1
        else:
            return 0

    def get_full_size(self):

        self.convert_to_KG()
        self.convert_to_CM()
        bodymass = self.get_body_mass_ratio()
        size = ['XS', 'S', 'M', 'L', 'XL', 'XXL', '3XL', '4XL', '5XL']

        if (self.weight < 59):
            if (self.height < 165):
                return size[0]
            if (self.height >= 165):
                return size[1]

        if (self.weight >= 59) and (self.weight < 64):
            if (self.height >= 154 and self.height < 170):
                return size[1]
            else:
                return size[1] + " long"

        if (self.weight >= 64) and (self.weight < 68.5):
            if (self.height >= 157 and self.height < 170):
                return size[1]
            if (self.height >= 170 and self.height < 190):
                return size[1] + " long"
            return size[2] + " long"

        if (self.weight >= 68.5) and (self.weight < 73):
            if (self.height >= 165 and self.height < 173):
                return size[2]
            if (self.height >= 173 and self.height < 190):
                return size[1] + " long"
            return size[2] + " long"

        if (self.weight >= 73) and (self.weight < 77.5):
            if (self.height >= 165 and self.height < 180):
                return size[2]
            if (self.height >= 180 and self.height < 190):
                return size[1] + " long"
            return size[2] + " long"

        if (self.weight >= 77.5) and (self.weight < 80):
            if (self.height >= 165 and self.height < 183):
                return size[2]

            return size[2] + " long"

        if (self.weight >= 80) and (self.weight < 83):
            if (self.height >= 165 and self.height < 168):
                return size[2 + bodymass]
            if (self.height >= 168 and self.height < 180):
                return size[2]
            if (self.height >= 180 and self.height < 193):
                return size[2 + bodymass]

            return size[2] + " long"

        if (self.weight >= 83) and (self.weight < 85.2):
            if (self.height >= 165 and self.height < 175):
                return size[2 + bodymass]
            if (self.height >= 175 and self.height < 180):
                return size[2]

            return size[2 + bodymass]

        if (self.weight >= 85.2) and (self.weight < 88.4):
            if (self.height >= 165 and self.height < 170):
                return size[3]
            if (self.height >= 170 and self.height < 188):
                return size[2 + bodymass]

            return size[3]

        if (self.weight >= 88.4) and (self.weight < 93):
            return size[3]

        if (self.weight >= 93) and (self.weight < 99):
            if (self.height >= 170 and self.height < 183):
                return size[4]
            if (self.height >= 183 and self.height < 193):
                return size[3]

            return size[4]

        if (self.weight >= 99) and (self.weight < 104):
            if (self.height >= 173 and self.height < 180):
                return size[5]
            if (self.height >= 180 and self.height < 193):
                return size[4]
            if (self.height >= 193 and self.height < 205):
                return size[3]

        if (self.weight >= 104) and (self.weight < 118):
            if (self.height >= 170 and self.height < 180):
                return size[6]
            if (self.height >= 180 and self.height < 193):
                return size[5]
            if (self.height >= 193 and self.height < 205):
                return size[4]

        if (self.weight >= 118) and (self.weight < 127):
            if (self.height >= 170 and self.height < 180):
                return size[7]
            if (self.height >= 180 and self.height < 193):
                return size[6]
            if (self.height >= 193 and self.height < 210):
                return size[5]
        if (self.weight >= 127) and (self.weight < 140):
            if (self.height >= 170 and self.height < 180):
                return size[8]
            if (self.height >= 180 and self.height < 193):
                return size[7]
            if (self.height >= 193 and self.height < 210):
                return size[6]

        return size[8]

# test full_size
# input in order : weight, height , weight unit,hieght unit

# obj=full_size(160,195,'kg','cm')
# result=obj.get_full_size()
# print ("standard full size is " +result )
