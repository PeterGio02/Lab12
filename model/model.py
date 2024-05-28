import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._retailers = None
        self._grafo = nx.Graph()
        self._idMap = {}
        #Per la ricorsione
        self._bestPath = []
        self._pesoMax = 0


    def fillDD(self):
        return DAO.getAllyears()

    def buildGraph(self, anno, nazione):
        self._grafo.clear()

        #NODI
        self._retailers = DAO.getVertici(nazione)
        for r in self._retailers:
            self._idMap[r.Retailer_code] = r

        self._grafo.add_nodes_from(self._retailers)

        #ARCHI
        for r1 in self._retailers:
            for r2 in self._retailers:
                if r1 != r2:
                    peso = DAO.getArchi(anno, r1, r2)
                    if peso > 0:
                        self._grafo.add_edge(r1, r2, weight=peso)


    def detailsGraph(self):
        return f"il grafo ha {len(self._grafo.nodes)} nodi e {len(self._grafo.edges)} archi"


    def calcolaVolume(self, r):
        volume=0
        vicini = self._grafo.neighbors(r)

        for n in vicini:
            volume += self._grafo[r][n]["weight"]

        r.Volume = volume







