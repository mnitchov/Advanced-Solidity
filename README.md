# Advanced-Solidity

Attached are two smart contracts, one for creating an ERC20 Token and its Crowdsale.
Once the two contracts are compiled on Remix we must deploy them and test on Metamask.

We'll start with the PupperCoin contract. Enter the name of the token, its symbol, and the intial supply.

![1](https://user-images.githubusercontent.com/77086043/126416702-70ce0423-d78b-47e8-9ef7-ebf49e1da429.PNG)
 
Press transact and confirm the contract on Metamask.

![2](https://user-images.githubusercontent.com/77086043/126416863-53b87594-882f-425b-9ced-d706a3831f38.PNG)

Confirm that the transaction was approved on Etherscan.

![3](https://user-images.githubusercontent.com/77086043/126416925-dc48f3a2-af59-4d0c-89fb-023c4f1344b6.PNG)

Next, deploy the PupperCoinSaleDeployer. Enter a name, the symbol, and the funding wallet.

![8](https://user-images.githubusercontent.com/77086043/126418176-44bd3f29-1431-4ae9-ae1e-9da6eb6e3b36.PNG)

Confirm the contract and verify it was succesful on Etherscan.

![4](https://user-images.githubusercontent.com/77086043/126418345-54a49ac6-9424-4814-83ab-55d527d92679.PNG)

Add the token on Metamask. Do so by going to 'Assets' and 'Add Token'. Paste the contract address from the first Etherscan confirmation from PupperCoin.

![6](https://user-images.githubusercontent.com/77086043/126418456-32ada840-8ccd-408a-9202-964e6a178b1f.PNG)

End off by sending test Ether to the contract.

![7](https://user-images.githubusercontent.com/77086043/126418522-0bd3dd10-9eaf-4c15-b209-7c552e750654.PNG)
