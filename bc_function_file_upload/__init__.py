import logging
import json
from .manager import Manager
import azure.functions as func



def main(req: func.HttpRequest):
    try:  
        logging.info('Python HTTP trigger function processed a request.')

        user_id = req.params.get('user_id')
        file_object = req.files["file_name"]
        name_of_the_file = req.files["file_name"].filename
        file_data_stream = file_object.read()
        file_data = json.loads(file_data_stream)

        obj = Manager()
        result = obj.get_details(name_of_the_file,file_data)
        return func.HttpResponse(f"{json.dumps(result)}")
        #return func.HttpResponse(f"Hello,{result},{name_of_the_file},{file_data_stream} This HTTP triggered function executed successfully.")

    except Exception as e:
        error_name = str(e)
        return func.HttpResponse(f"Hi, {error_name}  ",status_code=400)
    finally:
        pass    