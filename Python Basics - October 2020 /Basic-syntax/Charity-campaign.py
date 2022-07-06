campaign_days = int (input())
confectioners_num = int (input())
cake_number = int (input())
waffles_number = int (input())
pancake_num = int (input())

cake_price = cake_number * 45
waffles_price= waffles_number * 5.80
pancake_price = pancake_num * 3.20

full_sum_per_day = (cake_price + waffles_price + pancake_price)*confectioners_num
whole_campaign_sum = full_sum_per_day * campaign_days
sum_after_costs = whole_campaign_sum - (1/8 *whole_campaign_sum)
print(sum_after_costs)



    