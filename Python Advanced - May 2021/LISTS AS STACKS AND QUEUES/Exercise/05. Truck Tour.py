from collections import deque

n = int(input())

stations = deque([])

for x in range(n):
    stations.append(input())
# започвам на чисто с нулев резервоар
for big_circle_iteration in range(n):
    is_valid = True  # предполагаме, че от пърата бензиностанция ще станат нещата
    tank_petrol = 0
    # пробвам
    for small_circle_iteration in range(n):
        # надникваме какво има просто зад този елемент
        current_station = stations[big_circle_iteration]

        stations.append(current_station)
        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        tank_petrol += petrol

        if tank_petrol >= distance_to_next_station:
            tank_petrol += distance_to_next_station
            #ротейтвам
            stations.append(stations.popleft())
        # ние да не можем да стигнем, дистанцията да е по голяма от колкото петрол имаме
        # брейкваме, защпто няма смисъл да ходим до следваща бензиностанция, пробваме от следващата
        else:
            stations.append(current_station)
            is_valid = False
            break
    if is_valid:
        print(big_circle_iteration)
        break
