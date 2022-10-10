# ke.py
import glob
import time

import keyboard as kb

import ocr_unit_test as ocr

price = []


def get_file_list():
    file_list = glob.glob(r"*.png")
    for file in file_list:
        # print(f"{file}")
        pic_to_float = ocr.ocr_process_single_value(f"{file}")
        # print(f"{pic_to_float}")
        price.append(pic_to_float)


# while True:
# kb.press_and_release("shift+print_screen")
# time.sleep(600)


get_file_list()
price = set(price)
price = list(price)
price.sort()

print(f"Min: {str(price[0]).rjust(5, ' ')}")
print(f"Max: {str(price[-1]).rjust(5, ' ')}")
# print(price.sort)
# print(price.sort())
