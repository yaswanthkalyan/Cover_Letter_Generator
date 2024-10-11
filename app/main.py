import streamlit as st
from langchain_community.document_loaders import WebBaseLoader

from chains import Chain
from portfolio import Portfolio
from utils import clean_text

def create_streamlit_app(llm,portfolio,clean_text):
    st.title("Cover Letter Generator")
    url_input = st.text_input("Enter valid URL:", value="https://www.amazon.jobs/en/jobs/2796391/applied-scientist-artificial-general-intelligence?cmpid=SPLICX0248M&utm_source=linkedin.com&utm_campaign=cxro&utm_medium=social_media&utm_content=job_posting&ss=paid")
    submit_button = st.button("Submit")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            portfolio.load_portfolio()
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills=job.get('skills', [])
                links=portfolio.query_links(skills)
                cover_letter=llm.write_coverletter(job, links)
                st.code(cover_letter, language='markdown')
        except Exception as e:
            st.error(f'Error occured: {e}')

if __name__=='__main__':
    chain = Chain()
    portfolio = Portfolio()
    st.set_page_config(layout="wide",page_title='Cover Letter Generator',page_icon='📝')
    create_streamlit_app(chain, portfolio, clean_text)
