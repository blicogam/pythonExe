import math
import fractions

def main():
	userInput = input("Enter radius: ")
	try:
		radius = float(userInput)
		diameter = radius * 2.0
		circum = diameter * math.pi
		sa = circum * 2.0 * radius
		vol = sa * radius * fractions.Fraction('1/3')
		print(radius)
		print(diameter)
		print(circum)
		print(sa)
		print(vol)

	except ValueError:
		print("Invalid radius:",userInput )

if __name__ == '__main__':
	main()