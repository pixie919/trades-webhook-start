rpc = "https://devnet-rpc.shyft.to?api_key=" # Devnet RPC
client = Client(rpc)
payer = Keypair()
mpg = "BRWNCEzQTm8kvEXHsVVY9jpb1VLbpv9B8mkF43nMLCtu" # Stakechip Devnet MPG Key
market_product_group_key = Pubkey.from_string(mpg)

ctx = SDKContext.connect(
  client=client,
  market_product_group_key=market_product_group_key,
  payer=payer,
  raise_on_error=True
)