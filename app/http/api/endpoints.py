from flask import Flask, json, g, request
from app.transactions.service import Service as Transaction
from app.transactions.schema import TransactionSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
transactionService = Transaction();

@app.route("/", methods=["GET"])
def index():
 return json_response(transactionService.find_transactions())

@app.route("/transactions", methods=["POST"])
def create():
   transactions = json.loads(request.data)
   for transaction in transactions:
       TransactionSchema().load(transaction)
   transactionService.create_transactions(transactions)
   return json_response({})

@app.route("/transaction/", methods=["GET"])
def get_all_transactions():
    return json_response(transactionService.find_transactions())

@app.route("/transaction/<int:service>", methods=["GET"])
def get_transactions(service_id):
    return json_response(transactionService.find_transactions({"service":service_id}))


@app.route("/services", methods=["GET"])
def find_services():
    return json_response({})


@app.route("/services/types", methods=["GET"])
def get_service_types():
    return json_response(transactionService.get_service_types())

def json_response(payload, status=200):
 return (json.dumps(payload), status, {'content-type': 'application/json'})
