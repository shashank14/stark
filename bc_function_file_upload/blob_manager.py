from azure.storage.blob import ContainerClient
import datetime as dt

class BlobFileUpload:

    def __init__(self) -> None:
        pass

    def upload_file_to_the_blob(self,file_data_stream_after_update):
        try:
            con_str_blob = "DefaultEndpointsProtocol=https;AccountName=asterix;AccountKey=Y9lTVwq4QPArxH7iOuCCJkx7L05lA2PeywpxgnvWW5barkirRH9gA4//gTVSKywPW89dSut5rOjA+ASt+grJ8w==;EndpointSuffix=core.windows.net"
            container_name="geopython"
            unique_stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")
            name_of_file = str(unique_stamp)+"."+str('geojson')
            container_client = ContainerClient.from_connection_string(con_str_blob,container_name)
            blob_client = container_client.get_blob_client(name_of_file)
            msg_from_blob = blob_client.upload_blob(file_data_stream_after_update)
            return msg_from_blob
        
        except Exception as e:
            pass
        finally:
            pass 