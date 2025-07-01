const Web3 = require("web3");
const web3 = new Web3.default("http://localhost:8545");

let lastBlock = 0;

async function watchBlocks() {
  setInterval(async () => {
    const current = Number(await web3.eth.getBlockNumber());
    if (current > lastBlock) {
      for (let i = lastBlock + 1; i <= current; i++) {
        const block = await web3.eth.getBlock(i, true);
        if (block.transactions.length > 0) {
          console.log(`\n🧱 Block ${block.number} | Tx Count: ${block.transactions.length}`);
          block.transactions.forEach((tx, idx) => {
            console.log(`  Tx ${idx + 1}: ${tx.from.slice(0, 10)}... → ${tx.to.slice(0, 10)}..., Value: ${web3.utils.fromWei(tx.value, "ether")} ETH`);
          });
        }
      }
      lastBlock = current;
    }
  }, 2000);
}

watchBlocks();
