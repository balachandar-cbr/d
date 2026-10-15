# Ex 6: Hamming Code - Error Detection and Correction
def calculate_parity_bits(data):
    m = len(data)
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    n = m + r
    hamming = ['0'] * (n + 1)

    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:      # not a power of 2 -> data position
            hamming[i] = data[j]
            j += 1

    for p in range(r):
        position = 2 ** p
        parity = 0
        for i in range(1, n + 1):
            if i & position:
                parity ^= int(hamming[i])
        hamming[position] = str(parity)
    return ''.join(hamming[1:])

def detect_error(received):
    n = len(received)
    received = ['0'] + list(received)
    error_position = 0
    position = 1
    while position <= n:
        parity = 0
        for i in range(1, n + 1):
            if i & position:
                parity ^= int(received[i])
        if parity != 0:
            error_position += position
        position *= 2
    return error_position, received

data = input("Enter data bits: ")
hamming_code = calculate_parity_bits(data)
print("\nGenerated Hamming Code:", hamming_code)

received = input("\nEnter received Hamming Code: ")
error_position, received_data = detect_error(received)

if error_position == 0:
    print("No error detected.")
    print("Received data is correct.")
else:
    print("Error detected at position:", error_position)
    if error_position <= len(received):
        received_data[error_position] = '1' if received_data[error_position] == '0' else '0'
    corrected_code = ''.join(received_data[1:])
    print("Corrected Hamming Code:", corrected_code)
