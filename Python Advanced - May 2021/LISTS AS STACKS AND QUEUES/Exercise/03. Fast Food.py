from collections import deque

total_food_quantity = int(input())
order_deque = deque()

for order in input().split():
    order_deque.append(int(order))
max_order = max(order_deque)

for i in range(len(order_deque)):
    order = order_deque.popleft()
    if order <= total_food_quantity:
        total_food_quantity -= order
    else:
        order_deque.append(order)
        break

print(max_order)
if len(order_deque) == 0:
    print("Orders complete")
else:
    print(f"Orders left:", ''.join([str(order)for order in order_deque]))
