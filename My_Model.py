#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
from pdfminer.high_level import extract_text
import spacy
from spacy.matcher import Matcher


# In[2]:


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)


# In[3]:


if __name__ == '__main__':
   print(extract_text_from_pdf(r"C:\Users\anand\OneDrive\Desktop\project\data\resume v6.pdf"))


# In[4]:


import pdfminer
import re

def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name


# In[5]:


def extract_text_from_pdf(pdf_path):
   return extract_text(pdf_path)

# My_Website.py

def extract_contact_number_from_resume(text):
    pattern = r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b"
    match = re.search(pattern, text)
    if match:
        phone_number = match.group()
        return phone_number  # Return the extracted phone number

    return None  # Return None if no phone number is found




# In[6]:


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_email_from_resume(text):
    email = None

    # Use regex pattern to find a potential email address
    pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
    match = re.search(pattern, text)
    if match:
        email = match.group()

    return email


# In[7]:


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_skills_from_resume(text, skills_list):
    skills = []

    # Search for skills in the resume text
    for skill in skills_list:
        pattern = r"\b{}\b".format(re.escape(skill))
        match = re.search(pattern, text, re.IGNORECASE)
        if match:
            skills.append(skill)

    return skills


# In[8]:


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:(?:Bachelor|B\.S\.|B\.A\.|Master|M\.S\.|M\.A\.|Ph\.D\.)\s(?:[A-Za-z]+\s)*[A-Za-z]+)"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education


# In[9]:


def extract_education_from_resume(text):
    education = []

    # Use regex pattern to find education information
    pattern = r"(?i)(?:Bsc|\bB\.\w+|\bM\.\w+|\bPh\.D\.\w+|\bBachelor(?:'s)?|\bMaster(?:'s)?|\bPh\.D)\s(?:\w+\s)*\w+"
    matches = re.findall(pattern, text)
    for match in matches:
        education.append(match.strip())

    return education


# In[10]:


def extract_text_from_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_name_from_resume(text):
    name = None

    # Use regex pattern to find a potential name
    pattern = r"(\b[A-Z][a-z]+\b)\s(\b[A-Z][a-z]+\b)"
    match = re.search(pattern, text)
    if match:
        name = match.group()

    return name


# In[20]:


if __name__ == '__main__':
    resume_paths = [r"C:\Users\anand\OneDrive\Desktop\project\data\resume v6.pdf"]

    for resume_path in resume_paths:
        text = extract_text_from_pdf(resume_path)

        print("Resume:", resume_path)

        name = extract_name_from_resume(text)
        if name:
            print("Name:", name)
        else:
            print("Name not found")

        phone_number = extract_contact_number_from_resume(text)
        if phone_number:
            print("phone Number:", phone_number)
        else:
            print("phone Number not found")

        email = extract_email_from_resume(text)
        if email:
            print("Email:", email)
        else:
            print("Email not found")

        skills_list = ['Python', 'Data Analysis', 'Machine Learning', 'Communication', 'Project Management', 'Deep Learning', 'SQL', 'Tableau']
        extracted_skills = extract_skills_from_resume(text, skills_list)
        if extracted_skills:
            print("Skills:", extracted_skills)
        else:
            print("No skills found")

        extracted_education = extract_education_from_resume(text)
        if extracted_education:
            print("Education:",extract_education_from_resume)
        else:
            print("No education information found")

        print()

