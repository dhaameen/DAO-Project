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
from dotenv import load_dotenv



st.set_page_config(
    page_title = "DAO Home",
    page_icon = "🤑"
)
w3 = Web3(Web3.HTTPProvider(os.getenv("WEB3_PROVIDER_URI")))

load_dotenv()

@st.cache(allow_output_mutation=True)
def load_contract():

    # Load the contract ABI
    with open(Path('./compiled/token_abi.json')) as f:
        contract_abi = json.load(f)

    # Set the contract address (this is the address of the deployed contract)
    contract_address = os.getenv("TOKEN_ADDRESS")

    # Get the contract
    contract = w3.eth.contract(
        address=contract_address,
        abi=contract_abi
    )

    return contract

token_contract = load_contract()


st.title("")

st.markdown("## Group5 Dao")
st.markdown("Our DAO aims to help issues within the mental health area. Creating a more social and positive community so people can express their experiences and share positive stories in a safe place. Group5DAO coordinates efforts and problem solving around crypto and blockchain applications and aims to help people through difficulties or hardships. To join the DAO you have to mint our governance token with the form below. This would allow y")



st.markdown("***")

st.write("Get Tokens Here")

with st.form("Get Tokens", clear_on_submit = True):
    address = st.text_input("Enter your wallet address")
    amount = st.text_input("Enter amount you would like to mint")

    submit = st.form_submit_button("Mint Tokens!")

    tx_hash = token_contract.functions.mint(address, amount).transact({'from': address, 'gas': 1000000})
    receipt = w3.eth.waitForTransactionReceipt(tx_hash)
    st.write("Transaction receipt mined:")
    st.write(dict(receipt))
