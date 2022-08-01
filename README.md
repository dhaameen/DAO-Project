# DAO-Project
![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/DAO.jpeg)

## Table of Contents
- [Summary](#summary)
  * [DAO Purpose](#dao-purpose)
  * [DAO Components](#dao-components)
- [Tech Stack](#tech-stack)
- [Installation Guide](#installation-guide)
  * [Remix IDE](#remix-ide)
  * [Streamlit](#streamlit)
- [Smart Contracts](#smart-contracts)
  * [CORE](#core)
  * [DAO Token](#dao-token)
  * [Governance Contract](#governance-contract)
  * [Timelock Contract](#timelock-contract)
- [dApps](#dapps)
  * [Tokens](#tokens)
  * [Vote on a Proposal](#vote-on-a-proposal)

## Summary

### DAO Purpose

![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/mind_image.jpeg)

We decided to create a DAO with a community focus on Mental Health and Wellbeing.

Our DAO funds contribute to:
- funding mental health research
- raising awareness
- funding projects
- events

Members can vote on funding proposals.

Members of our DAO can be rewarded for:
- "influencer" style posts
- hosting events
- starting a successful crowdfunding campaign
- bringing in new members

For more details of our DAO's purpose see our [marketing strategy](https://github.com/dhaameen/DAO-Project/marketing.md).

### DAO Components

Our DAO includes smart contracts for the following:
* [CORE](https://github.com/dhaameen/DAO-Project/blob/main/contracts/CORE.sol): this is the BASE contract that will be governed by the Governance_token, this contract will be owned by the DAO
* [DAO token](https://github.com/dhaameen/DAO-Project/blob/main/contracts/DAOtoken.sol): this is the voting token contract for the DAO proposals
* [governance contract](https://github.com/dhaameen/DAO-Project/blob/main/contracts/GovernanceContract.sol): this sets up the governance rules associated with voting including the voting period and the required quorum
* [timelock contract](https://github.com/dhaameen/DAO-Project/blob/main/contracts/Timelock.sol): this contract will execute proposals and holds any funds, ownership, and access control roles

## Tech Stack
- Solidity
- Remix IDE
- Streamlit
- MetaMask
- Ganache
- VS Code

## Installation Guide

### Remix IDE
In your web browser, navigate to [Remix IDE](https://remix.ethereum.org/).

Create a new document, and code your contract.

Upon completion, in the left menu navigate to the "Solidity Compiler" and compile your contract.

Then in the left menu navigate to "Deploy & Run Transactions" and deploy your contract.

Scroll down to interact with your contract.

### Streamlit
Optional: Create a new Web 3 environment (recommended).

Install [Web3.py](https://web3py.readthedocs.io/en/stable/overview.html) and [Streamlit](https://docs.streamlit.io/en/stable/installation.html) as follows:
  ```shell
  pip install streamlit
  ```
  
  ```shell
pip install web3==5.17
```

Clone the 'DAO-Project' repository.

In your terminal, navigate to the folder containing 'app.py' and enter the command. 

  ```shell
streamlit run app.py
```

Streamlit will launch locally in your default browser.

From there you can interact with the app.

## Smart Contracts

### CORE
[CORE](https://github.com/dhaameen/DAO-Project/blob/main/contracts/CORE.sol) is the BASE contract that will be governed by the Governance_token. This contract will be owned by the DAO.

![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/core.png)

### DAO Token
[DAO token](https://github.com/dhaameen/DAO-Project/blob/main/contracts/DAOtoken.sol) is the voting token contract for the DAO proposals.

![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/dao_token.png)

### Governance Contract
[Governance Contract](https://github.com/dhaameen/DAO-Project/blob/main/contracts/GovernanceContract.sol) sets up the governance rules associated with voting including the voting period and the required quorum.

![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/governance1.png)
![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/governance2.png)
![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/governance3.png)

### Timelock Contract
The [timelock contract](https://github.com/dhaameen/DAO-Project/blob/main/contracts/Timelock.sol) will execute proposals. It holds any funds, ownership, and access control roles.

![alt=“”](https://github.com/dhaameen/DAO-Project/blob/main/images/timelock.png)

## dApps
### Tokens

### Vote on a Proposal
