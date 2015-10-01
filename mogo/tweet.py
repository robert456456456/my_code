__author__ = 'Robert Adinihy'
from pymongo import MongoClient
class twitter_m():

    def User_name(self):
        username = input("Enter user name with quotes:")
        return username
    def Message(self):
        message= input("Enter Message with quotes:")
        return message

    def __init__(self):
        # connect to the MongoDB
        connection = MongoClient("localhost")
        # connect to the twitter database and the messages collection
        db = connection.twitter.messages
        # create a dictionary to hold twitter documents
        #  create dictionary
        message_record = {}
        # set flag variable
        flag = True
        # loop for data input
        while (flag):
            # ask for input
            twitter_username = self.User_name()
            twitter_message= self.Message()


            print  twitter_username,twitter_message
            # place values in dictionary
            message_record = {'user_name': twitter_username, 'message': twitter_message}
            # insert the record
            db.insert(message_record)
            # should we continue?
            flag = input('Enter another message record? ')
            if (flag[0].upper() == 'N'):
             flag = False

             # find all documents
             results = db.find()

             print()
             print('+-+-+-+-+-+-+-+-+-+-+-+-+-+-')

             # display documents from collection
             for record in results:

                print(record['user_name'] + ',', record['message'])

            print()

            # close the connection to MongoDB
            connection.close()
#run class
flag = True
while(flag):
 twitter_m().__init__()
 flag = input('Run again? ')
 if (flag[0].upper() == 'N'):
    flag = False

