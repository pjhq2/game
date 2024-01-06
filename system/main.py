import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from system.test.sequence import sequence
from system.test.test     import test

if __name__ == '__main__':
    sequence()
    #test()
