print("the idiot test")

print("""
[1] Begin
""")

select = input("[Choose number 1]: ")

if select == '1':
    
    print("begining")
    
    print("Question 1")
    print("What color is the sky?")

    print("""
    [1] Blue
    [2] Green
    [3] Yellow
    [4] Purple
    """)
    q1 = input("[?]: ")

    if q1 == '1':
        print("Correct")
    
        print("Question 2")
        print("Who is the creator of this quiz?")

        print("""
        [1] ShotGunAlpha YT Studios
        [2] Jeff
        [3] Yo mama
        [4] Joe MAMA
        """)
        q2 = input("[?]: ")
        if q2 == '1':
            print("Correct")
    
            print("Question 3")
            print("Is this quiz over?")

            print("""
            [1] YES(This is the correct answer)
            """)
            q3 = input("[?]: ")
            if q3 == '1':
                print("Correct")
                print("Thanks for playing the Idiot Quiz")
                print("""
                [1] Close the idiot quiz
                """)
                leave = input("[?]: ")
                if leave == '1':
                    pass


        if q2 == '2':
            print("WRONG!!!!!!!!!!!!!!!")
        if q2 == '3':
            print("WRONG!!!!!!!!!!!!!!!")
        if q2 == '4':
            print("WRONG!!!!!!!!!!!!!!!")
    if q1 == '2':
        print("WRONG!!!!!!!!!!!!")
    if q1 == '3':
        print("WRONG!!!!!!!!!!!!")
    if q1 == '4':
        print("WRONG!!!!!!!!!!!!")
