
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(f"For loop iteration: {i}")
else:
    print("For loop finished normally (not executed in this case due to break)")

print("-" * 20)

count = 0
while count < 5:
    if count == 1:
        count += 1
        pass
    if count == 3:
        print("Breaking from while loop")
        break
    print(f"While loop iteration: {count}")
    count += 1
else:
    print("While loop finished normally (not executed in this case due to break)")

print("Program complete.")