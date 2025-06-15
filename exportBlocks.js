const fs = require("fs");
const Web3 = require("web3");
const web3 = new Web3.default("http://localhost:8545");

(async () => {
  const latest = await web3.eth.getBlockNumber();
  const blockData = [];

  for (let i = 0; i <= latest; i++) {
    const block = await web3.eth.getBlock(i, true); // true to include transactions
    blockData.push(block);
  }

 fs.writeFileSync("exported_blocks.json", JSON.stringify(blockData, (key, value) =>
  typeof value === "bigint" ? value.toString() : value, 2));
  console.log(`✅ Exported ${blockData.length} blocks to exported_blocks.json`);
})();
