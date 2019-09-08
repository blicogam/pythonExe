import string

def totalEarnings(perHr, regHours, overHours):
	overtime = overHours * 1.5 * perHr
	weekpay = perHr * regHours + overtime
	print(weekpay)

def main():
	userInput = input("Enter perHr, numRegHrs, and overtimeHours, all sep by single spaces: ")
	try:
		data = userInput
		datalist = data.split()
		datalist = list(map(float, datalist))
		totalEarnings(datalist[0], datalist[1], datalist[2])

	except NameError:
		print("Unable to read data")

if __name__ == '__main__':
	main()