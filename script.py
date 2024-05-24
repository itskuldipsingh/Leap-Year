from LeapYear import leap_year

while True:
    #date = input("Enter date in dd-mm-yyyy format (e.g., 16-05-2024) or type 'exit' to exit: ")
    year = input("Enter Year or type 'exit' to exit: ")
    if year.lower() == "exit":
    #if date.lower() == "exit":
        break
    try:
        #Day, Month, Year = map(int, date.split("-"))
        year = int(year)
        if leap_year(year):
            print(f"{year} : leap year")
        else:
            print(f"{year} : non-leap year")
    except ValueError:
        print("Invalid input! Please enter a valid date in dd-mm-yyyy format or type 'exit' to exit.")
        
