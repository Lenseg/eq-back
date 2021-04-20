from ..repo import Repository
from ..repo.mongo import MongoRepository
from .schema import TransactionSchema

class Service(object):
 def __init__(self, repo_client=Repository(adapter=MongoRepository)):
   self.repo_client = repo_client

 def find_transactions(self, params):
   transactions = self.repo_client.find_all(params)
   return [self.dump(transaction) for transaction in transactions]

 def find_services(self):
  services = self.repo_client.find_services()
  return self.dump(services);

 def create_transactions(self, transactions):
     self.repo_client.create(transactions)
     return self.dump(transactions)


 def get_service_types(self):
    return productTypes

 def dump(self, data):
    return TransactionSchema(exclude=['_id']).dump(data).data

productTypes = [
    {
     'name': 'шприц 1мл (кр. шапочки)',
     'id': 1,
     'type': 1
    },{
     'name': 'шприц 1мл (съемки) 1',
     'id': 2,
     'type': 1
    },{
     'name': 'шприц 2 мл',
     'id': 3,
     'type': 1
    },{
     'name': 'шприц 3 мл',
     'id':4,
     'type': 1
    },{
     'name': 'шприц 5 мл',
     'id':5,
     'type': 1
    },{
     'name': 'шприц 10 мл',
     'id':6,
     'type': 1
    },{
     'name': 'презерватив',
     'id':7,
     'type': 1
    },{
     'name': 'салфетка',
     'id':8,
     'type': 1
    },{
     'name': 'Консультации/направления по ВИЧ',
     'id':9,
     'type': 2
    },{
     'name': 'Консультации/направления по гепатитам',
     'id': 10,
     'type': 2
    },{
     'name': 'Консультации/направления туберкулез',
     'id': 11,
     'type': 2
    },{
     'name': 'Консультации/направления по ИППП',
     'id': 12,
     'type': 2
    },{
     'name': 'Консультации/направления по ПИО',
     'id': 13,
     'type': 2
    },{
     'name': 'Консультации/направления по лечению наркозависимости',
     'id': 14,
     'type': 2
    },{
     'name': 'Консультации/направления по юридическим вопросам',
     'id': 15,
     'type': 2
    },{
     'name': 'Тест на ВИЧ сделано',
     'id': 16,
     'type': 4
    },{
     'name': 'Тест на Гепатит',
     'id': 17,
     'type': 4
    },{
     'name': 'Налоксон',
     'id': 18,
     'type': 3
    },{
     'name': 'Иглы',
     'id': 19,
     'type': 1
    },{
     'name': 'Консультации/направления по передозировкам',
     'id': 20,
     'type': 2
    },{
     'name': 'Консультации/направления по другим вопросам',
     'id': 21,
     'type': 2
    },{
     'name': 'Информационные материалы',
     'id': 22,
     'type': 1
    },{
     'name': 'Дополнительные раздаточные материалы',
     'id': 23,
     'type': 1
    },{
     'name': 'Консультации/направления по больницам',
     'id': 24,
     'type': 2
    },{
     'name': 'Консультации/направления по СЦ',
     'id': 25,
     'type': 2
    },{
     'name': 'Медицинские консультации и услуги',
     'id': 26,
     'type': 2
    },{
     'name': 'Сопровождение в органы власти',
     'id': 27,
     'type': 2
    },{
     'name': 'Консультации родственникам',
     'id': 28,
     'type': 2
    },{
     'name': 'Жалобы в гос. органы',
     'id': 29,
     'type': 2
    },{
     'name': 'Консультации по восстановлению документов',
     'id': 30,
     'type': 2
    },{
     'name': 'Консультации по вопросам детей',
     'id': 31,
     'type': 2
    },{
     'name': 'Консультации (число) психолога',
     'id': 32,
     'type': 2
    },{
     'name': 'Дошедшие до СЦ',
     'id': 31,
     'type': 2
    },{
     'name': 'Получившие мед помощь',
     'id': 33,
     'type': 2
    },{
     'name': 'Консультации (человек) психолога',
     'id': 34,
     'type': 2
    },{
     'name': 'Тест на ВИЧ роздано',
     'id': 35,
     'type': 4
    },{
     'name': 'Количество посещений в больницах',
     'id': 35,
     'type': 2
    },{
     'name': 'Проведенных групп',
     'id': 36,
     'type': 2
    },{
     'name': 'Сопровождение в больницы',
     'id': 37,
     'type': 2
    },{
     'name': 'Количество кейсов',
     'id': 35,
     'type': 2
    },{
     'name': 'Количество новых кейсов',
     'id': 36,
     'type': 2
    },{
     'name': 'Количество участников получивших юридическую помощь/консультацию',
     'id': 37,
     'type': 2
    },{
     'name': 'Количество консультаций (не участников) по юридической помощи (в том числе по телефону, тг, и тп)',
     'id': 38,
     'type': 2
    },{
     'name': 'Из них приведшие к положительному решению проблемы',
     'id': 39,
     'type': 2
    },{
     'name': 'Из них консультаций по уголовным делам',
     'id': 40,
     'type': 2
    },{
     'name': 'Из них консультаций по медицинским делам',
     'id': 41,
     'type': 2
    },{
     'name': 'Из них консультаций по гражданским делам ( в том числе семейным)',
     'id': 42,
     'type': 2
    },{
     'name': 'Из них консультаций по административным правонарушениям',
     'id': 43,
     'type': 2
    },{
     'name': 'В том числе в суды',
     'id': 44,
     'type': 2
    },{
     'name': 'Набор по самотестированию',
     'id': 45,
     'type': 4
    }
]
