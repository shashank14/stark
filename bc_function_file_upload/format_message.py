
class DisplayMessssge:

    def __init__(self):
        pass

    def format_the_display_message_file_extention(self,result):
        try:
            
            message_to_display = {"status":200,"file_upload_status":"File upload Terminated","message":result[0]["geojson"]["geojson_check_message"]}
            #print(message_to_display)
            return message_to_display
        except Exception as e:
            pass
        finally:
            pass

    def format_the_display_message_invalid_data_format(self,result):
        try:
            message_to_display = {"status":200,"file_upload_status":"File upload Terminated","message":result[1]["data_format"]["file_data_format_check_message"]}
            #print(message_to_display)
            return message_to_display
        except Exception as e:
            pass
        finally:
            pass

    def format_the_display_message_invalid_crs_and_attributes_datatypes(self,result):
        try:
            msg=""
            if result[2]["crs"]["crs_check_flag"] is False:
                msg = msg + str(result[2]["crs"]["crs_check_message"])
            if result[3]["attributes"]["attribute_check_flag"] is False:
                msg = msg + str(result[3]["attributes"]["attribute_check_message"])
            if result[4]["data_type"]["datatype_check_flag"] is False:
                msg = msg + str(result[4]["data_type"]["datatype_check_message"])

            #message = str(result[2]["crs"]["crs_check_message"])+", "+str(result[3]["attributes"]["attribute_check_message"])+ ", "+result[4]["data_type"]["datatype_check_message"]
            message_to_display = {"status":200,"file_upload_status":"File upload Terminated","message":msg}
            #print(">>",message_to_display)
            return message_to_display
        except Exception as e:
            pass
        finally:
            pass