import xmlrpc.client

url = 'http://192.168.10.178:8017'
db = 'durgarao'
username = 'admin'
password = 'admin'

common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
version = common.version()
print("version..........................", version)

uid = common.authenticate(db, username, password, {})
if uid:
    print("Authentication Success", uid)
else:
    print("authentication failed")

# Object Proxy to interact with models
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# try:
    # loan_ids = models.execute_kw(db, uid, password, 'room.info', 'search', [[]])
    # value = models.execute_kw(db, uid, password, 'bank.transaction', 'search', [[]])
    # print(value)
    # print("Loan IDs:", loan_ids)
    # id = models.execute_kw(db, uid, password, 'room.info', 'write', [[[],{'age':25}]])
    # id = models.execute_kw(db, uid, password, 'bank.transaction', 'search', [[]])
    # print(id)
    # for i in value:
        # id = models.execute_kw(db, uid, password, 'room.info', 'write', [[i], {'floor_number': 123456}])
        # id = models.execute_kw(db, uid, password, 'school.profile', 'unlink', [[i]])
        # print(id)
    # for i in loan_ids:
    #     id = models.execute_kw(db, uid, password, 'school.profile', 'write', [[[3], {'email': 'hp@gmail.com'}]])
    #     print(id)
    # print(value)
    # models.execute_kw(db, uid, password, 'bank.account', 'write', [[[5], {'name': 'Durgarao'}]])
    # for i in value:
    #     id = models.execute_kw(db, uid, password, 'bank.account', 'write', [[[i], {'name': 'Durgarao'}]])
    #     print(id)
    # value = models.execute_kw(db, uid, password, 'department.info', 'search', [[]])
    # value1 = models.execute_kw(db, uid, password, 'department.info', 'unlink', [[2]])
    # print(value1)

    # print(value)
    # for i in value:
    #     value2 = models.execute_kw(db, uid, password, 'employee.info', 'write', [[[i],{'name':'Dhatri','description':'hhg','manager':'22'}]])
    #     print(value2)
    # print(value)
    # field_name = 'x_name'  # Name of the field you want to delete
    # field_ids = models.execute_kw(db, uid, password, 'ir.model.fields', 'search', [[['name', '=', field_name]]])
    #
    # if field_ids:
    #     field_id = field_ids[0]
    #
    #     # Delete the field
    #     delete_result = models.execute_kw(db, uid, password, 'ir.model.fields', 'unlink', [[field_id]])
    #     print(f"Field {field_name} deleted successfully.")
    # else:
    #     print(f"Field {field_name} not found.")
    # value = models.execute_kw(db, uid, password, 'sale.order', 'search', [[]])
    # print(value)
    #
    # model_ids = models.execute_kw(db, uid, password, 'ir.model', 'search', [[['model', '=', 'sale.order']]])
    # if model_ids:
    #     model_id = model_ids[0]
    #
    #     # Create new field
    #     field_params = {
    #         'name': 'x_name10',  # Field name, must start with x_ if custom
    #         'field_description': 'Name111',  # Human-readable name
    #         'ttype': 'char',  # Field type
    #         # 'relation': 'bank.account',
    #         'model_id': model_id,  # ID of the model
    #         'state': 'manual',  # State, should be 'manual'
    #         'required': True,  # Required field
    #     }
    #
    #     new_field_id = models.execute_kw(db, uid, password, 'ir.model.fields', 'create', [field_params])
    #     print(f"Created new field with ID: {new_field_id}")
    # else:
    #     print("Model 'sale.order' not found.")
    # change = models.execute_kw(db,uid,password,'shopping.customer','create',[{'name':'durgarao'}])
    # change1 = models.execute_kw(db,uid,password,'shopping.customer','create',[{'name':'durgarao'}])
    # value1 = models.execute_kw(db, uid, password, 'sale.order', 'search', [[]])
    # value1 = models.execute_kw(db, uid, password, 'recycle.account', 'unlink', [[1]])
    # print(value1)
    # for i in value1:
    #     values2= models.execute_kw(db, uid, password, 'recycle.account', 'unlink',[[i]])
    #     print(values2)
    # print(value1)
    # value = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],{'offset':1,'limit':'10'})
    # value = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['is_company', '=', True]]],{'offset':1,'limit':'10'})
    # value0 = models.execute_kw(db, uid, password, 'res.partner', 'search_count', [[['is_company', '=', True]]])
    #
    # value1 = models.execute_kw(db, uid, password, 'bank.account', 'search', [[['gender', '=', 'male']]])
    # value3 = models.execute_kw(db, uid, password, 'bank.account', 'create', [{'name':'guru','account_number':123698547}])
    # id = models.execute_kw(db, uid, password, 'bank.transaction', 'create',[ {'account_number': "123456",'date':'2024-05-02','transaction_type':'deposit','amount':200000}])
    # id = models.execute_kw(db, uid, password, 'bank.transaction', 'write',[[1] ,{'account_number': "78910",'amount':400000}])
    # print("created filed id>>>>>>>>>>",id)
    # id = models.execute_kw(db,uid,password,'school.profile','write',[[8],{'name':'raju'}])
    # ids = models.execute_kw(db,uid,password,'bank.transaction','search',[[]])
    # id33 = models.execute_kw(db,uid,password,'bank.transaction','browse',[[ids]])
    # for i in ids:
    #     models.execute_kw(db, uid, password, 'school.student', 'write', [[i], {'name': 'swarup'}])

    # print("write filed id>>>>>>>>>>",id33)
    # if value1:
    #     value2 = models.execute_kw(db, uid, password, 'bank.account', 'read', [value1], {'fields': ['name']})
    #     print("Records read:", value2)
    # else:
    #     print("No records found with gender 'male'")

    # record_ids = list(value1)
    # value3 = models.execute_kw(db, uid, password, 'bank.account', 'write', [record_ids], {'gender': "female"})

    # print("Search result:", value)
    # print("search count:",value0)
    # print("search result:",value1)
    # print(value2)
    # print(len(value1))
# except xmlrpc.client.Fault as error:
#     print("XML-RPC Fault:", error)
