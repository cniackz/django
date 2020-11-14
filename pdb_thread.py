import threading
import pdb

class SomeThread(threading.Thread):
  def run(self):
    a = 1
    print a
    pdb.set_trace()
    print 'a'

def main():
  print 'hola'
  someThread = SomeThread()
  someThread.start()

if __name__ == '__main__':
  main()