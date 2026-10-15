# Ex 8: Frame Creation Using Character Stuffing
def character_stuffing(data):
    FLAG = 'F'
    ESC = 'E'
    stuffed_data = FLAG
    for char in data:
        if char == FLAG or char == ESC:
            stuffed_data += ESC
        stuffed_data += char
    stuffed_data += FLAG
    return stuffed_data

data = input("Enter the data: ")
result = character_stuffing(data)
print("\nOriginal Data :", data)
print("Stuffed Frame :", result)
