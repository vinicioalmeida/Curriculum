# Prof. Vinicio Almeida
# almeida.vinicio@gmail.com
# https://sites.google.com/view/vinicioalmeida/

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

# List to store the content of the curriculum
curriculum = []

# Personal information
name = "Vinicio de Souza e Almeida"
phone = "+55 84 994305243"
email = "almeida.vinicio@gmail.com"
personal_sites = [
    "LinkedIn: linkedin.com/in/vinicioalmeida",
    "GitHub: github.com/vinicioalmeida",
    "Website: sites.google.com/view/vinicioalmeida",
    "Twitter: @ovinicioalmeida",
    "Instagram: @almeidavinicio"
]

# Add Personal information
curriculum.append(Paragraph(name, getSampleStyleSheet()['Title']))
curriculum.append(Paragraph(phone, getSampleStyleSheet()['Normal']))
curriculum.append(Paragraph(email, getSampleStyleSheet()['Normal']))
curriculum.append(Spacer(1, 0.1 * inch))  # Add space

# Add personal sites
curriculum.append(Paragraph("Personal Sites:", getSampleStyleSheet()['Heading2']))
for site in personal_sites:
    curriculum.append(Paragraph(site, getSampleStyleSheet()['Normal']))
curriculum.append(Spacer(1, 0.1 * inch))  # Add space

# Add areas of interest
areas_of_interest = "Areas of Interest: Quant Research, Algo Trading, Finance, Python"
curriculum.append(Paragraph(areas_of_interest, getSampleStyleSheet()['Heading2']))
curriculum.append(Spacer(1, 0.1 * inch))  # Add space

# Define education entries
education_entries = [
    {
        "degree": "Doctor of Science in Business-Finance",
        "university": "Federal University of Rio de Janeiro - UFRJ/COPPEAD",
        "dates": "2006 - 2010",
        "description": "Thesis on initial public offerings underpricing in Brazil."
    },
    {
        "degree": "Bachelor of Science in Business",
        "university": "Ceará State University - UECE",
        "dates": "2000 - 2005",
        "description": "Undergraduate paper on credit scoring."
    }
]

# Add education entries to the curriculum
curriculum.append(Paragraph("Education:", getSampleStyleSheet()['Heading2']))
for entry in education_entries:
    curriculum.append(Paragraph(entry["degree"], getSampleStyleSheet()['Heading4']))
    curriculum.append(Paragraph(entry["university"], getSampleStyleSheet()['Normal']))
    curriculum.append(Paragraph(entry["dates"], getSampleStyleSheet()['Normal']))
    curriculum.append(Paragraph(entry["description"], getSampleStyleSheet()['Normal']))
    curriculum.append(Spacer(1, 0.1 * inch))  # Add space

# Define employment entries
employment_entries = [
    {
        "position": "Professor of Finance",
        "company": "Federal University of Rio Grande do Norte - UFRN",
        "dates": "2010 - Present",
        "description": "Teaching on undergraduate and graduate courses (Time Series Analysis, Derivatives), Research on quantitative portfolio management."
    },
    {
        "position": "Portfolio Management",
        "company": "BB Asset",
        "dates": "2008 - 2010",
        "description": "Equity funds management with quantitative idea generation."
    },
    {
        "position": "Analyst",
        "company": "BB Investments",
        "dates": "2007 - 2008",
        "description": "Participated on equity offerings structuring."
    }
]

# Add employment entries to the curriculum
curriculum.append(Paragraph("Employment:", getSampleStyleSheet()['Heading2']))
for entry in employment_entries:
    curriculum.append(Paragraph(entry["position"], getSampleStyleSheet()['Heading4']))
    curriculum.append(Paragraph(entry["company"], getSampleStyleSheet()['Normal']))
    curriculum.append(Paragraph(entry["dates"], getSampleStyleSheet()['Normal']))
    curriculum.append(Paragraph(entry["description"], getSampleStyleSheet()['Normal']))
    curriculum.append(Spacer(1, 0.1 * inch))  # Add space

# Create a PDF document
doc = SimpleDocTemplate("CurriculumVinicioAlmeida.pdf", pagesize=letter)

# Build the curriculum content
doc.build(curriculum)