import hashlib
import time
from argon2 import PasswordHasher


start = time.time()
input = 'cowboy'
hasher = PasswordHasher()
verifier = PasswordHasher()
hash = hasher.hash(input)
with open('./wordlist','r') as wordlist:
    for password in wordlist.readlines():
        # aux_password = hashlib.sha256(password.strip().encode()).hexdigest()
        # if input == aux_password:
        #     print('Password: {}'.format(aux_password))
        #     break
        try:
            aux_password = password.strip()
            hasher.verify(hash, aux_password)
            print('Password: {}'.format(aux_password))
            break
        except:
            if hasher.check_needs_rehash(hash):
                hash = hasher.hash(input)
            pass

print('Time execution: {}s'.format(time.time() - start))