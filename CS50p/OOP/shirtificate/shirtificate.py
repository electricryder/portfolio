from fpdf import FPDF, Align


name = input("Name: ")
pdf = FPDF()
pdf.add_page()
pdf.ln(10)
pdf.set_font("helvetica", size=50)
pdf.cell(80)
pdf.cell(210, 10, "CS50 Shirtificate", center=True, align=Align.C)
pdf.ln(90)
pdf.image("shirtificate.png", x=Align.C, y=50, w=200, keep_aspect_ratio=True )
pdf.set_font("helvetica", size=20)
pdf.set_text_color(255,255,255)
pdf.cell(150, 10, f"{name} took CS50", center=True, align=Align.C)
pdf.output("shirtificate.pdf")
