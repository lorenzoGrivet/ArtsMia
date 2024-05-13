import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._artObjectList=DAO.getAllObjects()
        self._grafo=nx.Graph()
        self._grafo.add_nodes_from(self._artObjectList)
        self._idMap={}
        for v in self._artObjectList:
            self._idMap[v.object_id]=v


    def creaGrafo(self):
        self.addEdges()


    def addEdges(self):
        self._grafo.clear_edges()

        #ciclo sui nodi se grafo è piccolo
        # for u in self._artObjectList:
        #     for v in self._artObjectList:
        #         peso = DAO.getPeso(u,v)
        #         self._grafo.add_edge(u,v,weigth=peso)

        #oppure faccio query
        allEdges=DAO.getAllConnessioni(self._idMap)

        for e in allEdges:
            self._grafo.add_edge(e.v1,e.v2,weigth=e.peso)



    def checkExistence(self,idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._grafo.nodes)

    def getNumEdges(self):
        return len(self._grafo.edges)