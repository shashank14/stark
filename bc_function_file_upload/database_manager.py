#import psycopg2

class Database:

    def __init__(self) -> None:
        pass

    def querty_builder(self,*args,**kwagrs):
        try:
            #print(kwagrs)
            values = kwagrs
            #print(kwagrs)
            insert_query_string =  ''' insert into farmland_file (filename,fileurl,date,userid,status)
            values ('{file_name}','{file_url}',
            '{date}','{user_id}','{status}') RETURNING fileid; '''.format(file_name=values.get("file_name"),
            file_url=values.get("file_url"),date=values.get("date"),user_id=values.get("user_id"),
            status=values.get("status")
            )
            return insert_query_string

        except Exception as e:
            pass
        finally:
            pass

    def insert_file_record(self):
        try:

            # conn = psycopg2.connect(database="spatest", user='geouser', password='geopass', host='localhost', port= '5432')
            # values = {"file_name":"shashank","file_url":"conatiner/python","date":"2022-09-21","user_id":11,"status":1}
            # cursor = conn.cursor()
            #print(values)
            #insert_query_string = self.querty_builder(file_name="shashank",file_url="conatiner/python",date="2022-09-21",user_id="10",status="1")
            #print(insert_query_string)
            # cursor.execute(insert_query_string)
            # id_of_new_row = cursor.fetchone()[0]
            # conn.commit()
            # cursor.close()
            # conn.close()

            # append file_id,user_id and country_id to the data_dict
            # return the same
            return 101
        except Exception as e:
            pass
        finally:
            pass
            # if cursor:
            #     cursor.close()
            # if conn:
            #     conn.close()