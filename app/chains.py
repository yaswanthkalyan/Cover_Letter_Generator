from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Chain:
    def __init__(self):
        # Fetch the API key
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")
        
        self.llm = ChatGroq(temperature=0, groq_api_key=api_key, model_name='llama-3.1-70b-versatile')

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]
    
    def write_coverletter(self, job, links):
        prompt_coverletter = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION
            {job_description}
    
    
    
            ### INSTRUCTION:
            You are [Name], a graduate student studying computational data science at Purdue University and will graduate in this December. You are currently looking for full-time opportunities. You came across a Job posting that suits your intrents and knowledge. You reaching out to you to see if you can get help finding a referral for this opportunity. You have over 2+ years of experience in Data Analytics and Data Science. You are well-versed in Data modeling and visualization.
            You are interested in ML and Data Related Roles.

            Your job is to write a cover letter to recruiter regarding the job mention and highlighting the skills which the job required as your expertise.
            Also add the most relavant ones from the following links to showcase your portfolio.
            Remember you are [Name], graduate student and aspiring data scientist.

            Do not provide preamble

            ### EMAIL <NO PREAMBLE>:

            """
        )
        chain_coverletter = prompt_coverletter | self.llm
        res = chain_coverletter.invoke({"job_description": str(job), "link_list": links})
        return res.content

