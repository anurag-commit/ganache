const Web3 = require("web3");
const fs = require("fs");
const web3 = new Web3.default("http://localhost:8545");

(async () => {
  const accounts = await web3.eth.getAccounts();
  const balances = [];

  for (let i = 0; i < accounts.length; i++) {
    const balance = await web3.eth.getBalance(accounts[i]);
    balances.push({
      account: accounts[i],
      balance_eth: web3.utils.fromWei(balance, "ether")
    });
  }

  fs.writeFileSync("balances_after_attack.json", JSON.stringify(balances, null, 2));
  console.log("✅ Account balances saved to balances_after_attack.json");
})();
