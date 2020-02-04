
def main():

	def check_if_number(n):
		try:
			float(n)
		except ValueError:
			return False
		return True

	first_number = input("Enter the first number: ")
	a = check_if_number(first_number)
	second_number = input("Enter the second number: ")
	b = check_if_number(second_number)


	if a and b:
		first_number = float(first_number)
		second_number = float(second_number)
		operation = input("Choose the operation (+, -, /, *): ")

		if operation == '+':
			answer = first_number + second_number
		elif operation == '-':
			answer = first_number - second_number
		elif operation == '/':
			answer = first_number / second_number
		elif operation == '*':
			answer = first_number * second_number
		else:
			print('the operation is not valid')

		print('the answer is '+ str(answer))
	else:
		print("The numbers were invalid")

	pass




if __name__ == '__main__':
	main()
