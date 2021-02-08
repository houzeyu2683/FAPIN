

##
##  套件載入。
import fastapi, uvicorn


##
##  建立一個應用。
application = fastapi.FastAPI()


##
##  假設從資料庫中撈出一些資料，每筆資料透過dictionary包起來，
##  在將這些資料使用list包裝。
student = [{"name": "Tom"}, {"name": "Wade"}, {"name": "James"}]


##
##  沒有函數參數的類型，預設為字串，
##  所以在使用前必須將型態進行轉換。
@application.get("/student/")
async def filter(start, end):
    start, end = int(start), int(end)
    response = student[start : start + end]
    return(response)


##
##  函數參數可以給定預設值，如果沒有給定預設值，
##  必須在路徑中加入，否則不會有正確的回覆。
@application.get("/teacher/{name}")
async def teacher(name, age, gender = "male"):
    response = {
        "name":name,
        "age":age,
        "gender":gender
    }
    return(response)


##
##
if(__name__=='__main__'):
 
    ##  設定參數，啟動服務器，
    ##  參數'reload=True'代表當偵測到腳本改變，將會重新啟動服務器，方便開發。
    uvicorn.run("03:application", host="localhost", port=5000, reload=True)
