max_cap = []
curr_cap = []

for i in range(3):
    x = int(input("How much milk can the buckets hold: "))
    max_cap.append(x)

for i in range(3):
    x = int(input("How much milk are in the buckets: "))
    curr_cap.append(x)

for i in range(100):
    pout = i % 3
    pin = (pout + 1) % 3
    z = curr_cap[pout] + curr_cap[pin]
    if z > max_cap[pin]:
        curr_cap[pout] = z - max_cap[pin]
        curr_cap[pin] = max_cap[pin]
    else:
        curr_cap[pin] += curr_cap[pout]
        curr_cap[pout] = 0

print(curr_cap[0])
print(curr_cap[1])
print(curr_cap[2])
