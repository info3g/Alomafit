import operator


class stretch_percentagetype():
    def __init__(self, name):
        self.name = name

        self.nonestretch = ["buckram", "cambric", "casement", "cheese cloth", "chiffon", "chintz", "corduroy", "crepe",
                            "denim", "drill", "flanne", "gabardine",
                            "georgette", "kashmir Silk Khadi", "lawn", "mulmul", "muslin", "organdy", "poplin",
                            "sheeting", "taffeta", "tissue", "velvet"]

    def get_type(self):
        if (self.name.lower() in self.nonestretch):
            return "non stretch"
        else:
            return "stretch"


class garmentmeasure():
    def __init__(self, chest, waist, seat, shoulder, stretch_percentage, type, fit, sporty, size):
        self.chest = chest
        self.seat = seat
        self.waist = waist
        self.shoulder = shoulder
        self.stretch_percentage = stretch_percentage
        self.type = type
        self.fit = fit
        self.sporty = sporty

        self.location = []
        self.accept = []
        self.rate = 0
        self.defwaist = 0
        self.defchest = 0
        self.defseat = 0
        self.defshoulder = 0

        self.size = size

    def defference(self, bodymeasurements):
        if (self.chest != 0):
            self.defchest = self.chest - bodymeasurements.chest
        if (self.seat != 0):
            self.defseat = self.seat - bodymeasurements.seat
        if (self.waist != 0):
            self.defwaist = self.waist - bodymeasurements.waist
        if (self.shoulder != 0):
            self.defshoulder = self.shoulder - bodymeasurements.shoulder

    def rating(self):
        self.rate = abs(self.defseat) + abs(self.defshoulder) + \
                    abs(self.defwaist) + abs(self.defchest)

    ##################################################################################
    def stretch_rule_slim(self, body):

        minr_shoulder = body.shoulder - 0.06 * body.shoulder
        maxr_shoulder = body.shoulder + 0.03 * body.shoulder
        vminr_shoulder = body.shoulder - 0.09 * body.shoulder
        vmaxr_shoulder = body.shoulder + 0.06 * body.shoulder

        minr_waist = body.waist - 0.06 * body.waist
        maxr_waist = body.waist + 0.03 * body.waist
        vminr_waist = body.waist - 0.09 * body.waist
        vmaxr_waist = body.waist + 0.06 * body.waist

        minr_chest = body.chest - 0.06 * body.chest
        maxr_chest = body.chest + 0.03 * body.chest
        vminr_chest = body.chest - 0.09 * body.chest
        vmaxr_chest = body.chest + 0.06 * body.chest

        minr_seat = body.seat - 0.06 * body.seat
        maxr_seat = body.seat + 0.03 * body.seat
        vminr_seat = body.seat - 0.09 * body.seat
        vmaxr_seat = body.seat + 0.06 * body.seat

        if (self.waist != 0):
            if ((self.waist >= minr_waist) and (self.waist <= maxr_waist)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.waist < minr_waist) and (self.waist >= vminr_waist)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.waist < vminr_waist):
                self.location.append("waist")
                self.accept.append("too tight")
            elif ((self.waist > maxr_waist) and (self.waist <= vmaxr_waist)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.waist > vminr_waist):
                self.location.append("waist")
                self.accept.append("too loose")

        if (self.seat != 0):
            if ((self.seat >= minr_seat) and (self.seat <= maxr_seat)):
                self.location.append("seat")
                self.accept.append("perfect fit")
            elif ((self.seat < minr_seat) and (self.seat >= vminr_seat)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.seat < vminr_seat):
                self.location.append("seat")
                self.accept.append("too tight")
            elif ((self.seat > maxr_seat) and (self.seat <= vmaxr_seat)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.seat > vminr_seat):
                self.location.append("seat")
                self.accept.append("too loose")

        if (self.chest != 0):
            if ((self.chest >= minr_chest) and (self.chest <= maxr_chest)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.chest < minr_chest) and (self.chest >= vminr_chest)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.chest < vminr_chest):
                self.location.append("chest")
                self.accept.append("too tight")
            elif ((self.chest > maxr_chest) and (self.chest <= vmaxr_chest)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.chest > vminr_chest):
                self.location.append("chest")
                self.accept.append("too loose")

        if (self.shoulder != 0):
            if ((self.shoulder >= minr_shoulder) and (self.shoulder <= maxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("perfect fit")
            elif ((self.shoulder < minr_shoulder) and (self.shoulder >= vminr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.shoulder < vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too tight")
            elif ((self.shoulder > maxr_shoulder) and (self.shoulder <= vmaxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.shoulder > vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too loose")

    ##################################################################################
    def stretch_rule_tailord(self, body):

        minr_shoulder = body.shoulder - 0.03 * body.shoulder
        maxr_shoulder = body.shoulder + 0.06 * body.shoulder
        vminr_shoulder = body.shoulder - 0.05 * body.shoulder
        vmaxr_shoulder = body.shoulder + 0.09 * body.shoulder

        minr_waist = body.waist - 0.03 * body.waist
        maxr_waist = body.waist + 0.06 * body.waist
        vminr_waist = body.waist - 0.05 * body.waist
        vmaxr_waist = body.waist + 0.09 * body.waist

        minr_chest = body.chest - 0.03 * body.chest
        maxr_chest = body.chest + 0.06 * body.chest
        vminr_chest = body.chest - 0.05 * body.chest
        vmaxr_chest = body.chest + 0.09 * body.chest

        minr_seat = body.seat - 0.03 * body.seat
        maxr_seat = body.seat + 0.06 * body.seat
        vminr_seat = body.seat - 0.05 * body.seat
        vmaxr_seat = body.seat + 0.09 * body.seat

        if (self.waist != 0):
            if ((self.waist >= minr_waist) and (self.waist <= maxr_waist)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.waist < minr_waist) and (self.waist >= vminr_waist)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.waist < vminr_waist):
                self.location.append("waist")
                self.accept.append("too tight")
            elif ((self.waist > maxr_waist) and (self.waist <= vmaxr_waist)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.waist > vminr_waist):
                self.location.append("waist")
                self.accept.append("too loose")

        if (self.seat != 0):
            if ((self.seat >= minr_seat) and (self.seat <= maxr_seat)):
                self.location.append("seat")
                self.accept.append("perfect fit")
            elif ((self.seat < minr_seat) and (self.seat >= vminr_seat)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.seat < vminr_seat):
                self.location.append("seat")
                self.accept.append("too tight")
            elif ((self.seat > maxr_seat) and (self.seat <= vmaxr_seat)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.seat > vminr_seat):
                self.location.append("seat")
                self.accept.append("too loose")

        if (self.chest != 0):
            if ((self.chest >= minr_chest) and (self.chest <= maxr_chest)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.chest < minr_chest) and (self.chest >= vminr_chest)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.chest < vminr_chest):
                self.location.append("chest")
                self.accept.append("too tight")
            elif ((self.chest > maxr_chest) and (self.chest <= vmaxr_chest)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.chest > vminr_chest):
                self.location.append("chest")
                self.accept.append("too loose")

        if (self.shoulder != 0):
            if ((self.shoulder >= minr_shoulder) and (self.shoulder <= maxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("perfect fit")
            elif ((self.shoulder < minr_shoulder) and (self.shoulder >= vminr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.shoulder < vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too tight")
            elif ((self.shoulder > maxr_shoulder) and (self.shoulder <= vmaxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.shoulder > vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too loose")

    #########################################################################################
    def stretch_rule_sport(self, body):
        minr_shoulder = body.shoulder - 0.04 * body.shoulder
        maxr_shoulder = body.shoulder + 0.04 * body.shoulder
        vminr_shoulder = body.shoulder - 0.08 * body.shoulder
        vmaxr_shoulder = body.shoulder + 0.08 * body.shoulder

        minr_waist = body.waist - 0.04 * body.waist
        maxr_waist = body.waist + 0.04 * body.waist
        vminr_waist = body.waist - 0.08 * body.waist
        vmaxr_waist = body.waist + 0.08 * body.waist

        minr_chest = body.chest - 0.04 * body.chest
        maxr_chest = body.chest + 0.04 * body.chest
        vminr_chest = body.chest - 0.08 * body.chest
        vmaxr_chest = body.chest + 0.08 * body.chest

        minr_seat = body.seat - 0.04 * body.seat
        maxr_seat = body.seat + 0.04 * body.seat
        vminr_seat = body.seat - 0.08 * body.seat
        vmaxr_seat = body.seat + 0.08 * body.seat

        if (self.waist != 0):
            if ((self.waist >= minr_waist) and (self.waist <= maxr_waist)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.waist < minr_waist) and (self.waist >= vminr_waist)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.waist < vminr_waist):
                self.location.append("waist")
                self.accept.append("too tight")
            elif ((self.waist > maxr_waist) and (self.waist <= vmaxr_waist)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.waist > vminr_waist):
                self.location.append("waist")
                self.accept.append("too loose")

        if (self.seat != 0):
            if ((self.seat >= minr_seat) and (self.seat <= maxr_seat)):
                self.location.append("seat")
                self.accept.append("perfect fit")
            elif ((self.seat < minr_seat) and (self.seat >= vminr_seat)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.seat < vminr_seat):
                self.location.append("seat")
                self.accept.append("too tight")
            elif ((self.seat > maxr_seat) and (self.seat <= vmaxr_seat)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.seat > vminr_seat):
                self.location.append("seat")
                self.accept.append("too loose")

        if (self.chest != 0):
            if ((self.chest >= minr_chest) and (self.chest <= maxr_chest)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.chest < minr_chest) and (self.chest >= vminr_chest)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.chest < vminr_chest):
                self.location.append("chest")
                self.accept.append("too tight")
            elif ((self.chest > maxr_chest) and (self.chest <= vmaxr_chest)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.chest > vminr_chest):
                self.location.append("chest")
                self.accept.append("too loose")

        if (self.shoulder != 0):
            if ((self.shoulder >= minr_shoulder) and (self.shoulder <= maxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("perfect fit")
            elif ((self.shoulder < minr_shoulder) and (self.shoulder >= vminr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.shoulder < vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too tight")
            elif ((self.shoulder > maxr_shoulder) and (self.shoulder <= vmaxr_shoulder)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.shoulder > vminr_shoulder):
                self.location.append("shoulder")
                self.accept.append("too loose")

    ##########################################################################################
    def type1_nonstretch_close(self):

        if (self.chest != 0):
            if ((self.defchest >= 0) and (self.defchest <= 9)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 9) and (self.defchest <= 8)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 8):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 0) and (self.defchest >= -2)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < -2):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 0) and (self.defseat <= 7)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 7) and (self.defseat <= 10)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 10):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 0) and (self.defseat >= -2)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < -2):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 0) and (self.defwaist <= 7.5)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 7.5) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 10):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 0) and (self.defwaist >= -8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -8):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ##############################################################################

    def type1_nonstretch_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 8) and (self.defchest <= 10)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 10) and (self.defchest <= 13)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 13):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 8) and (self.defchest >= 4)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 4):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 5) and (self.defseat <= 8)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 8) and (self.defseat <= 10)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 10):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 5) and (self.defseat >= 3)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 3):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 7) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 10) and (self.defwaist <= 12)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 12):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 7) and (self.defwaist >= 5)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 5):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type1_nonstretch_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 10) and (self.defchest <= 13)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 13) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 20):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10) and (self.defchest >= 8)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 8):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 8) and (self.defseat <= 10)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 10) and (self.defseat <= 15)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 15):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 8) and (self.defseat >= 5)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 5):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 10) and (self.defwaist <= 12)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 12) and (self.defwaist <= 15)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 15):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 10) and (self.defwaist >= 8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 8):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type1_nonstretch_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 13) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 20) and (self.defchest <= 25)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 25):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 13) and (self.defchest >= 10)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 10):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 10) and (self.defseat <= 15)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 15) and (self.defseat <= 18)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 18):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 10) and (self.defseat >= 8)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 8):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 13) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 20) and (self.defwaist <= 25)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 25):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 13) and (self.defwaist >= 10)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 10):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################
    def type1_nonstretch_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 20) and (self.defchest <= 27)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 27) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 30):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 20) and (self.defchest >= 15)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 15):
                self.location.append("chest")
                self.accept.append("too tight")
        if (self.seat != 0):
            if ((self.defseat >= 15) and (self.defseat <= 20)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 20) and (self.defseat <= 24)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 24):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 15) and (self.defseat >= 13)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 13):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 20) and (self.defwaist <= 27)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 27) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 30):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 20) and (self.defwaist >= 15)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 15):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ############################################################################

    ############################################################################

    ##############################################################################

    def type2_nonstretch_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 9) and (self.defchest <= 11)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 11) and (self.defchest <= 15)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 15):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 9) and (self.defchest >= 7)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 7):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 8) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 10) and (self.defwaist <= 11)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 11):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 9) and (self.defwaist >= 8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 8):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type2_nonstretch_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 12) and (self.defchest <= 15)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 15) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 20):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 12) and (self.defchest >= 10)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 10):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 11) and (self.defwaist <= 14)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 14) and (self.defwaist <= 19)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 19):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 11) and (self.defwaist >= 9)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 9):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type2_nonstretch_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 15) and (self.defchest <= 25)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 25) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 30):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 15) and (self.defchest >= 12)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 12):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 14) and (self.defwaist <= 25)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 25) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 30):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 14) and (self.defwaist >= 12)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 12):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################

    def type2_nonstretch_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 25) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 30) and (self.defchest <= 35)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 35):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 25) and (self.defchest >= 20)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 20):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 25) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 30) and (self.defwaist <= 35)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 35):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 25) and (self.defwaist >= 20)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 20):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ############################################################################

    #############################################################################
    #############################################################################

    ##############################################################################

    def type3_nonstretch_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 13) and (self.defchest <= 17)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 17) and (self.defchest <= 19)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 19):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 13) and (self.defchest >= 10)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 10):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 13) and (self.defwaist <= 17)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 17) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 20):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 13) and (self.defwaist >= 10)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 10):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ##########################################################################

    def type3_nonstretch_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 17) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 20) and (self.defchest <= 24)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 24):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 17) and (self.defchest >= 15)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 15):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 17) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 20) and (self.defwaist <= 23)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 23):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 17) and (self.defwaist >= 14)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 14):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type3_nonstretch_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 21) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 30) and (self.defchest <= 35)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 35):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 21) and (self.defchest >= 18)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 18):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 20) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 30) and (self.defwaist <= 35)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 35):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 20) and (self.defwaist >= 16)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 16):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################

    def type3_nonstretch_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 30) and (self.defchest <= 40)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 40) and (self.defchest <= 45)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 45):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 30) and (self.defchest >= 24)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 24):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 30) and (self.defwaist <= 40)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 40) and (self.defwaist <= 45)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 45):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 30) and (self.defwaist >= 25)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 25):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ##########################################################################

    def type1_stretchy_close(self):

        if (self.chest != 0):
            if ((self.defchest >= -2) and (self.defchest <= 5)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 5) and (self.defchest <= 7)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 7):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < -2) and (self.defchest >= -4)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < -4):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= -2) and (self.defseat <= 4)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 4) and (self.defseat <= 8)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 8):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < -2) and (self.defseat >= -4)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < -4):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= -2) and (self.defwaist <= 7.5)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 7.5) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 10):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < -2) and (self.defwaist >= -9)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -9):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 2) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 2) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ##############################################################################

    def type1_stretchy_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 4) and (self.defchest <= 10)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 10) and (self.defchest <= 13)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 13):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 4) and (self.defchest >= 0)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 0):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 3) and (self.defseat <= 8)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 8) and (self.defseat <= 10)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 10):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 3) and (self.defseat >= 1)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 1):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 5) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 10) and (self.defwaist <= 12)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 12):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 5) and (self.defwaist >= 3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type1_stretchy_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 7) and (self.defchest <= 13)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 13) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 20):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 7) and (self.defchest >= 4)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 4):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 6) and (self.defseat <= 10)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 10) and (self.defseat <= 15)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 15):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 6) and (self.defseat >= 4)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 4):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 7) and (self.defwaist <= 12)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 12) and (self.defwaist <= 15)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 15):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 7) and (self.defwaist >= 4)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 4):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type1_stretchy_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 10) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 20) and (self.defchest <= 25)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 25):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10) and (self.defchest >= 8)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 8):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.defseat >= 8) and (self.defseat <= 15)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 15) and (self.defseat <= 18)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 18):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 8) and (self.defseat >= 6)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 6):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 10) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 20) and (self.defwaist <= 25)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 25):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 10) and (self.defwaist >= 8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 8):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################
    def type1_stretchy_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 18) and (self.defchest <= 27)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 27) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 30):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 18) and (self.defchest >= 13)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 13):
                self.location.append("chest")
                self.accept.append("too tight")
        if (self.seat != 0):
            if ((self.defseat >= 13) and (self.defseat <= 20)):
                self.location.append("seat")
                self.accept.append("well fit")

            elif ((self.defseat > 20) and (self.defseat <= 24)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 24):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 13) and (self.defseat >= 11)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 11):
                self.location.append("seat")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 18) and (self.defwaist <= 27)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 27) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 30):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 18) and (self.defwaist >= 13)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 13):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ############################################################################

    ############################################################################

    ##############################################################################

    def type2_stretchy_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 6) and (self.defchest <= 11)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 11) and (self.defchest <= 15)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 15):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 6) and (self.defchest >= 4)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 4):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 5) and (self.defwaist <= 10)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 10) and (self.defwaist <= 11)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 11):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 5) and (self.defwaist >= 3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 3):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type2_stretchy_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 10) and (self.defchest <= 15)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 15) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 20):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10) and (self.defchest >= 8)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 8):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 9) and (self.defwaist <= 14)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 14) and (self.defwaist <= 19)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 19):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 9) and (self.defwaist >= 7)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 7):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type2_stretchy_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 13) and (self.defchest <= 25)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 25) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 30):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 13) and (self.defchest >= 10)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 10):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 10) and (self.defwaist <= 25)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 25) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 30):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 10) and (self.defwaist >= 8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 8):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################

    def type2_stretchy_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 22) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 30) and (self.defchest <= 35)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 35):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 22) and (self.defchest >= 19)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 19):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 22) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 30) and (self.defwaist <= 35)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 35):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 22) and (self.defwaist >= 19)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 19):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ############################################################################

    #############################################################################
    #############################################################################

    ##############################################################################

    def type3_stretchy_fitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 10) and (self.defchest <= 17)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 17) and (self.defchest <= 19)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 19):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10) and (self.defchest >= 8)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 8):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 10) and (self.defwaist <= 17)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 17) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 20):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 10) and (self.defwaist >= 8)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 8):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ##########################################################################

    def type3_stretchy_semifitted(self):
        if (self.chest != 0):
            if ((self.defchest >= 15) and (self.defchest <= 20)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 20) and (self.defchest <= 24)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 24):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 15) and (self.defchest >= 13)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 13):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 15) and (self.defwaist <= 20)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 20) and (self.defwaist <= 23)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 23):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 15) and (self.defwaist >= 13)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 10):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###########################################################################

    def type3_stretchy_loosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 19) and (self.defchest <= 30)):
                self.location.append("chest")
                self.accept.append("well fit")

            elif ((self.defchest > 30) and (self.defchest <= 35)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 35):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 19) and (self.defchest >= 15)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 15):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 18) and (self.defwaist <= 30)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 30) and (self.defwaist <= 35)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 35):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 18) and (self.defwaist >= 14)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 14):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ################################################################################

    def type3_stretchy_veryloosefit(self):
        if (self.chest != 0):
            if ((self.defchest >= 26) and (self.defchest <= 40)):
                self.location.append("chest")
                self.accept.append("well fit")
            elif ((self.defchest > 40) and (self.defchest <= 45)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 45):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 26) and (self.defchest >= 22)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 22):
                self.location.append("chest")
                self.accept.append("too tight")

        if (self.waist != 0):
            if ((self.defwaist >= 26) and (self.defwaist <= 40)):
                self.location.append("waist")
                self.accept.append("well fit")
            elif ((self.defwaist > 40) and (self.defwaist <= 45)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 45):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 26) and (self.defwaist >= 22)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 22):
                self.location.append("waist")
                self.accept.append("too tight")
        if (self.shoulder != 0):
            if ((self.defshoulder >= 3) and (self.defshoulder <= 4)):
                self.location.append("shoulder")
                self.accept.append("well fit")
            elif ((self.defshoulder > 4) and (self.defshoulder <= 6)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defshoulder > 6):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defshoulder < 3) and (self.defshoulder >= 1)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defshoulder < 1):
                self.location.append("shoulder")
                self.accept.append("too tight")

    ###############################################################################

    def pant_rule_nonestretch(self):

        if (self.waist != 0):
            if ((self.defwaist < -3.81) and (self.defwaist >= -8.89)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist > -3.81) and (self.defwaist < 0)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 0):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < -8.89) and (self.defwaist >= -12.7)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -12.7):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.seat >= 5.08) and (self.defseat <= 10.16)):
                self.location.append("shoulder")
                self.accept.append("perfect fit")
            elif ((self.defseat > 10.16) and (self.defseat <= 12.7)):
                self.location.append("shoulder")
                self.accept.append("looser")
            elif (self.defseat > 12.7):
                self.location.append("shoulder")
                self.accept.append("too loose")

            elif ((self.defseat < 5.08) and (self.defseat >= 3.81)):
                self.location.append("shoulder")
                self.accept.append("tighter")
            elif (self.defseat < 3.81):
                self.location.append("shoulder")
                self.accept.append("tighter")

    ##########################################################################
    def pant_rule_stretch(self):

        if (self.waist != 0):
            if ((self.defwaist <= -3.81) and (self.defwaist >= -8.89)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist > -3.81) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 0):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < -8.89) and (self.defwaist >= -12.7)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -12.7):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.seat != 0):
            if ((self.seat >= 3.81) and (self.defseat <= 8.89)):
                self.location.append("seat")
                self.accept.append("perfect fit")
            elif ((self.defseat > 8.89) and (self.defseat <= 11.43)):
                self.location.append("seat")
                self.accept.append("looser")
            elif (self.defseat > 11.43):
                self.location.append("seat")
                self.accept.append("too loose")

            elif ((self.defseat < 3.81) and (self.defseat >= 2.54)):
                self.location.append("seat")
                self.accept.append("tighter")
            elif (self.defseat < 2.54):
                self.location.append("seat")
                self.accept.append("tighter")

    ##############################################################################
    def tshirt_rule(self):

        if (self.waist != 0):
            if ((self.defwaist < 5.08) and (self.defwaist >= -5.08)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist >= 5.08) and (self.defwaist <= 10.16)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 10.16):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < -5.08) and (self.defwaist >= -10.16)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -10.16):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.chest != 0):
            if ((self.chest >= 0) and (self.defchest <= 5.08)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.defchest > 5.08) and (self.defchest <= 12.7)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 12.7):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 0) and (self.defchest >= -5.08)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < -5.08):
                self.location.append("chest")
                self.accept.append("tighter")

    ##################################################################################################

    def shirt_rule_nonestretch(self):

        if (self.waist != 0):
            if ((self.defwaist < 11.43) and (self.defwaist >= 6.35)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist >= 11.43) and (self.defwaist <= 15.24)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 15.24):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 6.35) and (self.defwaist >= 3.81)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 3.81):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.chest != 0):
            if ((self.chest >= 10.16) and (self.defchest <= 13.97)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.defchest > 13.97) and (self.defchest <= 17.78)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 17.78):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10.16) and (self.defchest >= 5.08)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 5.08):
                self.location.append("chest")
                self.accept.append("tighter")

    ################################################################################################

    def shirt_rule_stretch(self):

        if (self.waist != 0):
            if ((self.defwaist < 10.16) and (self.defwaist >= 5.08)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist >= 10.16) and (self.defwaist <= 13.97)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 13.97):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 5.08) and (self.defwaist >= 2.54)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 2.54):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.chest != 0):
            if ((self.chest >= 7.62) and (self.defchest <= 11.43)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.defchest > 11.43) and (self.defchest <= 15.24)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 15.24):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 7.62) and (self.defchest >= 2.54)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 2.54):
                self.location.append("chest")
                self.accept.append("tighter")

    ###############################################################################

    def suit_rule_nonestretch(self):

        if (self.waist != 0):
            if ((self.defwaist < 6.35) and (self.defwaist >= 3.81)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist >= 6.35) and (self.defwaist <= 8.89)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 8.89):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 3.81) and (self.defwaist >= 1.27)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 1.27):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.chest != 0):
            if ((self.chest >= 10.16) and (self.defchest <= 15.24)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.defchest > 15.24) and (self.defchest <= 17.78)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 17.78):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 10.16) and (self.defchest >= 5.08)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 5.08):
                self.location.append("chest")
                self.accept.append("tighter")

    ################################################################################################

    def suit_rule_stretch(self):

        if (self.waist != 0):
            if ((self.defwaist < 5.08) and (self.defwaist >= 2.54)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist >= 5.08) and (self.defwaist <= 7.62)):
                self.location.append("waist")
                self.accept.append("looser")
            elif (self.defwaist > 7.62):
                self.location.append("waist")
                self.accept.append("too loose")

            elif ((self.defwaist < 2.54) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.chest != 0):
            if ((self.chest >= 7.62) and (self.defchest <= 12.7)):
                self.location.append("chest")
                self.accept.append("perfect fit")
            elif ((self.defchest > 12.7) and (self.defchest <= 15.24)):
                self.location.append("chest")
                self.accept.append("looser")
            elif (self.defchest > 15.24):
                self.location.append("chest")
                self.accept.append("too loose")

            elif ((self.defchest < 7.62) and (self.defchest >= 2.54)):
                self.location.append("chest")
                self.accept.append("tighter")
            elif (self.defchest < 2.54):
                self.location.append("chest")
                self.accept.append("tighter")

    ############################################################################

    def gettype(self):
        type1 = ["dress", "culott", "skirt",
                 "jumpsuits"]
        type2 = ["jacket", "jackets"]
        type3 = ["coats"]
        type4 = ["trousers", "jeans", "pant", "short"]
        type5 = ["t-shirts", "polo", "sweaters & cardigans", "Polo Shirts"]
        type6 = ["top", "shirts", "vest", "blous", "blouse", "shirt"]
        type7 = ["hoodies & sweatshirts", "blazer", "suit"]
        if (self.type in type1):
            return "type1"
        elif (self.type in type2):
            return "type2"
        elif (self.type in type3):
            return "type3"
        elif (self.type in type4):
            return "type4"
        elif (self.type in type5):
            return "type5"
        elif (self.type in type6):
            return "type6"
        elif (self.type in type7):
            return "type7"

    ################################################################################
    def rules(self, body):
        self.defference(body)
        self.rating()
        t = self.gettype()
        if self.sporty == True:
            self.stretch_rule_sport(body)
            return 0

        if t == "type4":
            if (self.stretch_percentage <= 25):
                self.pant_rule_nonestretch()
                return 0
            else:
                self.pant_rule_stretch()
                return 0

        if t == "type5":
            self.tshirt_rule()
            return 0

        if t == "type6":
            if (self.stretch_percentage <= 25):
                self.shirt_rule_nonestretch()
                return 0
            else:
                self.shirt_rule_stretch()
                return 0

        if (t == "type7" or t == "type2" or t == "type3"):
            if (self.stretch_percentage <= 25):
                self.suit_rule_nonestretch()
                return 0
            else:
                self.suit_rule_stretch()
                return 0






        elif (self.stretch_percentage > 25) and ((self.fit == "closefit") or (self.fit == "skinny fit")):
            self.stretch_rule_slim(body)
            return 0
        elif (self.stretch_percentage > 25) and (
                (self.fit == "tailord") or (self.fit == "fitted") or (self.fit == "slimfit")):
            self.stretch_rule_tailord(body)
            return 0



        # elif ((self.stretch_percentage >= 3) and (t == "type1") and ((self.fit == "closefit") or(self.fit == "skinny fit"))):
        #     self.type1_stretchy_close()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type1") and ((self.fit == "fitted") or(self.fit == "tailord")or (self.fit == "slim fit")):
        #     self.type1_stretchy_fitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type1") and ((self.fit == "semifit") or (self.fit == "regular fit")):
        #     self.type1_stretchy_semifitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type1") and (self.fit == "loose fit"):
        #     self.type1_stretchy_loosefit()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type1") and (self.fit == "Oversized"):
        #     self.type1_stretchy_veryloosefit()
        #     return 0

        # elif (self.stretch_percentage >= 3) and (t == "type2") and ((self.fit == "fitted")or (self.fit == "slim fit")):
        #     self.type2_stretchy_fitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type2") and ((self.fit == "semifit") or (self.fit == "regular fit")):
        #     self.type2_stretchy_semifitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type2") and (self.fit == "loose fit"):
        #     self.type2_stretchy_loosefit()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type2") and (self.fit == "oversized"):
        #     self.type2_stretchy_veryloosefit()
        #     return 0

        # elif (self.stretch_percentage >= 3) and (t == "type3") and ((self.fit == "fitted")or (self.fit == "slim fit")):
        #     self.type3_stretchy_fitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type3") and ((self.fit == "semifit") or (self.fit == "regular fit")):
        #     self.type3_stretchy_semifitted()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type3") and (self.fit == "loose fit"):
        #     self.type3_stretchy_loosefit()
        #     return 0
        # elif (self.stretch_percentage >= 3) and (t == "type3") and (self.fit == "oversized"):
        #     self.type3_stretchy_veryloosefit()
        #     return 0

        elif ((self.stretch_percentage <= 25) and (t == "type1") and (
                (self.fit == "closefit") or (self.fit == "skinny fit"))):
            self.type1_nonstretch_close()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type1") and (
                (self.fit == "fitted") or (self.fit == "tailord") or (self.fit == "slim fit")):
            self.type1_nonstretch_fitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type1") and (
                (self.fit == "semifit") or (self.fit == "regular fit")):
            self.type1_nonstretch_semifitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type1") and (self.fit == "loose fit"):
            self.type1_nonstretch_loosefit()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type1") and (self.fit == "Oversized"):
            self.type1_nonstretch_veryloosefit()
            return 0

        elif (self.stretch_percentage <= 25) and (t == "type2") and (
                (self.fit == "fitted") or (self.fit == "slim fit")):
            self.type2_nonstretch_fitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type2") and (
                (self.fit == "semifit") or (self.fit == "regular fit")):
            self.type2_nonstretch_semifitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type2") and (self.fit == "loose fit"):
            self.type2_nonstretch_loosefit()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type2") and (self.fit == "oversized"):
            self.type2_nonstretch_veryloosefit()
            return 0

        elif (self.stretch_percentage <= 25) and (t == "type3") and (
                (self.fit == "fitted") or (self.fit == "slim fit")):
            self.type3_nonstretch_fitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type3") and (
                (self.fit == "semifit") or (self.fit == "regular fit")):
            self.type3_nonstretch_semifitted()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type3") and (self.fit == "loose fit"):
            self.type3_nonstretch_loosefit()
            return 0
        elif (self.stretch_percentage <= 25) and (t == "type3") and (self.fit == "oversized"):
            self.type3_nonstretch_veryloosefit()
            return 0


