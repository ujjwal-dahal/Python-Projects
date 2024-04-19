import random as rd


def rock_paper_scissor():
    yes_no = 'y'
    
    game_list = ['r','p','s']
    print("""\n******************* CHOOSE *******************
          r as Rock
          p as Paper
          s as Scissor \n""")
    
    print(""" *********** RULE ***********
          Draw : 1 Point
          Win : 2 Point \n""")

    while yes_no!='n':
        count = 5
        user_score=0
        comp_score=0
        while count!=0:
            #ch = user choice
            ch = input("\n -> Your Turn : ")
            #c = computer choice
            c = rd.choice(game_list)
            
            if(ch=='r' and c=='r'):
                print(f" Your : Rock Computer : Rock So DRAW")
                user_score+=1
                comp_score+=1
            elif(ch=='r' and c=='p'):
                print(f" Your : Rock Computer : Paper so You LOOSE")
                comp_score+=2
            elif(ch=='r' and c=='s'):
                print(f" Your : Rock Computer : Scissor so You WIN")
                user_score+=2
                
            elif(ch=='p' and c=='r'):
                print(f" Your : Paper Computer : Rock so You WIN")
                user_score+=2
            elif(ch=='p' and c=='p'):
                print(f" Your : Paper Computer : Paper So DRAW")
                user_score+=1
                comp_score+=1
            elif(ch=='p' and c=='s'):
                print(f" Your : Paper Computer : Scissor so You LOOSE")
                comp_score+=2
            
            elif(ch=='s' and c=='r'):
                print(f" Your : Scissor Computer : Rock so You LOOSE")
                comp_score+=2
            elif(ch=='s' and c=='p'):
                print(f" Your : Scissor Computer : Paper so You WIN")
                user_score+=2
            elif(ch=='s' and c=='s'):
                print(f" Your : Scissor Computer : Scissor So DRAW")
                user_score+=1
                comp_score+=1
                
            else:
                print("""\n ******************* Choose *******************
            r as Rock
            p as Paper
            s as Scissor \n""")
                ch = input("Your Turn : ")
                
                if(ch=='r' and c=='r'):
                    print(f" Your : Rock Computer : Rock So DRAW")
                    user_score+=1
                    comp_score+=1
                elif(ch=='r' and c=='p'):
                    print(f" Your : Rock Computer : Paper so You LOOSE")
                    comp_score+=2
                elif(ch=='r' and c=='s'):
                    print(f" Your : Rock Computer : Scissor so You WIN")
                    user_score+=2
                    
                elif(ch=='p' and c=='r'):
                    print(f" Your : Paper Computer : Rock so You WIN")
                    user_score+=2
                elif(ch=='p' and c=='p'):
                    print(f" Your : Paper Computer : Paper So DRAW")
                    user_score+=1
                    comp_score+=1
                elif(ch=='p' and c=='s'):
                    print(f" Your : Paper Computer : Scissor so You LOOSE")
                    comp_score+=2
                
                elif(ch=='s' and c=='r'):
                    print(f" Your : Scissor Computer : Rock so You LOOSE")
                    comp_score+=2
                elif(ch=='s' and c=='p'):
                    print(f" Your : Scissor Computer : Paper so You WIN")
                    user_score+=2
                elif(ch=='s' and c=='s'):
                    print(f" Your : Scissor Computer : Scissor So DRAW")
                    user_score+=1
                    comp_score+=1
            
            count-=1
            
        
    
        print(f" \n Your Score : {user_score} Computer Score : {comp_score}")
        if(user_score > comp_score):
            print("\n Your Score is HIGHER than Computer Score so You WIN")
        elif (user_score < comp_score):
            print("\n Your Score is LESSER than Computer Score so You LOOSE")
        else:
            print("\n Your Score and Computer Score Both are SAME so DRAW")   
      
        yes_no = input("\n --> Do You Wanna Play Game Again ? (y/n) : ")
        
rock_paper_scissor()

