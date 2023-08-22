def calculate_payment(minutes_parked, day_of_week):
    if minutes_parked < 5:
        return 0
    
    if day_of_week in ['Monday', 'Tuesday', 'Wednesday']:
        hourly_rate = 2.00
    elif day_of_week in ['Thursday', 'Friday']:
        hourly_rate = 2.50
    else:
        hourly_rate = 3.00
    
    full_hours = minutes_parked // 60
    fractional_hour = (minutes_parked % 60 > 5)
    
    if fractional_hour:
        full_hours += 1
    
    total_payment = full_hours * hourly_rate
    return total_payment

try:
    parked_time_minutes = float(input("Enter the parked time in minutes: "))
    day_of_week = input("Enter the day of the week: ")

    if parked_time_minutes < 0 or day_of_week not in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
        print("Error: Incorrect time or day input.")
    else:
        payment = calculate_payment(parked_time_minutes, day_of_week)
        if payment == 0:
            print("The customer does not need to pay for such a short parked time.")
        else:
            print(f"The customer should pay ${payment:.2f}")

except ValueError:
    print("Error: Invalid input. Enter a valid number for the parked time.")