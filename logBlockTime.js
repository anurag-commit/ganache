const Web3 = require("web3");
const fs = require("fs");
const web3 = new Web3.default("http://localhost:8545");

(async () => {
  const latest = await web3.eth.getBlockNumber();
  const blocks = [];

  for (let i = 0; i <= latest; i++) {
    const block = await web3.eth.getBlock(i, true);
    const timestamp = new Date(Number(block.timestamp) * 1000).toLocaleString();
    blocks.push({
      blockNumber: block.number,
      timestamp,
      txCount: block.transactions.length
    });
  }

  fs.writeFileSync("block_times_log.json", JSON.stringify(blocks, (key, value) =>
    typeof value === "bigint" ? value.toString() : value, 2));

  console.log(`✅ Saved block time log to block_times_log.json`);
})();
