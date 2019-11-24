import CanNetworkSimulator
import time
import decoder




while True:
    msg = CanNetworkSimulator.readCANNetwork()

    # print("message id: {} function: {} data: {} ".format(msg[0:2],msg[2:5],msg[5:]))
    decoded = decoder.decode(msg)
    print (decoded["name"],decoded["function"],decoded["data"],sep=" ")
    time.sleep(0.1)
    