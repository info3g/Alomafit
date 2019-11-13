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
    def __init__(self, bust, waist, hip, shoulder, stretch_percentage, type, fit, sporty, size, denim, fabric):
        self.bust = bust
        self.hip = hip
        self.waist = waist
        self.shoulder = shoulder
        self.stretch_percentage = stretch_percentage
        self.type = type
        self.fit = fit
        self.sporty = sporty
        self.denim = denim
        self.fabric = fabric

        self.location = []
        self.accept = []
        self.rate = 0
        self.defwaist = 0
        self.defbust = 0
        self.defhip = 0
        self.defshoulder = 0

        self.size = size

    def defference(self, bodymeasurements):
        if (self.bust != 0):
            self.defbust = self.bust - bodymeasurements.bust
        if (self.hip != 0):
            self.defhip = self.hip - bodymeasurements.hip
        if (self.waist != 0):
            self.defwaist = self.waist - bodymeasurements.waist
        if (self.shoulder != 0):
            self.defshoulder = self.shoulder - bodymeasurements.shoulder

    def rating(self):
        self.rate = abs(self.defhip) + abs(self.defshoulder) + \
                    abs(self.defwaist) + abs(self.defbust)

    #######################################################################################

    def nstretch_rule_btm1(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 1.5):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0.5) and (self.defwaist < 1.5)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 0.5)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")

            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ###########################################
    def nstretch_rule_btm2(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 1):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 1)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser,Relaxed fit")

            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ##############################################

    def nstretch_rule_btm3(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("Perfect Fit , Relaxed fit, as designed")

            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("Fitted")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################
    def nstretch_rule_btm4(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 7):
                self.location.append("hip")
                self.accept.append("Too loose, you will lose the shape")


            elif ((self.defhip > 4) and (self.defhip <= 7)):
                self.location.append("hip")
                self.accept.append("Looser, Over sized")

            if ((self.defhip >= 2) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("Perfect fit, Loose fit")
            elif ((self.defhip < 2) and (self.defhip >= 0)):
                self.location.append("hip")
                self.accept.append("Tighter, Fitted")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("Tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ##############################################
    def stretch_rule_btm1(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 1.5):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0.5) and (self.defwaist < 1.5)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 0.5)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")

            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    #############################################
    def stretch_rule_btm2(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 1.5):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 1.5)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3.5)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3.5):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")

            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    #############################################
    def stretch_rule_btm3(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 1):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 1)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser,relaxed fit")

            if ((self.defhip >= 1.5) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 1.5) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################
    def stretch_rule_btm4(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 1):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 1)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3.5)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3.5):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser,relaxed fit")

            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################
    def stretch_rule_btm5(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("Over sized")


            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("Perfect Fit , Relaxed fit, as designed")

            if ((self.defhip >= 2) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("Fitted")
            elif ((self.defhip < 2) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

                ###############################################

    def stretch_rule_btm6(self, body):

        if (self.waist != 0):
            if (self.defwaist >= 1):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0) and (self.defwaist < 1)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3.5)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3.5):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("Perfect Fit , Relaxed fit, as designed")

            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("Fitted")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    #######################################################################

    def nstretch_rule_skrt1(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0.5) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            elif ((self.defwaist >= -2) and (self.defwaist <= 0.5)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):
            if (self.defhip >= 3):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 2) and (self.defhip < 3)):
                self.location.append("hip")
                self.accept.append("looser")

            elif ((self.defhip >= 0) and (self.defhip <= 2)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1.5)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ###########################################################################
    def nstretch_rule_skrt2(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 1) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 1)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("Over sized")


            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("Perfect Fit , Relaxed fit, as designed")

            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("Fitted")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

    #############################################################################
    def nstretch_rule_skrt3(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 1) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 1)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 2):
                self.location.append("hip")
                self.accept.append("As designed")


            elif ((self.defhip > 0) and (self.defhip <= 2)):
                self.location.append("hip")
                self.accept.append("Tighter, Fitted")


            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ##############################################################################
    def nstretch_rule_skrt4(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 1) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 1)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("As designed")


            elif ((self.defhip > 2) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("Tighter, Fitted")


            elif (self.defhip < 2):
                self.location.append("hip")
                self.accept.append("You will lose the shape")

    ##########################################################################
    def stretch_rule_skrt1(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 1.5):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0.5) and (self.defwaist < 1.5)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2.5) and (self.defwaist <= 0.5)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2.5) and (self.defwaist >= -3.5)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3.5):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 3):
                self.location.append("hip")
                self.accept.append("too loose,Over sized")


            elif ((self.defhip > 1) and (self.defhip < 3)):
                self.location.append("hip")
                self.accept.append("looser")

            if ((self.defhip >= -1) and (self.defhip <= 1)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < -1) and (self.defhip >= -2.5)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -2.5):
                self.location.append("hip")
                self.accept.append("too tight")

    #######################################################################
    def stretch_rule_skrt2(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 0.5) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 0.5)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("Over sized")


            elif ((self.defhip > 2) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("Perfect Fit , Relaxed fit, as designed")

            if ((self.defhip >= 1) and (self.defhip <= 2)):
                self.location.append("hip")
                self.accept.append("Fitted")
            elif ((self.defhip < -1.5) and (self.defhip >= 1)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ################################################################
    def stretch_rule_skrt3(self, body):
        if (self.waist != 0):
            if (self.defwaist >= 2):
                self.location.append("waist")
                self.accept.append("too loose")
            elif ((self.defwaist > 1) and (self.defwaist < 2)):
                self.location.append("waist")
                self.accept.append("looser")

            if ((self.defwaist >= -2) and (self.defwaist <= 1)):
                self.location.append("waist")
                self.accept.append("perfect fit")
            elif ((self.defwaist < -2) and (self.defwaist >= -3)):
                self.location.append("waist")
                self.accept.append("tighter")
            elif (self.defwaist < -3):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 2):
                self.location.append("hip")
                self.accept.append("As designed")


            elif ((self.defhip > 1) and (self.defhip <= 2)):
                self.location.append("hip")
                self.accept.append("Tighter, Fitted")


            elif ((self.defhip < 1) and (self.defhip >= -1.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ##################################################################################
    def nstretch_rule_top1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    ###################################################################################
    def nstretch_rule_top2(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    ######################################################################################
    def nstretch_rule_top3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    #####################################################################################
    def nstretch_rule_top4(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    #################################################################################
    def stretch_rule_top1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    #######################################################################################
    def stretch_rule_top2(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

    ###########################################################################################
    def stretch_rule_top3(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    ###########################################################################################
    def stretch_rule_top4(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

    ########################################################################
    def stretch_rule_top5(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    #########################################################################
    def stretch_rule_top6(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

    ##########################################################################

    def stretch_rule_top7(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("over sized")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    ############################################################
    def hoody_rule(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized as designed")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("loose as designed")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    ############################################################

    def onesize_rule(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized as designed")
            elif ((self.defbust > 5) and (self.defbust < 8)):
                self.location.append("bust")
                self.accept.append("loose as designed")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")
            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

    ##############################################################
    def nstretch_rule_jac1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 10):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 6) and (self.defbust <= 10)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 6) and (self.defbust >= 4.5)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4.5) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit,fitted")
            elif ((self.defbust < 3) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ############################################################
    def nstretch_rule_jac2(self, body):

        if (self.bust != 0):
            if (self.defbust >= 10):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 6) and (self.defbust <= 10)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 6) and (self.defbust >= 4.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, semi fitted, relaxed fit")
            elif ((self.defbust < 4.5) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ################################################################

    def nstretch_rule_jac3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 10):
                self.location.append("bust")
                self.accept.append("oversized as designed")

            elif ((self.defbust >= 6) and (self.defbust <= 10)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose as designed")
            elif ((self.defbust < 6) and (self.defbust >= 4.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, semi fitted, relaxed fit")
            elif ((self.defbust < 4.5) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("close fit")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("tighter")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ##############################################################################
    def stretch_rule_jac1(self, body):
        if (self.bust != 0):
            if (self.defbust >= 9):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 5) and (self.defbust <= 9)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("perfect fit,fitted")
            elif ((self.defbust < 2) and (self.defbust >= -1)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ################################################################################
    def stretch_rule_jac2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 9):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 5) and (self.defbust <= 9)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 5) and (self.defbust >= 3.5)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 3.5) and (self.defbust >= -1)):
                self.location.append("bust")
                self.accept.append("perfect fit,fitted")
            elif ((self.defbust < -1) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -2):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ###############################################################################
    def stretch_rule_jac3(self, body):

        if (self.bust != 0):
            if (self.defbust >= 9):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 5) and (self.defbust <= 9)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("perfect fit,fitted")
            elif ((self.defbust < 2) and (self.defbust >= -1)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ##############################################################################
    def stretch_rule_jac4(self, body):

        if (self.bust != 0):
            if (self.defbust >= 9):
                self.location.append("bust")
                self.accept.append("over sized")

            elif ((self.defbust >= 5) and (self.defbust <= 9)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 5) and (self.defbust >= 3.5)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 3.5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 1) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -2):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ###############################################################################
    def stretch_rule_jac5(self, body):

        if (self.bust != 0):
            if (self.defbust >= 9):
                self.location.append("bust")
                self.accept.append("oversized as designed")

            elif ((self.defbust >= 5) and (self.defbust <= 9)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose as designed")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 2) and (self.defbust >= -1)):
                self.location.append("bust")
                self.accept.append("close fit")
            elif (self.defbust < -1):
                self.location.append("bust")
                self.accept.append("tighter")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("oversized as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ##########################################################################

    def nstretch_rule_cot1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ###############################################################################

    def nstretch_rule_cot2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    #############################################################################

    def nstretch_rule_cot3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized, as designed")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose, as designed")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("oversized, as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ################################################################################

    def stretch_rule_cot1(self, body):
        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    #######################################################################

    def stretch_rule_cot2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 6)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 6) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 4) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ###############################################################################

    def stretch_rule_cot3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ##############################################################################

    def stretch_rule_cot4(self, body):

        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("loose")
            elif ((self.defbust < 8) and (self.defbust >= 6)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 6) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 4) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    ############################################################################

    def stretch_rule_cot5(self, body):

        if (self.bust != 0):
            if (self.defbust >= 12):
                self.location.append("bust")
                self.accept.append("oversized, as designed")

            elif ((self.defbust >= 8) and (self.defbust <= 12)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose, as designed")
            elif ((self.defbust < 8) and (self.defbust >= 7)):
                self.location.append("bust")
                self.accept.append("relaxed fit")
            elif ((self.defbust < 7) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 5) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("tighter ")
            elif (self.defbust < 1):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("oversized, as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -1):
                self.location.append("waist")
                self.accept.append("too tight,no closure")

    #############################################################################
    def nstretch_rule_jmp1(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

            ###############################################################################

    def nstretch_rule_jmp2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

            ###############################################################################

    def nstretch_rule_jmp3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit , relaxed fit, as designed")
            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")
            ###############################################################################

    def nstretch_rule_jmp4(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized as designed")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose as designed")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, as designed")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit, as designed")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 7):
                self.location.append("hip")
                self.accept.append("too loose, you will lose the shape")
            elif ((self.defhip > 4) and (self.defhip <= 7)):
                self.location.append("hip")
                self.accept.append("looser, over sized")
            if ((self.defhip >= 2) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("perfect fit, loose fit")
            elif ((self.defhip < 2) and (self.defhip >= 0)):
                self.location.append("hip")
                self.accept.append("tighter, fitted")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ###############################################################################
    def stretch_rule_jmp1(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

            ###############################################################################

    def stretch_rule_jmp2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

            ###############################################################################

    def stretch_rule_jmp3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 1.5) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 1.5) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

            ###############################################################################

    def stretch_rule_jmp4(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter,skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")
            ###############################################################################

    def stretch_rule_jmp5(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("over sized")
            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit , relaxed fit, as designed")
            if ((self.defhip >= 1.5) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 1.5) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ###############################################################################
    def stretch_rule_jmp6(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit , relaxed fit, as designed")
            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    ###############################################################################
    def stretch_rule_jmp7(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized as designed")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("perfect fit, loose as designed")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("semi fitted, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 7):
                self.location.append("hip")
                self.accept.append("too loose, you will lose the shape")
            elif ((self.defhip > 4) and (self.defhip <= 7)):
                self.location.append("hip")
                self.accept.append("looser, over sized")
            if ((self.defhip >= 2) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("perfect fit, loose fit")
            elif ((self.defhip < 2) and (self.defhip >= 0)):
                self.location.append("hip")
                self.accept.append("tighter, fitted")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ###############################################################################

    def rule_drs0(self, body):

        if (self.bust != 0):
            if (self.defbust >= 5):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 5)):
                self.location.append("bust")
                self.accept.append("looser")

            elif ((self.defbust < 4) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")

            elif ((self.defbust < 1.5) and (self.defbust >= 0.75)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 5):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 2.5) and (self.defwaist < 5)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 1.5) and (self.defwaist <= 2.5)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 1.5) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    ###############################################################################

    def rule_drs1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 6):
                self.location.append("bust")
                self.accept.append("too loose")

            elif ((self.defbust >= 4) and (self.defbust <= 6)):
                self.location.append("bust")
                self.accept.append("looser")

            elif ((self.defbust < 4) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")


            elif ((self.defbust < 1) and (self.defbust >= -0.5)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -0.5):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 5):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 2.5) and (self.defwaist < 5)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 1.5) and (self.defwaist <= 2.5)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 1.5) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

    ############################################################################
    def nstretch_rule_drs1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif (self.defbust < 1.5) and (self.defbust >= 0.75):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def nstretch_rule_drs2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif (self.defbust < 1.5) and (self.defbust >= 0.75):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def nstretch_rule_drs3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1.5)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif (self.defbust < 1.5) and (self.defbust >= 0.75):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0.75):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= 0.5)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < 0.5) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("as designed")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit, as designed")
            if ((self.defhip >= 2) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 2) and (self.defhip >= -0.5)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -0.5):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def stretch_rule_drs1(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif (self.defbust < 1) and (self.defbust >= 0):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def stretch_rule_drs2(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("looser, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("perfect fit, close fit")

            elif (self.defbust < -2) and (self.defbust >= -3):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 4):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 4)):
                self.location.append("hip")
                self.accept.append("looser")
            if ((self.defhip >= 0) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 0) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def stretch_rule_drs3(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif (self.defbust < 1) and (self.defbust >= 0):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= 0)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < 0):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 2) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 2) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def stretch_rule_drs4(self, body):
        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("loose, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("perfect fit, fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif (self.defbust < -2) and (self.defbust >= -3):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("too loose, over sized")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("looser, relaxed fit")
            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("perfect fit")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    ############################################################################
    def stretch_rule_drs5(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 5)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 3)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 3) and (self.defbust >= 1)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < 1) and (self.defbust >= 0)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < 0):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 3) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 3) and (self.defwaist >= -1)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -1) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -2):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("as designed")
            elif ((self.defhip > 3.5) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit, as designed")
            if ((self.defhip >= 2) and (self.defhip <= 3.5)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 2) and (self.defhip >= -1)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -1):
                self.location.append("hip")
                self.accept.append("too tight")

    ##
    ############################################################################
    def stretch_rule_drs6(self, body):

        if (self.bust != 0):
            if (self.defbust >= 8):
                self.location.append("bust")
                self.accept.append("oversized")

            elif ((self.defbust >= 5) and (self.defbust <= 8)):
                self.location.append("bust")
                self.accept.append("too loose")
            elif ((self.defbust < 5) and (self.defbust >= 4)):
                self.location.append("bust")
                self.accept.append("perfect fit, relaxed fit")
            elif ((self.defbust < 4) and (self.defbust >= 2)):
                self.location.append("bust")
                self.accept.append("fitted")
            elif ((self.defbust < 2) and (self.defbust >= -2)):
                self.location.append("bust")
                self.accept.append("close fit")

            elif ((self.defbust < -2) and (self.defbust >= -3)):
                self.location.append("bust")
                self.accept.append("tighter")
            elif (self.defbust < -3):
                self.location.append("bust")
                self.accept.append("too tight")

        if (self.waist != 0):
            if (self.defwaist >= 8):
                self.location.append("waist")
                self.accept.append("too loose, over sized")
            elif ((self.defwaist > 6) and (self.defwaist < 8)):
                self.location.append("waist")
                self.accept.append("loose, relaxed fit")

            elif ((self.defwaist >= 2) and (self.defwaist <= 6)):
                self.location.append("waist")
                self.accept.append("looser, easy fit")
            elif ((self.defwaist < 2) and (self.defwaist >= -2)):
                self.location.append("waist")
                self.accept.append("fitted")
            elif ((self.defwaist < -2) and (self.defwaist >= -4)):
                self.location.append("waist")
                self.accept.append("tighter")

            elif (self.defwaist < -4):
                self.location.append("waist")
                self.accept.append("too tight")

        if (self.hip != 0):

            if (self.defhip >= 5):
                self.location.append("hip")
                self.accept.append("as designed")
            elif ((self.defhip > 3) and (self.defhip <= 5)):
                self.location.append("hip")
                self.accept.append("perfect fit, as designed")
            if ((self.defhip >= 1) and (self.defhip <= 3)):
                self.location.append("hip")
                self.accept.append("fitted")
            elif ((self.defhip < 1) and (self.defhip >= -2)):
                self.location.append("hip")
                self.accept.append("tighter, skinny fit")
            elif (self.defhip < -2):
                self.location.append("hip")
                self.accept.append("too tight")

    ##

    ############################################################################
    ####** GET Product type #############

    def gettype(self):

        type1 = ["Pant", "pant", "trousers", "short"]
        type2 = ["jeans"]
        type3 = ["skirt"]
        type4 = ["top", "tops", "blouses", "tonics shirts", "t-shirts", "vests", "crop top", "shirts"]
        type5 = ["hoodies and sweatshirts"]
        type6 = ["onesize"]
        type7 = ["jackets", "blazer", "light weight jackets"]
        type8 = ["coats", "winter jackets"]
        type9 = ["jumpsuit"]
        type10 = ["fit and flare dress"]
        type11 = ["sheath dress"]
        type12 = ["shift dress"]
        type13 = ["shirt dress"]

        if (self.type in type1):
            return "type1"
        if (self.type in type2):
            return "type2"
        if (self.type in type3):
            return "type3"
        if (self.type in type4):
            return "type4"
        if (self.type in type5):
            return "type5"
        if (self.type in type6):
            return "type6"

        if (self.type in type7):
            return "type7"
        if (self.type in type8):
            return "type8"
        if (self.type in type9):
            return "type9"

        if (self.type in type10):
            return "type10"
        if (self.type in type11):
            return "type11"
        if (self.type in type12):
            return "type12"
        if (self.type in type13):
            return "type13"

    #############################################################################
    ##*** GET Fit Type ****###
    #############################################################################

    def getfit(self):

        type1 = ["skinny", "close fit", "fitted", "slim"]
        type2 = ["regular fit", "semifit", "relaxed fit"]
        type3 = ["loose fit", "oversized"]
        type4 = ["tailored fit"]

        type5 = ["skinny", "close fit"]
        type6 = ["tailored fit", "fitted", "pencil skirt", "straight", "slim"]
        type7 = ["a-line", "relaxed fit", "semifit", "regular fit"]
        type8 = ["pleated", "flared", "gathered"]
        type9 = ["fitted bodice"]
        result = []
        if (self.fit in type1):
            result.append("fit1")
        if (self.fit in type2):
            result.append("fit2")
        if (self.fit in type3):
            result.append("fit3")
        if (self.fit in type4):
            result.append("fit4")
        if (self.fit in type5):
            result.append("fit5")
        if (self.fit in type6):
            result.append("fit6")
        if (self.fit in type7):
            result.append("fit7")
        if (self.fit in type8):
            result.append("fit8")
        if (self.fit in type9):
            result.append("fit9")
        return result

    ################################################################################

    ###   RULES  #####
    ################################################################################

    def rules(self, body):
        self.defference(body)
        self.rating()
        t = self.gettype()
        f = self.getfit()

        if self.sporty == True:
            self.stretch_rule_sport(body)
            return 0



        elif (t == "type1" or t == "type2"):
            if ("fit1" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_btm1(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_btm1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_btm2(body)
                    return 0

            if ("fit4" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_btm2(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_btm3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_btm4(body)
                    return 0

            if ("fit2" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_btm3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_btm5(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_btm6(body)
                    return 0

            if ("fit3" in f):
                if ((self.fabric == "nonestretch") or ((self.fabric == "stretch" and self.stretch_percentage <= 4))):
                    self.nstretch_rule_btm4(body)
                    return 0




        elif (t == "type3"):
            if ("fit5" in f):
                if (self.fabric == "nonestretch") or (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.nstretch_rule_skrt1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_skrt1(body)
                    return 0

            if ("fit6" in f):
                if (self.fabric == "nonestretch") or (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.nstretch_rule_skrt2(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_skrt2(body)
                    return 0

            if ("fit7" in f):
                if (self.fabric == "nonestretch") or (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.nstretch_rule_skrt3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_skrt3(body)
                    return 0

            if ("fit8" in f):
                self.nstretch_rule_skrt4(body)
                return 0


        elif (t == "type4" or t == "type12"):

            if ("fit5" in f):

                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_top1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_top1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_top2(body)
                    return 0

            if ("fit6" in f):

                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_top2(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_top3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):

                    self.stretch_rule_top4(body)
                    return 0

            if ("fit2" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_top3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_top5(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_top6(body)
                    return 0

            if ("fit3" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_top4(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_top7(body)
                    return 0


        elif (t == "type5"):
            self.hoody_rule(body)
            return 0
        elif (t == "type6"):
            self.onesize_rule(body)
            return 0


        elif (t == "type7"):
            if ("fit6" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jac1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jac1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_jac2(body)
                    return 0

            if ("fit2" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jac2(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jac3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_jac4(body)
                    return 0

            if ("fit3" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jac3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jac5(body)
                    return 0

        elif (t == "type8"):
            if ("fit6" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_cot1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_cot1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_cot2(body)
                    return 0

            if ("fit2" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_cot2(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_cot3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_cot4(body)
                    return 0

            if ("fit3" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_cot3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_cot5(body)
                    return 0

        elif (t == "type9" or t == "type13"):
            if ("fit5" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jmp1(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jmp1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_jmp2(body)
                    return 0

            if ("fit6" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jmp2(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jmp3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_jmp4(body)
                    return 0

            if ("fit2" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_jmp3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_jmp5(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_jmp6(body)
                    return 0

            if ("fit3" in f):
                if ((self.fabric == "nonestretch") or ((self.fabric == "stretch" and self.stretch_percentage <= 4))):
                    self.nstretch_rule_jmp4(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4):
                    self.stretch_rule_jmp7(body)
                    return 0


        elif ((t == "type10") and (f == "fit9")):
            if ((self.fabric == "nonestretch") or ((self.fabric == "stretch" and self.stretch_percentage <= 4))):
                self.rule_drs0(body)
                return 0
            elif (self.fabric == "stretch" and self.stretch_percentage > 4):
                self.rule_drs1(body)
                return 0


        elif (t == "type11"):
            if ("fit5" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_drs1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_drs1(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_drs2(body)
                    return 0

            if ("fit2" in f or "fit6" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_drs2(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_drs3(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_drs4(body)
                    return 0

            if ("fit3" in f):
                if (self.fabric == "nonestretch"):
                    self.nstretch_rule_drs3(body)
                    return 0

                elif (self.fabric == "stretch" and self.stretch_percentage <= 4):
                    self.stretch_rule_drs5(body)
                    return 0
                elif (self.fabric == "stretch" and self.stretch_percentage > 4) or (self.fabric == "knitted"):
                    self.stretch_rule_drs6(body)
                    return 0


#################################################################################################

class body():
    def __init__(self, bust, waist, hip, shoulder):
        self.shoulder = shoulder
        self.bust = bust
        self.waist = waist
        self.hip = hip


##################################################################################################


class fitsys():
    def __init__(self, fit, stretch_percentage, fabric, denim, type, sporty, sizes, busts, hips, waists, shoulders,
                 bust, hip, waist, shoulder):

        fit = fit.lower()

        # stretchy=stretch_percentage.lower()
        type = type.lower()
        self.type = type
        self.denim = denim
        self.fabric = fabric.lower()
        measure = []
        index = 0

        while (index < len(sizes)):
            temp = garmentmeasure(busts[index], waists[index], hips[index],
                                  shoulders[index], stretch_percentage, type, fit, sporty, sizes[index], self.denim,
                                  self.fabric)
            measure.append(temp)
            index = index + 1
        self.bodymeasue = body(bust, waist, hip, shoulder)
        self.gramentmeasure = measure
        for m in self.gramentmeasure:
            m.rules(self.bodymeasue)

    def get_best_fit(self):
        res = []
        types = ["dress", "top", "shirts", "blous", "blouses", "tops", "shirt dress", "shift dress", "jumpsuit",
                 "vests", "crop top", "hoodies and sweatshirts", "jackets", "blazer", "light weight jackets", "coats",
                 "winter jackets", "fit and flare dress", "sheath dress"]
        tstypes = ["t-shirts", "polo", "sweaters & cardigans", "tonics shirts"]
        for m in self.gramentmeasure:
            # m.rules(self.bodymeasue)
            if (self.type in types):
                i = m.location.index("bust")
                an = m.accept[i]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    temp1 = 2
                elif "looser" in an:
                    temp1 = 4
                elif "tighter" in an:
                    temp1 = 8

                elif "too tight" in an:
                    temp1 = 100
                elif "too loose" in an:
                    temp1 = 50
                elif "tight" in an:
                    temp1 = 10

                res.append(temp1)


            elif (self.type in tstypes):
                i = m.location.index("bust")
                an = m.accept[i]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    temp1 = 2
                elif "looser" in an:
                    temp1 = 4
                elif "tighter" in an:
                    temp1 = 8

                elif "too tight" in an:
                    temp1 = 100
                elif "too loose" in an:
                    temp1 = 50
                elif "tight" in an:
                    temp1 = 10

                res.append(temp1)
            else:
                i = m.location.index("hip")
                an = m.accept[i]
                i2 = m.location.index("waist")
                an2 = m.accept[i2]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    if "perfect fit" in an2:
                        temp1 = 1
                    else:
                        temp1 = 2
                elif "looser" in an:
                    if "perfect fit" in an2 or "as designed" in an2:
                        temp1 = 2
                    else:
                        temp1 = 4
                elif "tighter" in an:
                    if "perfect fit" in an2 or "as designed" in an2:
                        temp1 = 3
                    else:
                        temp1 = 8

                elif "too tight" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 10
                    else:
                        temp1 = 100

                elif "too loose" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 8
                    else:
                        temp1 = 50
                elif "tight" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 8
                    else:
                        temp1 = 10

                res.append(temp1)

        ind, max_value = min(enumerate(res), key=operator.itemgetter(1))

        return self.gramentmeasure[ind]

    def notfit(self):
        n = 0
        for m in self.gramentmeasure:
            # m.rules(self.bodymeasue)

            length = len(m.accept)
            temp1 = len([x for x in m.accept if "too loose" in x])
            temp2 = len([x for x in m.accept if "too tight" in x])
            if ((temp1 == length) or (temp2 == length)):
                n = n + 1
        if (n == len(self.gramentmeasure)):
            return True
        return False

    def get_fitted(self):

        if (self.notfit()):
            return "none"
        res = []
        types = ["dress", "top", "shirts", "blous", "blouses", "tops", "shirt dress", "shift dress", "jumpsuit",
                 "vests", "crop top", "hoodies and sweatshirts", "jackets", "blazer", "light weight jackets", "coats",
                 "winter jackets", "fit and flare dress", "sheath dress"]
        tstypes = ["t-shirts", "polo", "sweaters & cardigans", "tonics shirts"]
        for m in self.gramentmeasure:
            # m.rules(self.bodymeasue)

            if (self.type in types):
                i = m.location.index("bust")
                an = m.accept[i]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    temp1 = 2
                elif "looser" in an:
                    temp1 = 4
                elif "tighter" in an:
                    temp1 = 8

                elif "too tight" in an:
                    temp1 = 100
                elif "too loose" in an:
                    temp1 = 50
                elif "tight" in an:
                    temp1 = 10

                res.append(temp1)

            elif (self.type in tstypes):
                i = m.location.index("bust")
                an = m.accept[i]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    temp1 = 2
                elif "looser" in an:
                    temp1 = 4
                elif "tighter" in an:
                    temp1 = 8

                elif "too tight" in an:
                    temp1 = 100
                elif "too loose" in an:
                    temp1 = 50
                elif "tight" in an:
                    temp1 = 10

                res.append(temp1)
            else:
                i = m.location.index("hip")
                an = m.accept[i]
                i2 = m.location.index("waist")
                an2 = m.accept[i2]
                temp1 = 0
                if "perfect fit" in an or "fitted" in an:
                    temp1 = 1
                elif "as designed" in an or "relaxed fit" in an:
                    if "perfect fit" in an2:
                        temp1 = 1
                    else:
                        temp1 = 2
                elif "looser" in an:
                    if "perfect fit" in an2 or "as designed" in an2:
                        temp1 = 2
                    else:
                        temp1 = 4
                elif "tighter" in an:
                    if "perfect fit" in an2 or "as designed" in an2:
                        temp1 = 3
                    else:
                        temp1 = 8

                elif "too tight" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 10
                    else:
                        temp1 = 100

                elif "too loose" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 8
                    else:
                        temp1 = 50
                elif "tight" in an:
                    if "perfect fit" in an2 or "as designed" in an2 or "tighter" in an2 or "looser" in an2:
                        temp1 = 8
                    else:
                        temp1 = 10

                res.append(temp1)

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

################


# sizes = [ 's', 'm', 'l','xl','xxl','xxxl']
# busts = [85,90,95,100,105,110]
# hips = [0] *6
# shoulders = [0]*6
# waists = [70,75,80,85,90,95]
# # #(self,Denim, Fabric,fit, stretch_percentage, type, sporty, sizes, busts, hips, waists, shoulders, bust, hip, waist, shoulder):
# obj = fitsys("slim", 0,"knitted", False,"tops", False, sizes, busts,hips, waists, shoulders, 100,99, 72, 40)
# # # # #
# # # # # # result is smallest three sizes
# t = obj.get_fitted()

# # # # #t=obj.gramentmeasure
# # # # print ("dress")
# if(type(t) is str):
#    print (t)
# # # # #
# else:
#     for m in t:
#         print ("size : " + m.size)
# # # # #
#         ind = 0
#         while(ind < len(m.location)):
#             print (m.location[ind] + "  :   " + m.accept[ind])
#             ind = ind + 1
#         print (" ____________________________________________")
