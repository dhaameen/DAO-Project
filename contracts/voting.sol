pragma solidity ^0.8.0;

contract Ballot{
    // Variables to be used in voting process
    struct proposal{
        // Proposal object
        string proposerName;
        string title;
        string description;
        uint voteCount;
    }
    struct voter{
        // Voter Object
        string voterName;
        address voterAddress;
        bool voted;            
    }
    struct vote{
        // Instance of Vote
        voter voterId;
        bool choice;
    }
    
    proposal[] public Proposals; // Array of proposals to be displayed on web app
    address[] private voterRegistry; // list of addresses allowed to vote on proposals submitted to DAO

    //voterRegistry.push();
    //voterRegistry.push();
    //voterRegistry.push();
    //voterRegistry.push();

    uint private totalCount = 0; // Display this count on the web app
    uint public result = 0; // Display this count on the web app

    address public ballotAddress;

    // Mappings
    mapping(uint => vote) private votes;
    mapping(address => voter) public voterRegister;


    
    
}