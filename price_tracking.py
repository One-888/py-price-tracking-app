# ke.py
import glob
import time

import keyboard as kb

import ocr_unit_test as ocr


def get_price_from_file():
    price = []
    file_list = glob.glob(r"*.png")
    for file in file_list:
        # print(f"{file}")
        pic_to_float = ocr.ocr_process_single_value(f"{file}")
        # print(f"{pic_to_float}")
        price.append(pic_to_float)
    return price


def display_result():
    p1 = get_price_from_file()
    p1 = set(p1)
    p1 = list(p1)
    p1.sort()
    return p1


def main():
    time.sleep(10)
    while True:
        kb.press_and_release("shift+print_screen")
        p2 = display_result()
        print(f"Min: {str(p2[0]).rjust(10, ' ')}")
        print(f"Max: {str(p2[-1]).rjust(10, ' ')}")
        pause_time_second = 300
        time.sleep(pause_time_second)
        print("Wait {pause_time_second} sec")


main()
