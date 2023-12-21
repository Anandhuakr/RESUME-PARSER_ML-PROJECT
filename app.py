# Modify the function to handle both file path and file object
def extract_text_from_pdf(pdf):
    if hasattr(pdf, 'read'):  # If it's a file object
        return extract_text(pdf)
    elif isinstance(pdf, str):  # If it's a file path
        with open(pdf, 'rb') as file:
            return extract_text(file)
    else:
        return None  # Handle other cases or errors

# Flask application
from flask import Flask, render_template, request
from My_Model import extract_contact_number_from_resume

from My_Model import (
    extract_name_from_resume,
    extract_contact_number_from_resume,
    extract_email_from_resume,
    extract_skills_from_resume,
    extract_education_from_resume,
    extract_text_from_pdf,
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ... (other code)

@app.route('/result', methods=['POST'])
def result():
    if request.method == 'POST':
        resume_file = request.files['resume']
        # Process the uploaded file
        if resume_file.filename != '':
            # Instead of passing the file stream directly, save the uploaded file and then extract text from it
            file_path = "uploads/file.pdf"  # Define the path where you want to save the file
            resume_file.save(file_path)  # Save the uploaded file
            resume_text = extract_text_from_pdf(file_path)  # Extract text from the saved file
            # ... rest of your code

        name = extract_name_from_resume(resume_text)
        contact_number = extract_contact_number_from_resume(resume_text)
        email = extract_email_from_resume(resume_text)
        skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication']  # Add your skills
        skills = extract_skills_from_resume(resume_text, skills_list)
        education = extract_education_from_resume(resume_text)
        
        return render_template('result.html', 
                               name=name, 
                               contact_number=contact_number, 
                               email=email, 
                               skills=skills, 
                               education=education)
    else:
        return "No resume uploaded."
    
if __name__ == '__main__':
    app.run(debug=True)