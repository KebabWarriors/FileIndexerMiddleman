import rpyc
from py4j.java_gateway import JavaGateway
from gc import collect

class Middleman(rpyc.Service):
  def __init__(self):
    self.gateway = None
    self.file_indexers = []

  def on_connect(self, conn):
    self.gateway = JavaGateway()

  def on_disconnect(self, conn):
    collect()

  def exposed_index(self, path):
    reader = self.gateway.jvm.com.kebabwarriors.file_indexer.DocumentReader()
    reader.readDocumentsPath(path)

    file_indexer = self.gateway.jvm.com.kebabwarriors.file_indexer.FileIndexer(
        reader.getAllDocuments())

    self.file_indexers.append(file_indexer)

    return True

  def exposed_search(self, query):
    result = self.gateway.jvm.com.kebabwarriors.file_indexer.SearchEngine.search(query,
        self.file_indexers[0].getDocumentsMap(), self.file_indexers[0].getIndexedDocumentsMap())

    payload = {}

    for key in result:
      payload[key] = result[key]

    return payload
