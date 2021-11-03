#! /usr/bin/env python 3
import requests
import sys
import textwrap


def show_title():
    # displays title to the screen

    print("My Recipe Program")
    print()


def show_menu():
    # displays menu to screen

    print("COMMAND MENU")
    print("1 - List all categories")
    print("2 - List all meals for categories")
    print("3 - Search meal by name")
    print("4 - Random meal")
    print("5 - List all areas")
    print("6 - Search meals by area")
    print("7 - Menu")
    print("0 - Exit the program")
    print()


def list_categories():
    # gets and displays the list of categories to the screen

    categories = requests.get_categories()
    if categories is None:
        print("Technical difficulties, please try again later")
    else:
        print("CATEGORIES")
        for i in range(len(categories)):
            category = categories[i]
            print(" " + category.get_name())
        print()


def list_areas():
    # gets and displays the list of areas to the screen

    areas = requests.get_areas()
    if areas is None:
        print("Technical difficulties, please try again later")
    else:
        print("AREAS")
        for i in range(len(areas)):
            area = areas[i]
            print(" " + area.get_name())
        print()


def list_meals(title, meals):
    # displays the list of meals for a category or area to screen
    if meals is None:
        print("Technical difficulties, please try again later")
    else:
        print(title.upper(), "MEALS")
        for i in range(len(meals)):
            meal = meals[i]
            print(" " + meal.get_name())
        print()


def list_meals_by_category():
    # prompts user for a category and gets meal list if category is valid

    lookup_category = input("Enter a category: ")

    categories = requests.get_categories()
    found = False
    print()

    if categories is None:
        print("Technical difficulties, please try again later")
    else:
        for i in range(len(categories)):
            category = categories[i]
            if category.get_name().lower() == lookup_category.lower():
                found = True
                break

    if found:
        meals = requests.get_meals_by_category(lookup_category)
        list_meals(lookup_category, meals)
    else:
        print("Invalid category, please try again.")


def list_meals_by_area():
    # prompts user for an area and gets meal list if area is valid

    lookup_area = input("Enter an area: ")

    areas = requests.get_areas()
    found = False
    print()

    if areas is None:
        print("Technical difficulties, please try again later")
    else:
        for i in range(len(areas)):
            area = areas[i]
            if area.get_name().lower() == lookup_area.lower():
                found = True
                break

    if found:
        meals = requests.get_meals_by_area(lookup_area)
        list_meals(lookup_area, meals)
    else:
        print("Invalid area, please try again.")


def search_meals_by_name():
    lookup_meal = input("Enter meal name: ")

    meal = requests.get_meals_by_name(lookup_meal)
    print("Recipe: ", lookup_meal)
    print()

    my_wrap = textwrap.TextWrapper(width=80)
    print("Instructions:")
    wrap_list = my_wrap.wrap(meal.get_meal_steps())

    for line in wrap_list:
        print(line)

    print()

    print("Measure           Ingredient\n")
    # print("Measure: ", meal.get_meal_measures())


    if not (meal.get_meal_measures1() is None and meal.get_meal_ingredients1() is None):
        print(meal.get_meal_measures1() + "               " + meal.get_meal_ingredients1())

    if not (meal.get_meal_measures2() is None and meal.get_meal_ingredients2() is None):
        print(meal.get_meal_measures2() + "               " + meal.get_meal_ingredients2())

    if not (meal.get_meal_measures3() is None and meal.get_meal_ingredients3() is None):
        print(meal.get_meal_measures3() + "               " + meal.get_meal_ingredients3())

    if not (meal.get_meal_measures4() is None and meal.get_meal_ingredients4() is None):
        print(meal.get_meal_measures4() + "               " + meal.get_meal_ingredients4())

    if not (meal.get_meal_measures5() is None and meal.get_meal_ingredients5() is None):
        print(meal.get_meal_measures5() + "               " + meal.get_meal_ingredients5())

    if not (meal.get_meal_measures6() is None and meal.get_meal_ingredients6() is None):
        print(meal.get_meal_measures6() + "               " + meal.get_meal_ingredients6())

    if not (meal.get_meal_measures7() is None and meal.get_meal_ingredients7() is None):
        print(meal.get_meal_measures7() + "               " + meal.get_meal_ingredients7())

    if not (meal.get_meal_measures8() is None and meal.get_meal_ingredients8() is None):
        print(meal.get_meal_measures8() + "               " + meal.get_meal_ingredients8())

    if not (meal.get_meal_measures9() is None and meal.get_meal_ingredients9() is None):
        print(meal.get_meal_measures9() + "               " + meal.get_meal_ingredients9())

    if not (meal.get_meal_measures10() is None and meal.get_meal_ingredients10() is None):
        print(meal.get_meal_measures10() + "               " + meal.get_meal_ingredients10())

    if not (meal.get_meal_measures11() is None and meal.get_meal_ingredients11() is None):
        print(meal.get_meal_measures11() + "               " + meal.get_meal_ingredients11())

    if not (meal.get_meal_measures12() is None and meal.get_meal_ingredients12() is None):
        print(meal.get_meal_measures12() + "               " + meal.get_meal_ingredients12())

    if not (meal.get_meal_measures13() is None and meal.get_meal_ingredients13() is None):
        print(meal.get_meal_measures13() + "               " + meal.get_meal_ingredients13())

    if not (meal.get_meal_measures14() is None and meal.get_meal_ingredients14() is None):
        print(meal.get_meal_measures14() + "               " + meal.get_meal_ingredients14())

    if not (meal.get_meal_measures15() is None and meal.get_meal_ingredients15() is None):
        print(meal.get_meal_measures15() + "               " + meal.get_meal_ingredients15())

    if not (meal.get_meal_measures16() is None and meal.get_meal_ingredients16() is None):
        print(meal.get_meal_measures16() + "               " + meal.get_meal_ingredients16())

    if not (meal.get_meal_measures17() is None and meal.get_meal_ingredients17() is None):
        print(meal.get_meal_measures17() + "               " + meal.get_meal_ingredients17())

    if not (meal.get_meal_measures18() is None and meal.get_meal_ingredients18() is None):
        print(meal.get_meal_measures18() + "               " + meal.get_meal_ingredients18())

    if not (meal.get_meal_measures19() is None and meal.get_meal_ingredients19() is None):
        print(meal.get_meal_measures19() + "               " + meal.get_meal_ingredients19())

    if not (meal.get_meal_measures20() is None and meal.get_meal_ingredients20() is None):
        print(meal.get_meal_measures20() + "               " + meal.get_meal_ingredients20())


    print()

