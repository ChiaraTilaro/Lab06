from database.product_dao import ProductDao
from database.retailer_dao import RetailerDao
from database.sales_dao import SalesDao


class Model:
    def __init__(self):
        self.sales_dao = SalesDao()
        self.product_dao = ProductDao()
        self.retailer_dao = RetailerDao()
        self.retailers_map = {}

    def getAnni(self):
        return self.sales_dao.getAnni()

    def getBrand(self):
        return self.product_dao.getBrand()

    def getRetailer(self):
        return self.retailer_dao.getRetailer(self.retailers_map)

    def getTopVendite(self , anno , brand , retailer_code):
        vendite = self.sales_dao.getVenditeFiltrate(anno , brand , retailer_code)
        vendite.sort(reverse = True)
        return vendite[0:5]

    def getStatisticheVendite(self , anno , brand , retailer_code):
        vendite = self.sales_dao.getVenditeFiltrate(anno , brand , retailer_code)
        ricavoTotale = sum(vendita.ricavo for vendita in vendite)
        numeroRetailer = set([vendita.retailer_code for vendita in vendite])
        numeroProdotti = set([vendita.product_number for vendita in vendite])
        return ricavoTotale , len(vendite) , len(numeroRetailer) , len(numeroProdotti)
