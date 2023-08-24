# global constants
PASSWORD = "password"
USER = "user"
CODE = "code"
ADMIN= "admin"
SUPER = "superadmin"
LEVEL = "level"
RESULT = "result"

# users
users = [
    {
        "level": "user",
        "user": "carlos",
        "password": "123"
    },
    {
        "level": "admin",
        "user": "carlos1",
        "password": "1234"
    },
    {
        "level": "superadmin",
        "user": "carlos2",
        "password": "12345"
    }
]

def credentialsAreValid(user,password, requestedMethod):
    isValid = False

    for dbUser in users:
        isValid = dbUser[USER] == user and dbUser[PASSWORD] == password
        if isValid: 
            
            if dbUser[LEVEL] == ADMIN and requestedMethod == "getSuppliers":
                isValid = False

            if dbUser[LEVEL] == USER and requestedMethod != "getProducts":
                isValid = False

            break

    return isValid

def  authMiddleware(function):
    def autenticate(*args, **credentials):
        response = {}

        if PASSWORD in credentials and USER in credentials:
            if credentialsAreValid (credentials[USER],credentials[PASSWORD], function.__name__):
                response[CODE] = 200
                result = function(*args, **credentials)
                response[RESULT] = result
            else:
                response[CODE] = 404
        else:
            response[CODE] = 400

        return response
    
    return autenticate

# usr lel can only access to getProducts
@authMiddleware
def getProducts(**params):
    return {
        "productsIds":  [1,2,4]
    }

@authMiddleware
def getInvoices(**params):
    return {
        "InvoicesIds":  [1,2,4]
    }

# only visibe to superadmins
@authMiddleware
def getSuppliers(**params):
    return {
        "SuppliersIds":  [1,2,4]
    }

print(getProducts(user="carlos", password="123"))
print(getInvoices(user="carlos1", password="1234"))
print(getSuppliers(user="carlos", password="123"))