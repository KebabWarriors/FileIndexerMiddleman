import rpyc
from py4j.java_gateway import JavaGateway

class Middleman(rpyc.Service):
    def on_connect(self, conn):
        pass

    def on_disconnect(self, conn):
        pass
