#! /usr/bin/env python 3

class Category:
    def __init__(self, category):
        self.__category = category

    def get_name(self):
        return self.__category

    def set_name(self, category):
        self.__category = category


class Area:
    def __init__(self, area):
        self.__area = area

    def get_name(self):
        return self.__area

    def set_name(self, area):
        self.__area = area


class Meal:
    def __init__(self, meal_id, meal_name, meal_thumb):
        self.__meal_id = meal_id
        self.__meal_name = meal_name
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_name(self):
        return self.__meal_name

    def set_name(self, meal_name):
        self.__meal_name = meal_name

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Instructions:

    def __init__(self, meal_name, meal_steps, meal_ingredients1, meal_ingredients2, meal_ingredients3, meal_ingredients4,
                 meal_ingredients5,
                 meal_ingredients6, meal_ingredients7, meal_ingredients8, meal_ingredients9, meal_ingredients10, 
                 meal_ingredients11, meal_ingredients12, meal_ingredients13, meal_ingredients14, meal_ingredients15,
                 meal_ingredients16, meal_ingredients17, meal_ingredients18, meal_ingredients19, meal_ingredients20, 
                 meal_measures1, meal_measures2, meal_measures3, meal_measures4, 
                 meal_measures5,
                 meal_measures6, meal_measures7, meal_measures8, meal_measures9, meal_measures10, 
                 meal_measures11, meal_measures12, meal_measures13, meal_measures14, meal_measures15,
                 meal_measures16, meal_measures17, meal_measures18, meal_measures19, meal_measures20,):

        self.__meal_name = meal_name
        self.__meal_steps = meal_steps
        self.__meal_ingredients1 = meal_ingredients1
        self.__meal_ingredients2 = meal_ingredients2
        self.__meal_ingredients3 = meal_ingredients3
        self.__meal_ingredients4 = meal_ingredients4
        self.__meal_ingredients5 = meal_ingredients5
        self.__meal_ingredients6 = meal_ingredients6
        self.__meal_ingredients7 = meal_ingredients7
        self.__meal_ingredients8 = meal_ingredients8
        self.__meal_ingredients9 = meal_ingredients9
        self.__meal_ingredients10 = meal_ingredients10
        self.__meal_ingredients11 = meal_ingredients11
        self.__meal_ingredients12 = meal_ingredients12
        self.__meal_ingredients13 = meal_ingredients13
        self.__meal_ingredients14 = meal_ingredients14
        self.__meal_ingredients15 = meal_ingredients15
        self.__meal_ingredients16 = meal_ingredients16
        self.__meal_ingredients17 = meal_ingredients17
        self.__meal_ingredients18 = meal_ingredients18
        self.__meal_ingredients19 = meal_ingredients19
        self.__meal_ingredients20 = meal_ingredients20

        self.__meal_measures1 = meal_measures1
        self.__meal_measures2 = meal_measures2
        self.__meal_measures3 = meal_measures3
        self.__meal_measures4 = meal_measures4
        self.__meal_measures5 = meal_measures5
        self.__meal_measures6 = meal_measures6
        self.__meal_measures7 = meal_measures7
        self.__meal_measures8 = meal_measures8
        self.__meal_measures9 = meal_measures9
        self.__meal_measures10 = meal_measures10
        self.__meal_measures11 = meal_measures11
        self.__meal_measures12 = meal_measures12
        self.__meal_measures13 = meal_measures13
        self.__meal_measures14 = meal_measures14
        self.__meal_measures15 = meal_measures15
        self.__meal_measures16 = meal_measures16
        self.__meal_measures17 = meal_measures17
        self.__meal_measures18 = meal_measures18
        self.__meal_measures19 = meal_measures19
        self.__meal_measures20 = meal_measures20


    # instructions here

    def get_meal_name(self):
        return self.__meal_name

    def get_meal_steps(self):
        return self.__meal_steps

    def set_meal_steps(self, meal_steps):
        self.__meal_steps = meal_steps

    # ingredients start here

    def get_meal_ingredients1(self):
        return self.__meal_ingredients1

    def set_meal_ingredients1(self, meal_ingredients1):
        self.__meal_ingredients1 = meal_ingredients1

    def get_meal_ingredients2(self):
        return self.__meal_ingredients2

    def set_meal_ingredients2(self, meal_ingredients2):
        self.__meal_ingredients2 = meal_ingredients2

    def get_meal_ingredients3(self):
        return self.__meal_ingredients3

    def set_meal_ingredients3(self, meal_ingredients3):
        self.__meal_ingredients3 = meal_ingredients3

    def get_meal_ingredients4(self):
        return self.__meal_ingredients4

    def set_meal_ingredients4(self, meal_ingredients4):
        self.__meal_ingredients4 = meal_ingredients4

    def get_meal_ingredients5(self):
        return self.__meal_ingredients5

    def set_meal_ingredients5(self, meal_ingredients5):
        self.__meal_ingredients5 = meal_ingredients5

    def get_meal_ingredients6(self):
        return self.__meal_ingredients6

    def set_meal_ingredients6(self, meal_ingredients6):
        self.__meal_ingredients6 = meal_ingredients6

    def get_meal_ingredients7(self):
        return self.__meal_ingredients7

    def set_meal_ingredients7(self, meal_ingredients7):
        self.__meal_ingredients7 = meal_ingredients7

    def get_meal_ingredients8(self):
        return self.__meal_ingredients8

    def set_meal_ingredients8(self, meal_ingredients8):
        self.__meal_ingredients8 = meal_ingredients8

    def get_meal_ingredients9(self):
        return self.__meal_ingredients9

    def set_meal_ingredients9(self, meal_ingredients9):
        self.__meal_ingredients9 = meal_ingredients9

    def get_meal_ingredients10(self):
        return self.__meal_ingredients10

    def set_meal_ingredients10(self, meal_ingredients10):
        self.__meal_ingredients10 = meal_ingredients10

    def get_meal_ingredients11(self):
        return self.__meal_ingredients11

    def set_meal_ingredients11(self, meal_ingredients11):
        self.__meal_ingredients11 = meal_ingredients11

    def get_meal_ingredients12(self):
        return self.__meal_ingredients12

    def set_meal_ingredients12(self, meal_ingredients12):
        self.__meal_ingredients12 = meal_ingredients12

    def get_meal_ingredients13(self):
        return self.__meal_ingredients13

    def set_meal_ingredients13(self, meal_ingredients13):
        self.__meal_ingredients13 = meal_ingredients13

    def get_meal_ingredients14(self):
        return self.__meal_ingredients14

    def set_meal_ingredients14(self, meal_ingredients14):
        self.__meal_ingredients14 = meal_ingredients14

    def get_meal_ingredients15(self):
        return self.__meal_ingredients15

    def set_meal_ingredients15(self, meal_ingredients15):
        self.__meal_ingredients15 = meal_ingredients15

    def get_meal_ingredients16(self):
        return self.__meal_ingredients16

    def set_meal_ingredients16(self, meal_ingredients16):
        self.__meal_ingredients16 = meal_ingredients16

    def get_meal_ingredients17(self):
        return self.__meal_ingredients17

    def set_meal_ingredients17(self, meal_ingredients17):
        self.__meal_ingredients17 = meal_ingredients17

    def get_meal_ingredients18(self):
        return self.__meal_ingredients18

    def set_meal_ingredients18(self, meal_ingredients18):
        self.__meal_ingredients18 = meal_ingredients18

    def get_meal_ingredients19(self):
        return self.__meal_ingredients19

    def set_meal_ingredients19(self, meal_ingredients19):
        self.__meal_ingredients19 = meal_ingredients19

    def get_meal_ingredients20(self):
        return self.__meal_ingredients20

    def set_meal_ingredients20(self, meal_ingredients20):
        self.__meal_ingredients20 = meal_ingredients20



    # measures start here

    def get_meal_measures1(self):
        return self.__meal_measures1

    def set_meal_measures1(self, meal_measures1):
        self.__meal_measures1 = meal_measures1

    def get_meal_measures2(self):
        return self.__meal_measures2

    def set_meal_measures2(self, meal_measures2):
        self.__meal_measures2 = meal_measures2

    def get_meal_measures3(self):
        return self.__meal_measures3

    def set_meal_measures3(self, meal_measures3):
        self.__meal_measures3 = meal_measures3

    def get_meal_measures4(self):
        return self.__meal_measures4

    def set_meal_measures4(self, meal_measures4):
        self.__meal_measures4 = meal_measures4

    def get_meal_measures5(self):
        return self.__meal_measures5

    def set_meal_measures5(self, meal_measures5):
        self.__meal_measures5 = meal_measures5

    def get_meal_measures6(self):
        return self.__meal_measures6

    def set_meal_measures6(self, meal_measures6):
        self.__meal_measures6 = meal_measures6

    def get_meal_measures7(self):
        return self.__meal_measures7

    def set_meal_measures7(self, meal_measures7):
        self.__meal_measures7 = meal_measures7

    def get_meal_measures8(self):
        return self.__meal_measures8

    def set_meal_measures8(self, meal_measures8):
        self.__meal_measures8 = meal_measures8

    def get_meal_measures9(self):
        return self.__meal_measures9

    def set_meal_measures9(self, meal_measures9):
        self.__meal_measures9 = meal_measures9

    def get_meal_measures10(self):
        return self.__meal_measures10

    def set_meal_measures10(self, meal_measures10):
        self.__meal_measures10 = meal_measures10

    def get_meal_measures11(self):
        return self.__meal_measures11

    def set_meal_measures11(self, meal_measures11):
        self.__meal_measures11 = meal_measures11

    def get_meal_measures12(self):
        return self.__meal_measures12

    def set_meal_measures12(self, meal_measures12):
        self.__meal_measures12 = meal_measures12

    def get_meal_measures13(self):
        return self.__meal_measures13

    def set_meal_measures13(self, meal_measures13):
        self.__meal_measures13 = meal_measures13

    def get_meal_measures14(self):
        return self.__meal_measures14

    def set_meal_measures14(self, meal_measures14):
        self.__meal_measures14 = meal_measures14

    def get_meal_measures15(self):
        return self.__meal_measures15

    def set_meal_measures15(self, meal_measures15):
        self.__meal_measures15 = meal_measures15

    def get_meal_measures16(self):
        return self.__meal_measures16

    def set_meal_measures16(self, meal_measures16):
        self.__meal_measures16 = meal_measures16

    def get_meal_measures17(self):
        return self.__meal_measures17

    def set_meal_measures17(self, meal_measures17):
        self.__meal_measures17 = meal_measures17

    def get_meal_measures18(self):
        return self.__meal_measures18

    def set_meal_measures18(self, meal_measures18):
        self.__meal_measures18 = meal_measures18

    def get_meal_measures19(self):
        return self.__meal_measures19

    def set_meal_measures19(self, meal_measures19):
        self.__meal_measures19 = meal_measures19

    def get_meal_measures20(self):
        return self.__meal_measures20

    def set_meal_measures20(self, meal_measures20):
        self.__meal_measures20 = meal_measures20
