#Imports
from fpdf import FPDF


def main():
    name = input("Name: ").strip().title()

    pdf = FPDF(orientation="P", format="A4")
    pdf.add_page()
    pdf.image("shirtificate.png", x=16, y=62, w=180, h=200)
    pdf.set_font("helvetica", "U", 50)
    pdf.cell(0, 16, "CS50 Shirtificate", align="C")

    pdf.set_font("helvetica", "B", size=35)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(-185, 240, txt=f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
