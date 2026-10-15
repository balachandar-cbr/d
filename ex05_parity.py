# Ex 5: Parity Checking
data = input("Enter binary data: ")
print("\n1. Even Parity")
print("2. Odd Parity")
choice = int(input("Enter your choice: "))

ones = data.count('1')
if choice == 1:
    parity_bit = '0' if ones % 2 == 0 else '1'
    parity_type = "Even"
elif choice == 2:
    parity_bit = '1' if ones % 2 == 0 else '0'
    parity_type = "Odd"
else:
    print("Invalid choice")
    exit()

transmitted_data = data + parity_bit
print("\nParity Type:", parity_type)
print("Parity Bit:", parity_bit)
print("Transmitted Data:", transmitted_data)

received_data = input("\nEnter received data: ")
received_ones = received_data.count('1')

if choice == 1:
    print("No error detected." if received_ones % 2 == 0 else "Error detected.")
else:
    print("No error detected." if received_ones % 2 == 1 else "Error detected.")