#################################################################################################

class body():
    def __init__(self, chest, waist, seat, shoulder):
        self.shoulder = shoulder
        self.chest = chest
        self.waist = waist
        self.seat = seat


##################################################################################################


class fitsys():
    def __init__(self, fit, stretch_percentage, fabric, denim, type, sporty, sizes, busts, hips, waists, shoulders,
                 bust, hip, waist, shoulder):

        fit = fit.lower()

        # stretchy=stretch_percentage.lower()
        type = type.lower()
        self.type = type
        measure = []
        index = 0

        while (index < len(sizes)):
            temp = garmentmeasure(busts[index], waists[index], hips[index],
                                  shoulders[index], stretch_percentage, type, fit, sporty, sizes[index])
            measure.append(temp)
            index = index + 1
        self.bodymeasue = body(bust, waist, hip, shoulder)
        self.gramentmeasure = measure
        for m in self.gramentmeasure:
            m.rules(self.bodymeasue)

    def get_best_fit(self):
        res = []
        ptypes = ["pant", "trousers", "short", "jeans"]
        tstypes = ["t-shirts", "polo", "sweaters & cardigans", "top", "shirts", "vest", "blous", "blouse", "shirt",
                   "hoodies & sweatshirts", "blazer", "suit"]

        for m in self.gramentmeasure:
            # if (self.type in ptypes):
            #     i=m.location.index("waist")
            #     an=m.accept[i]
            #     temp1=0
            #     if "perfect fit" in an:
            #         temp1=1
            #     elif "as designed" in an:
            #         temp1=2
            #     elif "looser" in an:
            #         temp1=4
            #     elif "tighter" in an:
            #         temp1=8

            #     elif "too tight" in an:
            #         temp1=100
            #     elif "too loose" in an:
            #         temp1=50
            #     elif "tight" in an:
            #         temp1=10

            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)
            # elif (self.type in tstypes):
            #     i=m.location.index("chest")
            #     an=m.accept[i]
            #     temp1=0
            #     if "perfect fit" in an:
            #         temp1=1
            #     elif "as designed" in an:
            #         temp1=2
            #     elif "looser" in an:
            #         temp1=4
            #     elif "tighter" in an:
            #         temp1=8

            #     elif "too tight" in an:
            #         temp1=100
            #     elif "too loose" in an:
            #         temp1=50
            #     elif "tight" in an:
            #         temp1=10
            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)

            # else:
            #     temp1 = len([x for x in m.accept if x == "perfect fit"])
            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)
            temp1 = len([x for x in m.accept if x == "perfect fit"])
            temp2 = len([x for x in m.accept if x == "looser"])
            temp3 = len([x for x in m.accept if x == "tighter"])
            temp5 = len([x for x in m.accept if x == "too tight"])
            temp6 = len([x for x in m.accept if x == "too loose"])
            temp4 = temp1 + (4 * temp2) + (8 * temp3) + (100 * temp5) + (50 * temp6)
            res.append(temp4)
        ind, max_value = min(enumerate(res), key=operator.itemgetter(1))

        return self.gramentmeasure[ind]

    def notfit(self):
        n = 0
        for m in self.gramentmeasure:
            # m.rules(self.bodymeasue)
            length = len(m.accept)
            temp1 = len([x for x in m.accept if x == "too loose"])
            temp2 = len([x for x in m.accept if x == "too tight"])
            if ((temp1 == length) or (temp2 == length)):
                n = n + 1

        if (n == len(self.gramentmeasure)):
            return True
        return False

    def get_fitted(self):

        if (self.notfit()):
            return "none"
        res = []
        ptypes = ["pant", "trousers", "short", "jeans"]
        tstypes = ["t-shirts", "polo", "sweaters & cardigans", "top", "shirts", "vest", "blous", "blouse", "shirt",
                   "hoodies & sweatshirts", "blazer", "suit"]
        for m in self.gramentmeasure:
            # m.rules(self.bodymeasue)
            # if (self.type in ptypes):
            #     i=m.location.index("waist")
            #     an=m.accept[i]
            #     temp1=0
            #     if "perfect fit" in an:
            #         temp1=1
            #     elif "as designed" in an:
            #         temp1=2
            #     elif "looser" in an:
            #         temp1=4
            #     elif "tighter" in an:
            #         temp1=8

            #     elif "too tight" in an:
            #         temp1=100
            #     elif "too loose" in an:
            #         temp1=50
            #     elif "tight" in an:
            #         temp1=10

            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)
            # elif (self.type in tstypes):
            #     i=m.location.index("chest")
            #     an=m.accept[i]
            #     temp1=0
            #     if "perfect fit" in an:
            #         temp1=1
            #     elif "as designed" in an:
            #         temp1=2
            #     elif "looser" in an:
            #         temp1=4
            #     elif "tighter" in an:
            #         temp1=8

            #     elif "too tight" in an:
            #         temp1=100
            #     elif "too loose" in an:
            #         temp1=50
            #     elif "tight" in an:
            #         temp1=10
            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)

            # else:
            #     temp1 = len([x for x in m.accept if x == "perfect fit"])
            #     temp2 = len([x for x in m.accept if x == "looser"])
            #     temp3 = len([x for x in m.accept if x == "tighter"])
            #     temp5 = len([x for x in m.accept if x == "too tight"])
            #     temp6 = len([x for x in m.accept if x == "too loose"])
            #     temp4=temp1+(4*temp2)+(8*temp3)+(100*temp5)+(50*temp6)
            #     res.append(temp4)
            temp1 = len([x for x in m.accept if x == "perfect fit"])
            temp2 = len([x for x in m.accept if x == "looser"])
            temp3 = len([x for x in m.accept if x == "tighter"])
            temp5 = len([x for x in m.accept if x == "too tight"])
            temp6 = len([x for x in m.accept if x == "too loose"])
            temp4 = temp1 + (4 * temp2) + (8 * temp3) + (100 * temp5) + (50 * temp6)
            res.append(temp4)
        result = []
        ind, max_value = min(enumerate(res), key=operator.itemgetter(1))
        if (ind + 1 >= len(res)):
            result.append(self.gramentmeasure[ind - 2])
        if (ind - 1 > 0):
            result.append(self.gramentmeasure[ind - 1])

        result.append(self.gramentmeasure[ind])

        if (ind + 1 < len(res)):
            result.append(self.gramentmeasure[ind + 1])
        if (ind - 1 < 0):
            result.append(self.gramentmeasure[ind + 2])

        return result

# sizes = [ 's', 'm', 'l','xl','xxl','xxxl']
# hips = [0]*6
# busts= [100,104,108,112,116,120]
# shoulders = [0]*6
# waists = [74,80,84,88,92,96]
# obj = fitsys("fitted", 14, "suit", False, sizes, busts,
#                hips, waists, shoulders, 100,107, 85, 40)
# # # # #
# # # # # # result is smallest three sizes
# t = obj.get_fitted()

# t=obj.gramentmeasure
# # # #print ("dress")
# if(type(t) is str):
#       print (t)
# # # # #
# else:
#     for m in t:
#         print ("size : " + m.size)
# # # # #
#         ind = 0
#         while(ind < len(m.location)):
#              print (m.location[ind] + "  :   " + m.accept[ind])
#              ind = ind + 1
#         print (" ____________________________________________")
