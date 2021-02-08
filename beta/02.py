

##
##  套件載入。
import fastapi, uvicorn


##
##  建立一個應用。
application = fastapi.FastAPI()


##
##  根據應用，新增一個路徑'/'。
##  當呼叫該路徑，執行'root'函數。
@application.get("/")
async def root():
    response  = ""
    response += "The response from the first API.\n"
    response += "The name of function is 'root'.\n"
    return(response)


##
##  根據應用，新增一個路徑'item/{i}'，
##  當呼叫該路徑，執行'item'函數。
##  路徑中的'{i}'與函數'item'中的參數'i'必須一致。
##  其中'{i}'代表變數，將會透過參數'i'送入'item'函數。
@application.get('/item/{i}')
async def item(i):
    response = {"item":i}
    return(response)


##
##  根據應用，新增一個路徑'number/{n}'，
##  當呼叫該路徑，執行'number'函數。
##  路徑中的'{n}'與函數'number'中的參數'n'必須一致。
##  其中'{n}'代表變數，將會透過參數'n'送入'number'函數。
##  限制只能傳入整數，否則將不會得到正確的結果。
@application.get('/number/{n}')
async def number(n:int):
    response = {"number":n}
    return(response)


##
##  定義類'student'，
##  裡面有'name'、'age'，皆有預設值，類型使用字串。
class information:
    name   = 'Greg'
    age    = "18"


##
##  當路徑'/student/{v}'被呼叫時，
##  將變數{v}傳入函數'student'函數，其類別為字串。
@application.get("/student/{v}")
async def student(v):
    if(information.name==v):
        response  = "Detect with name.\n"
        response += "Student {} is exist.\n".format(v)
        response += "The age is {}.\n".format(information.age)
    if(information.age==v):
        response  = "Detect with age.\n"
        response += "Student {} is exist.\n".format(information.name)
        response += "The age is {}.\n".format(v)
    else:
        response  = "Not found with your input."
    return(response)


##
##
if(__name__=='__main__'):
 
    ##  設定參數，啟動服務器，
    ##  參數'reload=True'代表當偵測到腳本改變，將會重新啟動服務器，方便開發。
    uvicorn.run("02:application", host="localhost", port=5000, reload=True)