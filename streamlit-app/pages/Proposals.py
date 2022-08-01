"""
Main page where information about dao is
Voting tokens can be bought
introductory page (welcome to the dao...)
porject proposals
display treasury balance
"""

import streamlit as st
import os
import json
from web3 import Web3
from pathlib import Path
#from dotenv import load_dotenv


#load_dotenv()

st.set_page_config(
    page_title = "Proposals",
    page_icon = "📝"
)

st.title("Proposals")

st.markdown("## Proposal Form")
st.markdown("Submit Your Project Proposals Here:")

with st.form("Proposal Form", clear_on_submit = True):
    name = st.text_input("Enter your Name")
    title = st.text_input("Project Title")
    description = st.text_input("Project Description")

    submit = st.form_submit_button("Submit!")

st.write((name, title, description))