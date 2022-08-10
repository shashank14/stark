import pandas as pd
import psycopg2

class Dashboard:

    def __init__(self) -> None:
        pass

    def querty_builder(self,*args,**kwagrs):
        try:
            #print(kwagrs)
            values = kwagrs
            #print(kwagrs)
            select_query_string =  ''' select  filename,fileurl,date,userid,status farmland_file 
            where user_id in () '''.format(file_name=values.get("file_name"),
            file_url=values.get("file_url"),date=values.get("date"),user_id=values.get("user_id"),
            status=values.get("status")
            )
            return select_query_string

        except Exception as e:
            pass
        finally:
            pass

    def get_dash_board(self):
        try:
            conn = psycopg2.connect(database="spatest", user='geouser', password='geopass', host='localhost', port= '5432')
            # cursor = conn.cursor()
            # dfd = pd.read_sql(select_query_string, conn)
            # dfd["date"] = dfd["date"].astype(str)
            # dfd.to_json(orient='records')
            # values = list(dfd.columns)
            # json.dumps(values)            
            # conn.close()
            return 
        except Exception as e:
            pass
        finally:
            pass
            if conn:
                conn.close()