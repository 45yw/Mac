from hashlib import*
hashed_a1 = 'c627e19450db746b739f41b64097d449'
nonce = 'bbKtsfbABAA=5dad3cce7a7dd2c3335c9b400a19d6ad02df299b'
nc = '00000001'
cnonce = '9691c249745d94fc'
qop = 'auth'

uri = '/~q9/flag.html'
a2 = 'GET:' + uri
hashed_a2 = md5(a2).hexdigest()

seed = hashed_a1 + ':' + nonce + ':' + nc + ':' + cnonce + ':' + qop + ':' + hashed_a2
response = md5(seed).hexdigest()

print 'Use this seed : ' + seed + '\n'
print 'Use this response : ' + response + '\n'
