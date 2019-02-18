#Basic personal assistant by: Robert Sardilla
#Started development @ february 3 2019 
print("Hi there, i am your basic personal assistant")
version = ("0.0.3 dev build")
yes = ["Yes", "yes", "YES", "y", "Y"]
no = ["No", "no", "NO", "n", "N"]
male = ["Male", "m", "MALE", "male"]
female = ["Female", "f", "FEMALE", "female"]
from configparser import ConfigParser
write_data = ConfigParser()
def write():
    write_data = ConfigParser()
    write_data['bva_user_id'] = {
    'username': username,
    'gender': gender,
    }
    with open('data_bva.txt', "w") as data_bva:
        write_data.write(data_bva)
def name():
    global username
    input_name = input("May i know your name maam?sir?, so that i can properly help you (Leave Blank to skip): ")
    if input_name != (""):
        username = input_name
    else:
        username = ("Shy Person")
def gend():
    global gender
    input_gender = input("May i know your gender " + username + "? (Male/female, Leave blank to skip): ")
    if input_gender in male:
        gender = ("sir")
    elif input_gender in female:
        gender = ("maam")
    else:
        gender = ("")
try:
    with open('data_bva.txt', "r") as test_read_bva:
        read_bva = ConfigParser()
        read_bva.read('data_bva.txt')
        (read_bva.get('bva_user_id','username'))
except:
    name()
    gend()
    write()
else:
    username = (read_bva.get('bva_user_id','username'))
    gender = (read_bva.get('bva_user_id','gender'))
import datetime
atlas = datetime.datetime.now()
if atlas.hour <= 11:
    print("Goodmorning " + gender + " " + username + ",  i am glad to meet you.")
elif atlas.hour >= 17:
    print("Good Evening " + gender + " " + username + ", i am glad to meet you.")
elif atlas.hour >= 11:
    print("Good Afternoon " + gender + " " + username + ", i am glad to meet you.")
#commands functions
def help():
    print(gender +  username + " here are the lists of available commands (1/1)")
    print("help")
    print("time")
    print("date")
    print("rename")
    print("version")
    print("shut down")
    print("reset")
    cmd()
def time():
    import datetime
    time = datetime.datetime.now()
    print(time.strftime("%I-%M-%p"))
    cmd()
def date():
    import datetime
    date = datetime.datetime.now()
    print(date.strftime("%B-%d-%Y"))
    cmd()
def rename():
    global username
    username = input("To what name do you want to change your name " + gender + " " + username +"? ")
    print("Your name has been changed to " + username)
    write()
    cmd()
def versionf():
    print(gender + " " + username + " My current version is " + version)
    cmd()
def shut_down():
    sd_option = input("Are you sure you want to shut down? (Yes/No) ")
    if sd_option in yes:
        print("basic virtual assistant has been shut down")
    elif sd_option in no:
        cmd()
    else:
        print("invalid input")
        shut_down()
def reset():
    print("Are you really sure you want to erase all of data on your Basic Virtual Assistant?")
    erase = input("Type \"CONFIRM\" to permanently your bvl data: ")
    if erase == ("CONFIRM"):
        import os
        if os.path.exists("tdl_database.txt"):
            os.remove("tdl_database.txt")
            print("Your Bvl database has been reset")
        else:
            print("Bvl database does not exist")
            reset()
#command executer
def cmd():
    command = input("How may i help you " + gender + " " + username + "? ")
    if command == ("help"):
        help()
    elif command == ("time"):
        time()
    elif command == ("date"):
        date()
    elif command == ("rename"):
        rename()
    elif command == ("version"):
        versionf()
    elif command == ("shut down"):
        shut_down()
    elif command == ("reset"):
        reset()
    else:
        print("command \"" + command + "\" does not exist")
        print("Pls type help for the list of commands available")
        cmd()
cmd()