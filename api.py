from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=['GET'])
def getany():
    return 'WEEEEEABCPIG'

@app.route("/getName", methods=['GET'])
def getname():    
    return {'name':['James','Robert','Penguin','John','David','Richard','Thomas']}
                               
if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=4208)  