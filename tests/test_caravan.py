import sys

sys.path.append('../')
# import main modules
from data import Data
from say import Say
from ask import Ask


# init main modules
say = Say(print)
ask = Ask(say)
data = Data(ask)


sys.path.append('../events')
from caravan import Caravan
crv = Caravan(data, say, ask)
# crv.probability['rob'] = 100
# crv.probability['pillage'] = 0
# crv.probability['return'] = 5


while True:
    crv.start()

