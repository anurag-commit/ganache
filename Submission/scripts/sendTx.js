const Web3 = require("web3");
const web3 = new Web3.default("http://localhost:8545");

(async () => {
  const accounts = await web3.eth.getAccounts();
  for (let i = 0; i < 10; i++) {
    web3.eth.sendTransaction({
      from: accounts[0],
      to: accounts[1],
      value: web3.utils.toWei("0.01", "ether"),
    }).then((txHash) => {
      console.log(`Tx ${i + 1} sent: ${txHash}`);
    }).catch((err) => {
      console.error(`Tx ${i + 1} failed:`, err.message);
    });
  }
})();
