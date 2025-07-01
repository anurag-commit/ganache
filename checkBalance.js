web3.eth.getAccounts().then(accounts => {
  accounts.forEach(async acc => {
    const bal = await web3.eth.getBalance(acc);
    console.log(`${acc}: ${web3.utils.fromWei(bal, 'ether')} ETH`);
  });
});
