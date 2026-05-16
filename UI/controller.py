import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.anno = None
        self.brand = None
        self.retailer = None
        self.retailer_code = None

    def fillddAnno(self):
        anni = self._model.getAnni()
        for anno in anni:
            self._view.ddAnno.options.append(
                ft.dropdown.Option(anno[0])
            )
        self._view.update_page()

    def fillddBrand(self):
        brand = self._model.getBrand()
        for b in brand:
            self._view.ddBrand.options.append(
                ft.dropdown.Option(b[0])
            )
        self._view.update_page()

    def fillddRetailer(self):
        retailer = self._model.getRetailer()
        for r in retailer:
            self._view.ddRetailer.options.append(
                ft.dropdown.Option(key=r.retailer_code,
                                   text=r.retailer_name,
                                   )
            )
        self._view.update_page()

    def readAnno(self , e):
        if self._view.ddAnno.value == "None":
            self.anno = None
        else:
            self.anno = self._view.ddAnno.value

    def readBrand(self , e):
        if self._view.ddBrand.value == "None":
            self.brand = None
        else:
            self.brand = self._view.ddBrand.value

    def readRetailer(self , e):
        if self._view.ddRetailer.value == "None":
            self.retailer_code = None
        else:
            self.retailer_code = self._view.ddRetailer.value

    def handleTopVendite(self , e):
        topVendite = self._model.getTopVendite(self.anno , self.brand , self.retailer_code)
        self._view.txt_result.controls.clear()
        if len(topVendite) == 0:
            self._view.txt_result.controls.append(
                ft.Text("Nessuna vendita con i filtri selezionati")
            )
        else:
            for vendita in topVendite:
                self._view.txt_result.controls.append(
                ft.Text(vendita)
            )
        self._view.update_page()

    def handleAnalizzaVendite(self , e):
        statisticheVendite = self._model.getStatisticheVendite(self.anno , self.brand , self.retailer_code)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Satistiche vendite:"))
        self._view.txt_result.controls.append(ft.Text(f"Giro d'affari: {statisticheVendite[0]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero vendite: {statisticheVendite[1]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero retailers coinvolti: {statisticheVendite[2]}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero prodotti coinvolti: {statisticheVendite[3]}"))
        self._view.update_page()
