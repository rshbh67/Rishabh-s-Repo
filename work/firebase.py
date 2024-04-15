import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from flask import Flask , redirect , render_template, url_for ,request , jsonify

app = Flask(__name__)

# Initialize Firebase using a service account
cred = credentials.Certificate(r'/home/shopclues/Downloads/rishabh34-9a7b1-firebase-adminsdk-ljeri-642e197008.json')
firebase_admin.initialize_app(cred)

# Get a reference to the Firestore service
db = firestore.client()

doc_ref = db.collection('taskCollection').document()



@app.route('/product', methods=['POST'])
def add_product():
  dataa = request.json
  doc_ref.set(dataa)
  return "Data added successfully!"

@app.route('/phone',methods=['GET'])
def phone():
    docs = db.collection('taskCollection').get()
    ll=[]
    for doc in docs:
      ll.append(doc.to_dict().get("phone"))
      print(doc.to_dict().get("phone"))
      print(f'{doc.id} => {doc.to_dict().get("phone")}')

    # newpp=jsonify(ll)
    
    return jsonify(ll)


# @app.route('/phone',methods=['GET'])
# def track():
   
   



if __name__ == "__main__":
    app.run(debug=True)




# data = {
#     "name":"ujjwal",
#     "age" : 51,
#     "email":"ujjwal@gmail.com",
#     "phone": 8579878939
# }
# # Add a new document to the "users" collection


# # try:
 
# # except Exception as e:
# #     print("Error adding data: ", e)


# # Query Firestore to find documents where age is greater than or equal to 25
# # query = db.collection('taskCollection').where('age', '>=',40)

# # print(type(query))



# # Iterate over the results and print them
# # for doc in query.stream():
# #     print(f'{doc.id} => {doc.to_dict()}')



