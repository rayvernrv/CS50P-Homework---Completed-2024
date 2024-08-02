from fpdf import FPDF

class PDF(FPDF):
    def title(self):
        self.set_font("helvetica", "B", size=50)
        self.cell(0, 25, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    def shirt(self):
        self.image("shirtificate.png", x=5,y=50, w=200)

    def logo(self, word: str):
        self.word = word
        self.set_font("helvetica", size=25)
        self.set_text_color(255,255,255)
        self.cell(0, 150, word, align="C")


pdf = PDF()
pdf.add_page()
pdf.title()
pdf.shirt()
pdf.logo(input("Name: ") + " took CS50")
pdf.output("shirtificate.pdf")




