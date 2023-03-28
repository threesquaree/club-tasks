import cv2
import pytesseract

img = cv2.imread('arithmetic.jpg')

def function_1():
    text = pytesseract.image_to_string(img)

    text = text.replace('x', '*').replace('%', '/')

    s = eval(text)

    print(s)
    return s

function_1()