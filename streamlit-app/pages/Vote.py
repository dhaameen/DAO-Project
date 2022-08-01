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

st.markdown("## Proposals to Vote on: ")
st.markdown("#### Project Title: Canned Water")
st.markdown("#### Proposed by: Johnny Appleseed")
st.markdown("#### Description: ")
st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
st.markdown("Vote...")


address_whitelist = ["0x22C4238777d22C985D063831F6b3072f047405b7", "0xaCEF1a4f8a0680f152806898A43C64D4dfFe5cd4", "0xe49312d5cA8C1dEe8334567F60741c0D6D919166"]

address_check = st.text_input("Verify Wallet Address to Vote")
if address_check in address_whitelist:
    with st.form("Proposal Form", clear_on_submit = True):
        choice = st.selectbox("cast your vote", ["yes", "no"])
        submit = st.form_submit_button("Submit!")