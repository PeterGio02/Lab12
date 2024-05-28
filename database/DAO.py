from database.DB_connect import DBConnect
from model.retailer import Retailer


class DAO():
    def __init__(self):
        pass


    @staticmethod
    def getAllyears():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                select distinct Country
                from go_retailers gr
                """

        cursor.execute(query)

        for row in cursor:
            result.append(row['Country'])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getVertici(nazione):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """
                    select *
                    from go_retailers gr
                    where Country = %s
                """

        cursor.execute(query,(nazione,))

        for row in cursor:
            result.append(Retailer(row["Retailer_code"],row["Retailer_name"],row["Type"],row["Country"],0))






        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchi(anno, r1, r2):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """select count(distinct gds1.Product_number) as 'n' 
                   from go_daily_sales gds1, go_daily_sales gds2
                   where gds1.Product_number = gds2.Product_number and year(gds1.Date) = %s and year(gds1.Date)=year(gds2.Date) and  gds1.Retailer_code= %s 
                   and gds2.Retailer_code= %s
                      
                   """

        cursor.execute(query, (anno, r1.Retailer_code, r2.Retailer_code),)

        for row in cursor:
            result = row['n']

        cursor.close()
        conn.close()
        return result



