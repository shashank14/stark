                   


                    # upload the file to blob

                #return result[0],{"data_format":None},{"crs":None},{"attributes":None},{"data_type":None}
            # elif len(result) == 2:
            #     format_message = format_message.DisplayMessssge()
            #     msg = format_message.format_the_display_message_invalid_data_format(result)
            #     return 'msg-2'
            #     #return result[0],result[1],{"crs":None},{"attributes":None},{"data_type":None}
            # elif len(result) == 4:
            #     if result[2]["crs"]["crs_check_flag"] is False or result[3]["attributes"]["attribute_check_flag"] is False or result[4]["data_type"]["datatype_check_flag"] is False:
            #         format_message = format_message.DisplayMessssge()
            #         msg = format_message.format_the_display_message_invalid_crs_and_attributes_datatypes(result)
            #         return msg
            #     else:
                    # db = Database()
                    # file_id = db.insert_file_record()
                    # # now coverted to python native dict
                    # file_data = json.loads(file_data_stream)
                    # file_data_stream_after_update = json.dumps(file_data)
                    # # insert record to data base

                    # con_str_blob = "DefaultEndpointsProtocol=https;AccountName=asterix;AccountKey=Y9lTVwq4QPArxH7iOuCCJkx7L05lA2PeywpxgnvWW5barkirRH9gA4//gTVSKywPW89dSut5rOjA+ASt+grJ8w==;EndpointSuffix=core.windows.net"
                    # container_name="geopython"

                    # name_of_the_file.split('.')
                    # unique_stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
                    # name_of_file = str(unique_stamp)+"."+str('geojson')
                    # container_client = ContainerClient.from_connection_string(con_str_blob,container_name)
                    # blob_client = container_client.get_blob_client(name_of_file)
                    # blob_client.upload_blob(file_data_stream_after_update)
                    # # upload the file to blob



                        # def get_details(self,name_of_the_file,file_data_stream):
    #     try:

    #         check_new_file = template_check_new_file.TemplateCheckNewFile()
    #         result = check_new_file.check_template(name_of_the_file,file_data_stream)
    #         if len(result) == 1:
    #             format_message = format_message.DisplayMessssge()
    #             msg = format_message.format_the_display_message_file_extention(result)
    #             return msg
    #         else:
    #             db = database_manager.Database()
    #             file_id = db.insert_file_record()
    #             # now coverted to python native dict
    #             file_data = json.loads(file_data_stream)
    #             # update the file_id, user_id and country_id
    #             file_data_stream_after_update = json.dumps(file_data)
    #             blob_manager.BlobFileUpload(file_data_stream_after_update)
 
    #             msg = {'status': 200, 'file_upload_status': "File upload Successfull"}
    #             return msg
    #     except Exception as e:
    #         pass
    #     finally:
    #         pass