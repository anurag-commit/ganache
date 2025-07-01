const fs = require("fs");
const Web3 = require("web3");
const web3 = new Web3.Web3("http://localhost:8545");

let lastBlock = 0;
let blocks = [];

async function watchBlocks() {
  setInterval(async () => {
    const current = Number(await web3.eth.getBlockNumber());
    if (current > lastBlock) {
      for (let i = lastBlock + 1; i <= current; i++) {
        const block = await web3.eth.getBlock(i, true);
        
        blocks.push({
          number: Number(block.number),
          timestamp: Number(block.timestamp),
          txCount: block.transactions.length,
        });

        console.log(`\n🧱 Block ${block.number} | Tx Count: ${block.transactions.length}`);
        block.transactions.forEach((tx, idx) => {
          console.log(
            `  Tx ${idx + 1}: ${tx.from.slice(0, 10)}... → ${tx.to?.slice(0, 10)}..., Value: ${web3.utils.fromWei(tx.value, "ether")} ETH`
          );
        });
      }

      // Save the updated blocks array as JSON with BigInt-safe handling
      fs.writeFileSync(
        "all_blocks.json",
        JSON.stringify(blocks, (key, value) =>
          typeof value === "bigint" ? value.toString() : value,
          2
        )
      );

      lastBlock = current;
    }
  }, 2000);
}

watchBlocks();

