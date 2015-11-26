from authorizenet import apicontractsv1
from authorizenet.apicontrollers import *
from decimal import *

merchantAuth = apicontractsv1.merchantAuthenticationType()
merchantAuth.name = '5KP3u95bQpv'
merchantAuth.transactionKey = '4Ktq966gC55GAX7S'

transactionrequest = apicontractsv1.transactionRequestType()
transactionrequest.transactionType = apicontractsv1.transactionTypeEnum.getDetailsTransaction
transactionrequest.refTransId = "2245592542"

request = apicontractsv1.createTransactionRequest()
request.merchantAuthentication = merchantAuth
request.refId = "Sample"
request.transactionRequest = transactionrequest

controller = createTransactionController(request)
controller.execute()

response = controller.getresponse()

if (response.messages.resultCode=="Ok"):
    print "SUCCESS"
    print "Message Code : %s" % response.messages.message[0].code
    print "Message text : %s" % response.messages.message[0].text
    if (response.transactionResponse.responseCode == "1" ):
        print "Payer Id : %s " % response.transactionResponse.secureAcceptance.PayerID
        print "Transaction ID : %s " % response.transactionResponse.transId
else:
    print "ERROR"
    print "Message Code : %s" % response.messages.message[0].code
    print "Message text : %s" % response.messages.message[0].text