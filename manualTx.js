const Web3 = require("web3");
const readline = require("readline");

const web3 = new Web3.default("http://localhost:8545");

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

(async () => {
  const accounts = await web3.eth.getAccounts();
  console.log("Accounts:");
  accounts.forEach((acc, idx) => console.log(`[${idx}] ${acc}`));

  function askTransaction() {
    rl.question("Enter sender index: ", async (fromIdx) => {
      rl.question("Enter receiver index: ", async (toIdx) => {
        rl.question("Enter amount in ETH: ", async (amountEth) => {
          try {
            const from = accounts[parseInt(fromIdx)];
            const to = accounts[parseInt(toIdx)];
            const value = web3.utils.toWei(amountEth, "ether");

            const txHash = await web3.eth.sendTransaction({ from, to, value });
            console.log("Transaction sent! Hash:", txHash.transactionHash);
          } catch (err) {
            console.error("Transaction failed:", err.message);
          }

          rl.question("Send another transaction? (y/n): ", (answer) => {
            if (answer.toLowerCase() === "y") {
              askTransaction();
            } else {
              rl.close();
            }
          });
        });
      });
    });
  }

  askTransaction();
})();
