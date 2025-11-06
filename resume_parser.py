import re
import PyPDF2
import docx

# ------------------------------------------
# Function: Extract text from PDF or DOCX
# ------------------------------------------
def extract_text(file):
    if file.name.endswith(".pdf"):
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    elif file.name.endswith(".docx"):
        doc = docx.Document(file)
        return "\n".join([p.text for p in doc.paragraphs])
    else:
        return ""

# ------------------------------------------
# Function: Extract basic details using regex
# ------------------------------------------
def parse_resume(text):
    details = {
        "Name": None,
        "Email": None,
        "Phone": None,
        "Skills": [],
        "Education": [],
        "Experience": []
    }

    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    if email_match:
        details["Email"] = email_match.group(0)

    # Extract phone number
    phone_match = re.search(r'\+?\d[\d\s-]{8,}\d', text)
    if phone_match:
        details["Phone"] = phone_match.group(0)

    # Guess name (first line, optional)
    lines = text.strip().split('\n')
    if len(lines) > 0:
        details["Name"] = lines[0].strip()

    # Extract skills (based on keywords)
    skills_keywords = ["Python", "Machine Learning", "Data", "SQL", "Excel", "Java", "AWS", "Power BI", "Communication"]
    found_skills = [skill for skill in skills_keywords if skill.lower() in text.lower()]
    details["Skills"] = found_skills

    # Extract education section
    education_keywords = ["B.Tech", "B.E", "M.Tech", "MCA", "B.Sc", "M.Sc", "Bachelor", "Master", "PhD"]
    found_edu = [edu for edu in education_keywords if edu.lower() in text.lower()]
    details["Education"] = found_edu

    # Extract experience keywords
    exp_keywords = ["Intern", "Engineer", "Developer", "Analyst", "Manager"]
    found_exp = [exp for exp in exp_keywords if exp.lower() in text.lower()]
    details["Experience"] = found_exp

    return details
