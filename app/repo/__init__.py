class Repository(object):
 def __init__(self, adapter=None):
   if not adapter:
     raise ValueError("Invalid repository implementation")
   self.client = adapter()

 def find_all(self, selector):
   return self.client.find_all(selector)

 def find(self, selector):
   return self.client.find(selector)

 def find_services(self):
  return self.client.find_services()

 def create(self, selector):
   return self.client.create(selector)
