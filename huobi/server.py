#!/bin/python

import rpyc
import HuobiService as hb
rpyc.core.protocol.DEFAULT_CONFIG['allow_pickle'] = True

class MyService(rpyc.Service):
    #def on_connect(self, conn):
        # code that runs when a connection is created
        # (to init the service, if needed)
    #    pass

    #def on_disconnect(self, conn):
        # code that runs after the connection has already closed
        # (to finalize the service, if needed)
    #    pass

    def exposed_get_answer(self): # this is an exposed method
        return 42

    exposed_the_real_answer_though = 43     # an exposed attribute

    def get_question(self):  # while this method is not exposed
        return "what is the airspeed velocity of an unladen swallow?"

    def exposed_get_kline(self, symbol, period, size):
        return hb.get_kline(symbol, period, size)

    def exposed_setkey(self, access, secret):
        hb.setkey(access, secret)
        return

    def exposed_orders_list(self, symbol, states):
        return hb.orders_list(symbol, states)

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=18861)
    t.start()