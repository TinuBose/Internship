sec = int(input("Enter the number of seconds: "))

hr = sec // 3600  # Divide seconds by 3600 to get the number of hours
hr_sec = sec % 3600    # Calculate the remaining seconds after getting hours

min = hr_sec // 60     # Divide the remaining seconds by 60 to get the number of minutes
min_sec = hr_sec % 60       # Calculate the remaining seconds


print(hr,":",min,":",)
