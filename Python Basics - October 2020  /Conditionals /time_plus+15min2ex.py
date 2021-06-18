hours = int(input())
minutes = int(input())

minutes +=15

#sega trqbva da syobrazim usloviqta za minutite
if minutes > 59:
    hours = hours + 1 #1 #kogato min stanat poveche ot 60 dobqwqme 1 na chasovete
    #no kogato chasovete rastqt min zapochvat pak ot nachalo
    minutes = minutes - 60
if hours > 23:
    hours = hours - 24
if 0 <= minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")

