import learner
import recognizer
import dbconn

print("Sign up enter 1")
print("Sign in enter 2\n")
print("Select action from above two.")
print("Press 'q' for exit from camera view.\n")
action = raw_input('Select action : ')
email = raw_input('Enter email : ')
try:
    if int(action) == 1:
        name = raw_input('Enter name : ')
        res = dbconn.create_user(email, name)
        if res == True:
            id, name = dbconn.get_user(email)
            res_train = learner.learn_user(id)
            
            if res_train == True:
                print("\nUser sign up successful.")
            else:
                # delete user if training unsuccessful
                dbconn.del_user(id)
                print("\nUser sign up unsuccessful.")
        else:
            print('\nEmail address already exist.')
    elif int(action) == 2:
        res = dbconn.get_user(email)
        if res != None:
            id, name = res
            recognizer.recognize_face(id, name)
        else:
            print('\nPlease sign up.')
except Exception as e:
    print("\nInvalid action.")
