import math
record_in_seconds = float(input())
distance_in_metres = float(input())
time_in_sec_for_meter = float(input())

sum_time_in_seconds = distance_in_metres * time_in_sec_for_meter
slowing_distance_metres = (math.floor(distance_in_metres / 15)) * 12.5

total_time = slowing_distance_metres + sum_time_in_seconds

waste = abs(record_in_seconds - total_time)

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
elif total_time >= record_in_seconds:
    print(f"No, he failed! He was {waste:.2f} seconds slower.")

