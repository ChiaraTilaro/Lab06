from database.DB_connect import DBConnect
from model.vendite import Vendita


class SalesDao:

    def getAnni(self):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor()
            query = """
            SELECT DISTINCT YEAR(gds.Date)
                FROM go_daily_sales gds
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
            return None

    def getVenditeFiltrate(self , anno , brand , retailer_code):
        cnx = DBConnect.get_connection()
        if cnx is not None:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT gds.*, gds.Unit_sale_price*gds.Quantity AS Ricavo
                FROM go_daily_sales gds, go_retailers gr, go_products gp 
                WHERE gds.Retailer_code  = gr.Retailer_code  
                AND gds.Product_number = gp.Product_number 
                AND (YEAR(gds.Date)=COALESCE(%s,YEAR(gds.Date)))
                AND (gp.Product_brand =COALESCE(%s,gp.Product_brand))
                AND (gr.Retailer_code =COALESCE(%s,gr.Retailer_code))"""
            cursor.execute(query, (anno, brand, retailer_code,))
            result = []
            for row in cursor:
                result.append(Vendita(row["Date"],
                                   row["Quantity"],
                                   row["Unit_price"],
                                   row["Unit_sale_price"],
                                   row["Retailer_code"],
                                   row["Product_number"],
                                   row["Order_method_code"]))
            cursor.close()
            cnx.close()
            return result
        else:
            print("Errore nella connessione")
            return None

