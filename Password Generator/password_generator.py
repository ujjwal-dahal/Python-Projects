import random as rd
import string as st 


def pass_gen():
    print("""Which Type Of Password You Want To Create ?
                    1. Simple(Weak) Password
                    2. Medium Password
                    3. Strong Password \n""")
    choice = int(input("\n Choose 1 , 2 or 3 : "))


    if(choice>=1 and choice<=3):
        match choice:
            case 1:
                len_pw = int(input("\n Enter Length Of Password : "))
                _string = st.ascii_letters
                password = "".join(rd.choice(_string) for i in range(len_pw))
                print(f" Generated Password : {password} \n")
            case 2:
                len_pw = int(input("\n Enter Length Of Password : "))
                _string = st.ascii_letters + st.digits
                password = "".join(rd.choice(_string) for i in range(len_pw))
                print(f" Generated Password : {password} \n")
            case 3:
                len_pw = int(input("\n Enter Length Of Password : "))
                _string = st.ascii_letters + st.digits + st.punctuation
                password = "".join(rd.choice(_string) for i in range(len_pw))
                print(f" Generated Password : {password} \n")
    else:
        print("\n Error !! Choose 1 , 2 or 3 !! \n")
        
        
if __name__ == "__main__":
    pass_gen()
            