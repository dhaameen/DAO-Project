pragma solidity ^0.5.5;

import "./DAOtoken.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";


// Have the KaseiCoinCrowdsale contract inherit the following OpenZeppelin:
// * Crowdsale
// * MintedCrowdsale
contract DAOtokenCrowdsale  is Crowdsale, MintedCrowdsale {
    // Provide parameters for all of the features of your crowdsale, such as the `rate`, `wallet` for fundraising, and `token`.
    constructor(
        uint256 rate,
        address payable wallet,
        DAOtoken token
    )  
        Crowdsale(rate, wallet, token) 
        public
    {
        // constructor can stay empty
    }
}


contract DAOtokenCrowdsaleDeployer {
    // Create an `address public` variable called `DAO_token_address`.
    address public DAO_token_address;
    // Create an `address public` variable called `DAO_crowdsale_address`.
    address public DAO_crowdsale_address;

    // Add the constructor.
    constructor(
        string memory name,
        string memory symbol,
        address payable wallet
    ) public {
        // Create a new instance of the DAOtoken contract.
        DAOtoken token = new DAOtoken(name, symbol, 0);
        
        // Assign the token contract’s address to the `DAO_token_address` variable.
        DAO_token_address = address(token);

        // Create a new instance of the `DAOtokenCrowdsale` contract and assign the `DAOtokenCrowdsale` contract’s address to the `DAO_crowdsale_address` variable.
         DAOtokenCrowdsale DAO_crowdsale =
            new DAOtokenCrowdsale(1, wallet, token);
        DAO_crowdsale_address = address(DAO_crowdsale);

        // Set the `DAOCrowdsale` contract as a minter
        token.addMinter(DAO_crowdsale_address);
        
        // Have the `DAOtokennCrowdsaleDeployer` renounce its minter role.
        token.renounceMinter();
    }
}