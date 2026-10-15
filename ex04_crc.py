# Ex 4: CRC Error Detection
def crc_division(data, generator):
    data = list(data)
    generator = list(generator)
    for i in range(len(data) - len(generator) + 1):
        if data[i] == '1':
            for j in range(len(generator)):
                data[i + j] = str(int(data[i + j]) ^ int(generator[j]))
    return ''.join(data[-(len(generator) - 1):])

data = input("Enter data bits: ")
generator = input("Enter generator bits: ")

appended_data = data + '0' * (len(generator) - 1)
remainder = crc_division(appended_data, generator)
transmitted_data = data + remainder

print("\nCRC Remainder:", remainder)
print("Transmitted Data:", transmitted_data)

received_data = input("\nEnter received data: ")
check_remainder = crc_division(received_data, generator)
print("Checking Remainder:", check_remainder)

if '1' in check_remainder:
    print("Error detected in received data.")
else:
    print("No error detected. Data received correctly.")
