needed_money = float(input())  # пари нужни за екскурзията
money_in_hand = float(input())  # налични пари
spending_days = 0  # колко дни подред тя е харчила
#  сега трябва да се направи цикъл за вида действие и симата която ще спести или похарчи
# тук нямам команда, която да ме спира затова аз мога да си направя безкраен цикъл който трябва да бъде спрян
total_days = 0
while True:
    action = input()  # вид действие - или е spend или safe
    current_sum = float(input())  # Сумата, която ще спести/похарчи,  променя се всеки ден
    # сега остава да правя проверката дали е спенд или сейф
    total_days += 1
    if action == "spend":  # това значи от наличните пари аз трябва да махна
        money_in_hand -= current_sum
        if money_in_hand < 0:  # Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и
            # ще ѝ останат 0 лева
            money_in_hand = 0
        spending_days += 1  # увеличавам дните с единица защото те са важни трябва знам колко дни тя харчи
        # и това нещо не трябва да е в иф проверката трябва да е по навънка защото иначе ще се изпълнява
        if spending_days == 5:
            break
    elif action == "safe":
        money_in_hand += current_sum
        if money_in_hand >= needed_money:
            break
        spending_days = 0  # този по горе брояч spending days трябва да го направя отново равен на 0, защото тя харчи
        # харчи няколко дни брояча расте в момента в който тя спястява някой ден брояча трябва да стане 0 и ако харчи
        # пак трябва да започне да отброява 5 дни
if money_in_hand >= needed_money:
    print(f"You saved the money for {total_days} days.")
else:
    print("You can't save the money.")
    print(total_days)
