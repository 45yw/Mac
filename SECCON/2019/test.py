import hashlib
print('Valid flag.' if hashlib.sha1(input('Please your flag:').encode('utf-8')).hexdigest() == '3c90b7f38d3c200d8e6312fbea35668bec61d282' else 'wrong.')
