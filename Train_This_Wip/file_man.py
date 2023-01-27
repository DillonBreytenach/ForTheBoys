#ToDo::
    #ENCRYPTION/DECRYPTION

import os
#from cryptography.fernet import Fernet
from pathlib import Path


class File_Man():
    def __init__(self, **kwargs):
        pass
 
    def get_tree(self):
        pass

    def build_tree(self):
        try:
            # PROJECT_DATA
            #   | -SOCKET_DATA
            #      |--IN_BOUND.txt
            #      |--OUT_BOUND.txt
            #      |--MSG_OF.txt
            #      |--MSG_TO.txt
            #      |--USER.txt
            #      |--CONTS.txt
            #   | -MSGS
            #       |--*DYNAMIC*.txt
            #   | -CHATS
            #       |--CONTS_STATE.txt
            #       |--CURRENT.txt
            #       |--TARGET_STATE.txt
            self.make_dir("TEST_ONE")
            self.make_dir("TEST_TWO")
            self.make_dir("TEST_THREE")

            self.make_dir("TEST_ONE/FOLDER_ONE")
            self.make_dir("TEST_ONE/FOLDER_TWO")
            self.make_dir("TEST_ONE/FOLDER_THREE")

            self.test_files = ["TEST_0.txt","TEST_1.txt", "TEST_2.txt", "TEST_3.txt", "TEST_4.txt", "TEST_4.txt"]


            for f in self.test_files:
                self.write_file("TEST_ONE/FOLDER_ONE/"+str(f), "", "*", "w")
                self.write_file("TEST_TWO/"+str(f), "", "*", "w")

        except Exception as e:
            return "ERROR_READING_FILE"

    def make_dir(self, path):
        os.mkdir(path)
        return 0

    def file_list(self, path):
        file_list = []
        file_list = os.listdir(path)
        return file_list

    def clean_data(self, data, delim):
        n_data = data[2:-2]
        n_list = n_data.split(str(delim))
        return n_list

    def read_file(self, file_name, delim):
        if file_name:
            try:
                with open(file_name, "r") as rf:
                    data = rf.readlines()
                    rf.close()
                    if str(data) == "[]" or str(data) == "['']":
                        return ''
                    return (self.clean_data(str(data), delim))
            except Exception as e:
                print("ERROR_READING_FILE", str(e))
                return "ERROR_READING_FILE"
    
    def write_file(self, file_name, data, delim, rwm):
        if file_name == "MSGS/['A'].txt":
            return
        text = ""
        fc = self.check_file(file_name)
        if fc == False:
            os.system('touch ' + file_name)
            print(f"[FILE_MADE]\n    [>{str(file_name)}<]")
        if file_name:
            if type(data) == str:
                #print("WRITING STR:: ", str(data))
                text = data
            elif type(data) == list:
                for _ in data:
                    text += str(_) + str(delim)
                #print("WRITING LIST:: ", str(data))
            elif type(data) == str and len(data) == 0:
                text = ""
            #print(f'TEXT_TO_WRITE: \n {text}')      
            with open(file_name, rwm) as wf:
                wf.write(text)
                wf.close()
            return

    def check_file(self, file_name):
        print(f"[CHECK_FILE]::[>{str(file_name)}<]")
        path_to_file = file_name
        path = Path(path_to_file)
        if path.is_file():
            print(f'[IsFile]\n    [>{file_name}<]\n    [>{path}<]')
            return True
        else:
            print(f'[NotFile]\n    [>{file_name}<]\n    [>{path}<]')
            return False

    def check_dir(self, dir_name):
        print(f"[CHECK_DIR]::[>{str(dir_name)}<]")
        path_to_file = dir_name
        path = Path(dir_name)
        try:
            if os.path.isdir(dir_name):
                print(f"[IsDir]\n    [>{dir_name}<]\n    [>{path}<]")
                return True
            else:
                print(f"[NotDir]\n    [>{dir_name}<]\n    [>{path}<]")
                return False
        except Exception as e:
            print(f'\n\n!![ERROR]!!\n[DIR_TEST]::[>{str(e)}<]')



#FOR LATER ON...


#    def encrypt(self, data):
#        pass
#
#    def decrypt(self, data):
#        pass
#
#    def load_key(self):   
#        """
#        Loads the key from the current directory named `key.key`
#        """
#        return open("login.txt", "rb").read()
#
#    def write_key():
#        """
#        Generates a key and save it into a file
#        """
#        key = Fernet.generate_key()
#        with open("key.key", "wb") as key_file:
#            key_file.write(key)    
