print()

distance = float(input("Enter the distance in miles: "))
speed = float(input("Enter the speed in miles per hour: "))
hours_stop = float(input("How many hours to stop? "))

travel_time = distance / speed
total_time = travel_time + hours_stop

print(f"\nThe time is {total_time} hours.")
