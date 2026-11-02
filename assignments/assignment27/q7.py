'''## Q7. Time of Day

Take the hour as input in 24-hour format.

Print:

- 5 to 11 → `"Morning"`
- 12 to 16 → `"Afternoon"`
- 17 to 20 → `"Evening"`
- 21 to 23 or 0 to 4 → `"Night"`

If the hour is outside `0-23`, print `"Invalid Hour"`.

**Example:**
Enter hour: 18

Output:
Evening
'''

time = int(input("enter hour: "))
if time < 5 or time >= 21 or time <= 23:
    print("Night")
elif time < 12:
    print("Morning")
elif time < 17:
    print("afternoon")
elif time < 21:
    print("evening")   
else:
    print("Invalid Hour")
    
