from file_indexer_middleman.middleman import Middleman
from rpyc.utils.server import ThreadedServer

if __name__ == '__main__':
  middleman = Middleman()
  server = ThreadedServer(middleman, port=18861, protocol_config={"allow_public_attrs": True, "allow_all_attrs": True})
  server.start()

