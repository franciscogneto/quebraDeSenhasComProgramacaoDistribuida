from mpi4py import MPI
import time
from argon2 import PasswordHasher

def main():
    comm = MPI.COMM_WORLD
    id = comm.Get_rank()            
    qtt_process = comm.Get_size()  
    
    with open('./wordlist.txt','r') as wordlist:
      passwords = wordlist.readlines()
      wordlist_length = passwords.__len__()

    if ((wordlist_length % qtt_process) == 0 and qtt_process <= wordlist_length):
        offset = int(wordlist_length / qtt_process)
        start = id * offset
        stop = start + offset
        start_time = time.time()
        finished = False
        password_input = 'blowjob'
        hasher = PasswordHasher()
        hash = hasher.hash(password_input)
        for i in range(start, stop):
            aux_password = passwords[i].strip()
            try:
              hasher.verify(hash, aux_password)
              print('Password ({}) find by process {} in {} s'.format(aux_password, id, time.time() - start_time))
              finished = True
              break
            except:
              if hasher.check_needs_rehash(hash):
                hash = hasher.hash(input)
        if not finished:
          print("Total time execution by process {}: {} s".format(id, time.time() - start_time))
    else:
        if id == 0 :
            print("number of process must be equal, divisible or less than wordlist length ({})".format(wordlist_length))

main()