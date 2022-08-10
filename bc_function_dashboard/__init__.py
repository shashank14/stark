import logging
import json
from .manager import Manager
import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:  
        logging.info('Python HTTP trigger function processed a request.')

        user_id = req.params.get('user_id')

        obj = Manager()
        result = obj.get_details(user_id)
        return func.HttpResponse(f"{json.dumps(result)}")
        #return func.HttpResponse(f"Hello,{result},{name_of_the_file},{file_data_stream} This HTTP triggered function executed successfully.")

    except Exception as e:
        error_name = str(e)
        return func.HttpResponse(f"Hi, {error_name}  ",status_code=400)
    finally:
        pass  
