pragma solidity ^0.5.0;

import "./PupperCoin.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/Crowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/emission/MintedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/CappedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/validation/TimedCrowdsale.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/crowdsale/distribution/RefundablePostDeliveryCrowdsale.sol";

// @TODO: Inherit the crowdsale contracts
contract PupperCoinSale is Crowdsale, MintedCrowdsale, CappedCrowdsale, TimedCrowdsale, RefundableCrowdsale {
    constructor(
        uint rate, PupperCoin token, uint goal, uint openingTime, uint endingTime, 
        address payable wallet
    ) 
    
        Crowdsale(rate, wallet, token) 
        CappedCrowdsale(goal)
        TimedCrowdsale(openingTime, endingTime)
        RefundableCrowdsale(goal)
        public
    {
    
    }
}

contract PupperCoinSaleDeployer {
    address public token_sale_address;
    address public token_address;

    constructor(string memory name, string memory symbol, address payable wallet) public {
        PupperCoin token = new PupperCoin(name, symbol, 0);
        token_address = address(token);
        
        PupperCoinSale pupper_sale = new PupperCoinSale(1, token, 100, now, now + 24 weeks, wallet);
        token_sale_address = address(pupper_sale);

        // make the PupperCoinSale contract a minter, then have the PupperCoinSaleDeployer renounce its minter role
        token.addMinter(token_sale_address);
        token.renounceMinter();
    }
}
