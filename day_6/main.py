def main():
    #LEVEL 1 ===============
    # initial_tuple = tuple()
    # initial_tuple = ()
    sisters = ('Sophia', 'Sam')
    brothers = ('Richard', 'Larry')
    siblings = sisters + brothers
    print(f"I have {len(siblings)} siblings: {", ".join(siblings)}")

    family_members = list(siblings)
    family_members.append("Carol")
    family_members.append('James')
    print(family_members)

    #LEVEL 2 ===============
    siblings = family_members[:4]
    parents = family_members[4:]
    print(siblings, parents)
    fruits = ('apple', 'banana', 'pear')
    vegetables = ('cucumber', 'onion', 'potato ')
    animal_products = ('milk', 'cheese', 'egg')
    food_stuff_tp = fruits + vegetables +animal_products
    food_stuff_li = list(food_stuff_tp)
    middle_item = food_stuff_li[len(food_stuff_li)//2:len(food_stuff_li)//2+1]
    print(middle_item)
    first_and_last_three_elements = food_stuff_li[:3] + food_stuff_li[-3:]
    print(first_and_last_three_elements)
    del food_stuff_tp

    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    print('Estonia' in nordic_countries)
    print('Iceland' in nordic_countries)

if __name__ == '__main__':
    main()