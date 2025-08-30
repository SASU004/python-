import requests



class IRCTC:
    def __init__ (self):


        input (""" how would you  like to proceed?
               1. enter 1 to check live train sytatus 
               2. enter 2 to check PNR
               3. enter 3 to check train schedule""")
        
        if user_input == "1":
           print ( " live trai status ")
        elif user_input == "2":
           print ( " PNR status ")
        else:
           self.train_scedule()

    def train_scedule(self):
       train_no= input("Enter train number: ")
       self.fetch_data(train_no)

    def fetch_data(self, train_no):
       data = requestsget ()

        data=data.json()
       
       print (data)


obj=IRCTC()
    

        