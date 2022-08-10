import imp
import re
import json

class TemplateCheckNewFile:

    def __init__(self):
        pass
    
    def check_for_file_extention(self,name_of_the_file):
        try:
            match = re.search("\.geojson$", name_of_the_file)
            if match:
                return {"geojson":{"geojson_check_flag":True,"geojson_check_message":"The file has valid FileExtension"}}
            else:
                return {"geojson":{"geojson_check_flag":False,"geojson_check_message":"The file has invalid FileExtension"}}
        except Exception as e:
            pass
        finally:
            pass
       
    def check_for_crs(self,file_data_stream):
        try:
            crs = "WGS84"
            if crs == "WGS84":
                return {"crs":{"crs_check_flag":True,"crs_check_message":"The file has valid CRS"}}
            else:
                return {"crs":{"crs_check_flag":False,"crs_check_message":"The file has invalid CRS"}}
        except Exception as e:
            pass
        finally:
            pass

    def check_for_data_format(self,file_data_stream):
        try:
            file_data_format = "ifojson" #self.is_json(file_data_stream)
            if file_data_format == "json":
                return {"data_format": {"file_data_format_check_flag":True,"file_data_format_check_message":"The file has valid data format"}}
            else:
                return {"data_format": {"file_data_format_check_flag":False,"file_data_format_check_message":"The file has invalid data format"}}
        except Exception as e:
            pass
        finally:
            pass

    def is_json(data_stream):
        try:
            json.loads(data_stream)
        except ValueError as e:
            return False
        return True
    
    def check_for_attributes(self,file_data_stream):
        try:
            list_of_failed_attributes = [["Attribute Errors found prod_code 67456879"],["Attribute Errors found at prod_code 674568459"]]
            list_of_failed_attributes = []
            if len(list_of_failed_attributes)>0:
                return {"attributes":  {"attribute_check_flag":False,"attribute_check_message":str(list_of_failed_attributes)}}
            else:
                return {"attributes":  {"attribute_check_flag":True,"attribute_check_message":"All Attributes are in the correct format"}}
        except Exception as e:
            pass
        finally:
            pass

    def check_for_datatypes(self,file_data_stream):
        try:
            list_of_failed_datatypes = [["Datatype errors found at prod_code 67456879"],["Datatype errors found at prod_code 674568459"]]
            list_of_failed_datatypes = []
            if len(list_of_failed_datatypes)>0:
                return {"data_type":  {"datatype_check_flag":False,"datatype_check_message":str(list_of_failed_datatypes)}}
            else:
                return {"data_type":  {"datatype_check_flag":True,"datatype_check_message":"All Datatypes are correct in the correct format"}}
        except Exception as e:
            pass
        finally:
            pass

    def check_template(self,name_of_the_file,file_data_stream):
        try:
            result_for_file_extention = self.check_for_file_extention(name_of_the_file)
            if result_for_file_extention["geojson"]["geojson_check_flag"]==False:
                return result_for_file_extention,
            else:
                result_for_data_format = self.check_for_data_format(file_data_stream)
                if result_for_data_format["data_format"]["file_data_format_check_flag"]==False:
                    return result_for_file_extention,result_for_data_format,
            
                result_for_crs = self.check_for_crs(file_data_stream)
                result_for_attributes = self.check_for_attributes(file_data_stream)
                result_for_datatypes = self.check_for_datatypes(file_data_stream)


                if result_for_attributes["attributes"]["attribute_check_flag"] is False or result_for_datatypes["data_type"]["datatype_check_flag"] is False:
                    return result_for_file_extention,result_for_crs,result_for_attributes,result_for_datatypes
                else:
                    return result_for_file_extention,result_for_crs,result_for_attributes,result_for_datatypes
        except Exception as e:
            pass
        finally:
            pass    


