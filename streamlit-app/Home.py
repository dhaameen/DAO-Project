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
    page_title = "DAO Home",
    page_icon = "🤑"
)

# @st.cache(allow_output_mutation=True)
# def load_contract():

#     # Load the contract ABI
#     with open(Path('./contracts/compiled/artregistry_abi.json')) as f:
#         contract_abi = json.load(f)

#     # Set the contract address (this is the address of the deployed contract)
#     contract_address = os.getenv("SMART_CONTRACT_ADDRESS")

#     # Get the contract
#     contract = w3.eth.contract(
#         address=contract_address,
#         abi=contract_abi
#     )

#     return contract




st.title("DAO Home")

st.markdown("## Crowdfunding Dao")
st.markdown("Dao description...")


st.write("Verify your DAO membership here!")
address_to_check = st.text_input("Please enter your wallet address")


st.markdown("***")

st.write("Get Tokens Here")
# '''if st.button("Get Tokens"):
#     tx_hash = contract.functions.registerArtwork(address, artwork_uri).transact({'from': address, 'gas': 1000000})
#     receipt = w3.eth.waitForTransactionReceipt(tx_hash)
#     st.write("Transaction receipt mined:")
#     st.write(dict(receipt))'''
