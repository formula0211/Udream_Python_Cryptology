from Crypto.Hash import SHA256, SHA224, SHA384, SHA512




messege = ('한글메시지')
messege_byte = bytearray(messege, 'utf8')






h = SHA256.new()
h.update(messege.encode('utf8'))
print('SHA256:', h.hexdigest())



h = SHA224.new()
h.update(messege.encode('utf8'))
print('SHA224:', h.hexdigest())



h = SHA384.new()
h.update(messege.encode('utf8'))
print('SHA384:', h.hexdigest())



h = SHA512.new()
h.update(messege.encode('utf8'))
print('SHA512:', h.hexdigest())




