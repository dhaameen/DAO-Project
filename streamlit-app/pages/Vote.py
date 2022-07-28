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
    page_title = "Vote",
    page_icon = "🗣️"
)

st.title("Vote (DAO members only)")

st.markdown("## Proposals to Vote on")
st.markdown("Vote...")