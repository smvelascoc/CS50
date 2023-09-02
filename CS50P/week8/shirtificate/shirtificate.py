from fpdf import FPDF
from PIL import Image
import sys

def main():
    name = input("Name: ")
    shirt = open_image("shirtificate.png")

    #File creation
    certificate = FPDF(orientation = "P", format = (210,297))
    certificate.set_author("SVE")
    certificate.add_page()

    #Print title
    certificate.set_font("Helvetica", "B", 40)
    certificate.cell(certificate.epw/2)
    certificate.cell(txt = "CS50 Shirtificate", align = "X", new_x= "LMARGIN", new_y="NEXT")

    #Print Image
    certificate.set_y(certificate.get_y() + 20)
    certificate.image(shirt, w = certificate.epw)

    #Print name
    certificate.set_font("Helvetica", "", 24)
    certificate.set_text_color(255)
    certificate.set_xy(105, 100)
    certificate.cell(txt = f"{name} took CS50", align = "X")

    certificate.output("shirtificate.pdf")

def open_image(name):
    try:
        image_return = Image.open(name)
        return image_return
    except FileNotFoundError:
        sys.exit(f"Could not read {name}")

if __name__ == "__main__":
    main()