import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

        self._listYear = []
        self._listCountry = []

    def fillDD(self):
        elencoNazioni = self._model.fillDD()
        for n in elencoNazioni:
            self._view.ddcountry.options.append(ft.dropdown.Option(n))
        self._view._page.update()


    def handle_graph(self, e):
        self._view.txt_result.controls.clear()

        anno = int( self._view.ddyear.value )
        nazione = self._view.ddcountry.value
        self._model.buildGraph(anno, nazione)
        self._view.txt_result.controls.append(ft.Text(self._model.detailsGraph()))
        self._view._page.update()


    def handle_volume(self, e):
        self._view.txtOut2.controls.clear()
        lista = []
        listaOrdinata = []
        for r in self._model._grafo.nodes:
            self._model.calcolaVolume(r)
            if r.Volume > 0:
                lista.append(r)

        listaOrdinata = sorted(lista, key=lambda x: x.Volume, reverse = True)

        for r in listaOrdinata:
            self._view.txtOut2.controls.append(ft.Text(r))


        self._view._page.update()




    def handle_path(self, e):
        self._view.txtOut3.controls.clear()
        N =  int( self._view.txtN.value )

        if N >= 2:
            print("test")

        else:
            self._view.create_alert("Inserire un numero maggiore o uguale a 2!")


