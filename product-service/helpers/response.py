def getReponse(serviceName: str,data = None, responseStatus= "success", errorMessage: str= None ,statusCode: int = None,  payload  = None):
    responseFormat = {
        "serviceName" : serviceName, 
        "meta" :  {
            "response" : responseStatus,
            "errorMessage" : errorMessage if errorMessage else None,
            "statusCode" : statusCode,
            "payload" : payload
        } ,
        "data" : data
    }
    return responseFormat