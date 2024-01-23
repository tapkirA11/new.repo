email = input('Enter the email id: ')
if email.endswith ('@gmail.com') or email.endswith ('@rediffmail.com')  or email.endswith ('@yahoo.com'):
    print("valid email id")
else:
    print("invalid email id")
