from bitcoin import *

privateKey = sha256("LuxorForums Bitcoin Wallet")
publicKey = privtopub(privateKey)
address = pubtoaddr(publicKey)

print (privateKey)
print (publicKey)
print (address)
