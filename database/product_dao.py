from database.DB_connect import DBConnect


class ProductDao():

    def getBrand(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """
            select distinct gp.Product_brand 
from go_products gp 
            """
            cursor.execute(query)

            res = []
            for row in cursor:
                res.append(row)
            cursor.close()
            cnx.close()
            return res
        else:
            print("Errore nella connessione")
