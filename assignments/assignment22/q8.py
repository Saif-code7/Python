# **8.Take input of total minutes and convert them into hours and remaining minutes.**

# **Input:** 135

# **Output :** 2 hours 15 minutes

time = int(input("enter total minutes : "))

hours = time//60
rm = time%60
print(f"the time is : {hours} hours {rm} minutes")