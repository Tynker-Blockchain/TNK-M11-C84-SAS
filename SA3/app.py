from flask import Flask, render_template, request
import os
from hash import generateHash

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}
encryptedData ={}

@app.route("/", methods= ["GET", "POST"])
def home():
    print("running")
    print(request.args.get("form"))
    global blockData, encryptedData
    validation = None
    if request.method == "GET":
        return render_template('index.html')
    # Check if request.args.get("form") is "f1" i.e request came from 'f1' form
    elif request.args.get("form") == "f1":
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
       
        blockData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount
            }
        
        sender = generateHash(sender)
        receiver = generateHash(receiver)
        blockHash = generateHash(sender+receiver+amount)

        encryptedData = { 
                "sender": sender, 
                "receiver": receiver, 
                "amount": amount,
                "hash" : blockHash
            }
    # Add else     
    else:
        # Recieve sender, receiver, amount, hash data sent via form        
        sender = request.form.get("sender")
        receiver = request.form.get("receiver")
        amount = request.form.get("amount")
        hash = request.form.get("hash")
        
        # Concatinate sender, receiver and amount and generateHash and store the result in validateHash variable
        validationHash = generateHash(sender+receiver+amount)

        # Check if validationHash is equal to the hash received from the form data
        if validationHash == hash:
            # Store "Success" string in 'message' variable
            message= "Success"   
        else: 
            # Else store "Failed" string in the 'message' variable
            message = "Failed"

        # Create 'validation' dictionary and store 'message', 'blockHash', 'validationHash' keys in it with respective values
        validation = { 
               "message": message,
               "blockHash": hash,
               "validationHash": validationHash 
        }    

    # Also return validation as validation
    return render_template('index.html', blockData = blockData, encryptedData = encryptedData, validation = validation)
    
if __name__ == '__main__':
    app.run(debug = True, port=4000)