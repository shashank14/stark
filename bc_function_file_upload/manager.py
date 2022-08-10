from .template_check_new_file import TemplateCheckNewFile
from .database_manager import Database
from .blob_manager import BlobFileUpload
from .format_message import DisplayMessssge
import datetime as dt
import json

class Manager:

    def __init__(self):
        pass

    def get_details(self,name_of_the_file,file_data_stream):
        try:
            check_new_file = TemplateCheckNewFile()
            result = check_new_file.check_template(name_of_the_file,file_data_stream)
            if len(result) == 1:
                format_message = DisplayMessssge()
                msg = format_message.format_the_display_message_file_extention(result)
                return msg
                #return result[0],{"data_format":None},{"crs":None},{"attributes":None},{"data_type":None}
            elif len(result) == 2:
                format_message = DisplayMessssge()
                msg = format_message.format_the_display_message_invalid_data_format(result)
                return msg
                #return result[0],result[1],{"crs":None},{"attributes":None},{"data_type":None}
            elif len(result) == 5:
                if result[2]["crs"]["crs_check_flag"] is False or result[3]["attributes"]["attribute_check_flag"] is False or result[4]["data_type"]["datatype_check_flag"] is False:
                    format_message = DisplayMessssge()
                    msg = format_message.format_the_display_message_invalid_crs_and_attributes_datatypes(result)
                    return msg
            else:
                db = Database()
                file_id = db.insert_file_record()
                # # update the file_id, user_id and country_id
                # file_data_stream_after_update = json.dumps(file_data)
                file_data_stream_after_update = json.dumps(file_data_stream)
                blob_manager_object = BlobFileUpload()
                blob_num = blob_manager_object.upload_file_to_the_blob(file_data_stream_after_update)
                msg = {'status': 200, 'file_upload_status': "File upload Successfull"}
                return msg
        except Exception as e:
            pass
        finally:
            pass
