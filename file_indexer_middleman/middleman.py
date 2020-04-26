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

  def index(self, path):
    reader = self.gateway.jvm.com.kebabwarrios.es.Reader()
    reader.readDocumentsPath(path)

    file_indexer = self.gateway.jvm.com.kebabwarrios.es.FileIndexer(reader.getAllDocuments)

    self.file_indexers.append(file_indexer)

  def search(self, query):
    # TODO: Implement search logic.
    pass
