def getReponse(serviceName: str,data = None, responseStatus= "success", errorMessage: str= None ,statusCode: int = None,  payload  = None, totalData=None):
    responseFormat = {
        "serviceName" : serviceName, 
        "totalData" : totalData,
        "meta" :  {
            "response" : responseStatus,
            "errorMessage" : errorMessage if errorMessage else None,
            "statusCode" : statusCode,
            "payload" : payload,
        } ,
        "data" : data,
    }
    return responseFormat