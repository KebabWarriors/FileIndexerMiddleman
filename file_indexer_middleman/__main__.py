from file_indexer_middleman.middleman import Middleman
from rpyc.utils.server import ThreadedServer

if __name__ == '__main__':
  middleman = Middleman()
  server = ThreadedServer(middleman, port=18861)
  server.start()

