

##
##  套件載入。
import fastapi, uvicorn


##
##  建立一個應用。
application = fastapi.FastAPI()


##
##  根據應用，新增一個路徑。
##  當呼叫該路徑，執行'root'函數。
@application.get("/")
async def root():
    response  = ""
    response += "The response from the first API.\n"
    response += "The name of function is 'root'.\n"
    return(response)


##
##
if(__name__=='__main__'):

    ##  設定參數，啟動服務器，
    ##  參數'reload=True'代表當偵測到腳本改變，將會重新啟動服務器，方便開發。
    uvicorn.run("01:application", host="localhost", port=5000, reload=True)