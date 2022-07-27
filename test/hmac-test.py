import hmac
from hashlib import sha256

key = b'&s23@3fsd'
msg = b'hello lucio'
md5 = hmac.new(key, msg, digestmod=sha256).digest()
print(md5)
print(len(md5))
