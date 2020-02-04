
def main():


	first_number = input("Enter the first number: ")
	a = first_number.isnumeric()
	second_number = input("Enter the second number: ")
	b = second_number.isnumeric()

	if a and b:
		first_number = float(first_number)
		second_number = float(second_number)
		operation = input("Choose the operation (+, -, /, *): ")

		if operation == '+':
			answer = first_number + second_number
			print('the answer is '+ str(answer))
		elif operation == '-':
			answer = first_number - second_number
			print('the answer is '+ str(answer))
		elif operation == '/':
			answer = first_number / second_number
			print('the answer is '+ str(answer))
		elif operation == '*':
			answer = first_number * second_number
			print('the answer is '+ str(answer))
		else:
			print('the operation is not valid')

	else:
		print("the numbers were invalid")

	pass




if __name__ == '__main__':
	main()
