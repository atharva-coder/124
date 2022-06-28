from re import U
from flask import Flask,jsonify,request
app=Flask(__name__)
tasks=[{
    'id':1,
    'title':u'buy groceries',
    'description':u'milk,cheese,pizza,fruits',
    'done':False
    
},
{
    'id':2,
    'title':u'learn python',
    'description':u'need to find a good python tuorial on web',
    'done':False
}]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"please provide the data"
        },400)
    task={
            'id':tasks[-1]['id']+1,
            'title':request.json['title'],
            'description':request.json.get('description',""),
            'done':False


        }
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added successfully"
    },200)

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
app.run(debug=True)