months_31_days = (1, 3, 5, 7, 8, 10, 12)
months_30_days = (4, 6, 9, 11)

months = {
    "1": "Jan",
    "2": "Feb",
    "3": "Mar",
    "4": "Apr",
    "5": "May",
    "6": "Jun",
    "7": "Jul",
    "8": "Aug",
    "9": "Sep",
    "10": "Oct",
    "11": "Nov",
    "12": "Dic",
}


def display_months(month_name, amount_of_days):
    print(f"{month_name} has {amount_of_days} days")


month = input("Enter month number: ")

while not 1 <= int(month) <= 12:
    month = input("Enter a valid month number (1,12): ")

if int(month) in months_31_days:
    display_months(months[month], 31)
elif int(month) in months_30_days:
    display_months(months[month], 30)
else:
    display_months(months[month], 28)
