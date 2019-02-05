#basic personal assistant by: Robert Sardilla
#Started development @ february 3 2019 
version = ("0.0.2 dev build")
yes = ["Yes", "yes", "YES", "y", "Y"]
no = ["No", "no", "NO", "n", "N"]
male = ["Male", "m", "MALE", "male"]
female = ["Female", "f", "FEMALE", "female"]
print("Hi there, i am your basic personal assistant")
def yon():
    global username
    give_name = input("May i know your name, maam/sir?, so that i can properly help you (Yes, No): ")
    if give_name in yes:
     username = input("What is your name? ")
    elif give_name in no:
     username = ("Shy person")
    else:
        print("Invalid")
        yon()
def gend():
    global gender
    give_gender = input("May i know your gender " + username + "? (Male/female, Leave blank to skip): ")
    if give_gender in male:
        gender = ("sir")
    elif give_gender in female:
        gender = ("maam")
    else:
        gender = ("")
yon()
gend()
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
    else:
        print("command \"" + command + "\" does not exist")
        print("Pls type help for the list of commands available")
        cmd()
cmd()