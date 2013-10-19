# enter name


def enter_name():
    import re
    
    name = raw_input("please enter your name:")

    for char in name:
        if not re.match('[A-Za-z]',char):
            name = raw_input("enter name")
        else:
            new_file = open("details.txt","w")
            new_file.write("name is "+name+"\n")
            new_file.close()

    return name



# enter age

def enter_age():
    
    age = raw_input("please enter your age:")

    while(True):
        if int(age) not in range(10,60):
            print "sorry, please enter again"
            age = raw_input("enter age:")
        else:
            new_file = open("details.txt","a")
            new_file.write("age is "+age+"\n")
            new_file.close()
            break
        
    return age


# enter contact number

def enter_contact():
    
    import re
    contact_no = raw_input("enter contact number")
    number = str(contact_no)


    while(True):
        if not re.match('[0-9]',contact_no):
            print "Please try again"
            contact_no = raw_input("enter contact number")
        else:
            new_file = open("details.txt","a")
            new_file.write("contact number is "+contact_no+"\n")
            new_file.close()
            break
            

    return contact_no


# enter email

def enter_email():
    
    email = raw_input("Please enter your email")

    while(True):
        if '@' not in email:
            print "please try again"
            email = raw_input("Please enter your email")
        else:
            new_file = open("details.txt","a")
            new_file.write("email is "+email+"\n")
            new_file.close()
            break

    return email