def random_meal():
    print("A random meal was selected for you!")

    meal = requests.get_random_meal()
    print("Recipe: ", meal.get_meal_name())
    print()

    my_wrap = textwrap.TextWrapper(width=80)
    print("Instructions:")
    wrap_list = my_wrap.wrap(meal.get_meal_steps())

    for line in wrap_list:
        print(line)

    print()
    print("Measure           Ingredient\n")
    # print("Measure: ", meal.get_meal_measures())
    if not (meal.get_meal_measures1() is None and meal.get_meal_ingredients1() is None):
        print(meal.get_meal_measures1() + "               " + meal.get_meal_ingredients1())

    if not (meal.get_meal_measures2() is None and meal.get_meal_ingredients2() is None):
        print(meal.get_meal_measures2() + "               " + meal.get_meal_ingredients2())

    if not (meal.get_meal_measures3() is None and meal.get_meal_ingredients3() is None):
        print(meal.get_meal_measures3() + "               " + meal.get_meal_ingredients3())

    if not (meal.get_meal_measures4() is None and meal.get_meal_ingredients4() is None):
        print(meal.get_meal_measures4() + "               " + meal.get_meal_ingredients4())

    if not (meal.get_meal_measures5() is None and meal.get_meal_ingredients5() is None):
        print(meal.get_meal_measures5() + "               " + meal.get_meal_ingredients5())

    if not (meal.get_meal_measures6() is None and meal.get_meal_ingredients6() is None):
        print(meal.get_meal_measures6() + "               " + meal.get_meal_ingredients6())

    if not (meal.get_meal_measures7() is None and meal.get_meal_ingredients7() is None):
        print(meal.get_meal_measures7() + "               " + meal.get_meal_ingredients7())

    if not (meal.get_meal_measures8() is None and meal.get_meal_ingredients8() is None):
        print(meal.get_meal_measures8() + "               " + meal.get_meal_ingredients8())

    if not (meal.get_meal_measures9() is None and meal.get_meal_ingredients9() is None):
        print(meal.get_meal_measures9() + "               " + meal.get_meal_ingredients9())

    if not (meal.get_meal_measures10() is None and meal.get_meal_ingredients10() is None):
        print(meal.get_meal_measures10() + "               " + meal.get_meal_ingredients10())

    if not (meal.get_meal_measures11() is None and meal.get_meal_ingredients11() is None):
        print(meal.get_meal_measures11() + "               " + meal.get_meal_ingredients11())

    if not (meal.get_meal_measures12() is None and meal.get_meal_ingredients12() is None):
        print(meal.get_meal_measures12() + "               " + meal.get_meal_ingredients12())

    if not (meal.get_meal_measures13() is None and meal.get_meal_ingredients13() is None):
        print(meal.get_meal_measures13() + "               " + meal.get_meal_ingredients13())

    if not (meal.get_meal_measures14() is None and meal.get_meal_ingredients14() is None):
        print(meal.get_meal_measures14() + "               " + meal.get_meal_ingredients14())

    if not (meal.get_meal_measures15() is None and meal.get_meal_ingredients15() is None):
        print(meal.get_meal_measures15() + "               " + meal.get_meal_ingredients15())

    if not (meal.get_meal_measures16() is None and meal.get_meal_ingredients16() is None):
        print(meal.get_meal_measures16() + "               " + meal.get_meal_ingredients16())

    if not (meal.get_meal_measures17() is None and meal.get_meal_ingredients17() is None):
        print(meal.get_meal_measures17() + "               " + meal.get_meal_ingredients17())

    if not (meal.get_meal_measures18() is None and meal.get_meal_ingredients18() is None):
        print(meal.get_meal_measures18() + "               " + meal.get_meal_ingredients18())

    if not (meal.get_meal_measures19() is None and meal.get_meal_ingredients19() is None):
        print(meal.get_meal_measures19() + "               " + meal.get_meal_ingredients19())

    if not (meal.get_meal_measures20() is None and meal.get_meal_ingredients20() is None):
        print(meal.get_meal_measures20() + "               " + meal.get_meal_ingredients20())


    print()









def main():
    show_title()
    show_menu()

    while True:
        command = input("What would you like to do? (press 7 for menu) ")
        print()
        if command == "1":
            list_categories()
        elif command == "2":
            list_meals_by_category()
        elif command == "3":
            search_meals_by_name()
        elif command == "4":
            random_meal()
        elif command == "5":
            list_areas()
        elif command == "6":
            list_meals_by_area()
        elif command == "7":
            show_menu()
        elif command == "0":
            print("Thank you for dining with us!")
            sys.exit()

        else:
            print("Invalid entry.")


if __name__ == "__main__":
    main()