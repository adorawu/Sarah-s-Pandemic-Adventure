
import sys,time,random

typing_speed = 200 #wpm
def slow_type(t):
    for l in t:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print ()

#function to print how lady feels
def print_lady(h, m):
    if m <= 0 or h <= 0: 
        lady = """
                /////////////////
               ((((((((((((((((((
               )))  /       \  (((
               ((( (X)     (X) )))
               )))     <       (((
               (((      O      )))
               )))\___________/(((
                      _) (_
                     / \_/ \\
                    /(     )\\
                   /  )___(  \\
                     (     )
                    (       )
                     |  |  |
                      | | |
                      | | |
                     _|_|_|_"""

    elif m <= 50:                   
        lady = """
                /////////////////
               ((((((((((((((((((
               )))  /       \  (((
               ((( (*)     (*) )))
               )))     <       (((
               (((   .----.    )))
               )))\___________/(((
                      _) (_
                     / \_/ \\
                    /(     )\\
                   /  )___(  \\
                     (     )
                    (       )
                     |  |  |
                      | | |
                      | | |
                     _|_|_|_"""

    elif h <= 50:                     
        lady = """
                /////////////////
               ((((((((((((((((((
               )))  /       \  (((
               ((( (~)     (~) )))
               )))     <       (((
               (((   )~~~~~(   )))
               )))\___________/(((
                      _) (_
                     / \_/ \\
                    /(     )\\
                   /  )___(  \\
                     (     )
                    (       )
                     |  |  |
                      | | |
                      | | |
                     _|_|_|_"""
    else:
        lady = """
                /////////////////
               ((((((((((((((((((
               ))) ~~      ~~  (((
               ((( (*)     (*) )))
               )))     <       (((
               ((( '\______/`  )))
               )))\___________/(((
                      _) (_
                     / \_/ \\
                    /(     )\\
                   /  )___(  \\
                     (     )
                    (       )
                     |  |  |
                      | | |
                      | | |
                     _|_|_|_"""
    return lady

# Output that tells you that you live to see another day
def next_day(health, mental_health):
    print()
    print("""~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
    print("A day passes...\nHealth: " + str(health) + "\nMental Stability: " + str(mental_health))
    print()

# Output that tells you that you died
def die(health = 0, mental_health = 0):
    print(print_lady(health, mental_health))
    print("GAME OVER: Sarah got sick and died.")
    
# Output that tells you that you're too sad to continue
def sad(health = 0, mental_health = 0):
    print(print_lady(health, mental_health))
    print("GAME OVER: Sarah got depression from lack of social interaction and cannot continue.")

def over_hundred(x):
    if x > 100:
        x = 100
    return x
    
#Scene Counter to proceed to next scene
def scene_checker(scene):
    if scene == 0:
        return"Hi! My name is Sarah! I am a woman and I need your help making girlboss decisions so I can slay my way through this pandemic.\n Right now it's 2019 and I heard there is a spooky disease going around.\n But I need to go outside and feel the fresh air on my flesh. Should I go?\n"
    
    elif scene == 1:
        return"I have a presentation to do for my class that's worth 50 percent of my grade. Should I go to school?"
    
    elif scene == 2:
        return"My friend wants to hang out with me in the park with masks on. Should I go hang out with them?"
        
    elif scene == 3:
        return"My friend is inviting me to go out for dinner. Should I go to dinner?"
        
    elif scene == 4:
        return"PARTAYY time! My friend is inviting me to go with them! Should I go?"

    elif scene == 5:
        return"I just heard from the news that there's a vaccine for this disease. Should I get the vaccine?"
        
    elif scene == 6:
        return"Those darn rats ate all of my food! I have to go grocery shopping now. Should I go grocery shopping?"
        
    elif scene == 7:
        return"My neighbors knocked on my door to give me cookies. Should I talk to them?"
    
    elif scene == 8:
        return"My family is visiting me for the weekend and they want to go to an amusement park. Should I go with them?"
        
# define a main function
def play_game():
    while True:
        scene = 0
        health = 100
        mental_health = 100
        error_msg = "I don't understand what you just said, what was that?"

        #Scene 0 : Get fresh air?
        print()
        slow_type(scene_checker(scene)) # this prints the question
        print(print_lady(health, mental_health))

        while True:
            choice = input("Type Yes or No: ")
            print()
            if choice.lower() == "yes":
                chance_of_sick = random.random() #Generates a float between 0.0 and 1.0
                if chance_of_sick > 0.5:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("Oh no, somone walked next to me while coughing, and now I feel sick")
                    health -= 20
                    mental_health += 5
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("Wow that was so refreshing, I love the outdoors!")
                    health += 0
                    mental_health += 10
                
                break
            if choice.lower() == "no":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("Yeah it's better safe than sorry, but I wish I could be in the fresh air")
                health += 10
                mental_health -= 30
                
                break
            else:
                slow_type(error_msg)
                continue
        
        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1

        #Scene 1: Go to school and do presentation?
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("Type Yes or No: ")
            if choice.lower() == "yes":
                chance_of_sick = random.random() #Generates a float between 0.0 and 1.0
                if chance_of_sick > 0.5:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("Phew! The presentation went better than expected, but a lot of people were sniffling and it was so distracting...")
                    health -= 30
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("Phew! The presentation went better than expected! I feel great!")
                    mental_health += 5
                
                break
            if choice.lower() == "no":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I won't go, but not just because I want to skip school. I'm worried about getting sick")
                health += 10
                mental_health -= 30
                
                break
            else:
                print(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1

        #Scene 2: Go to the park with friend while wearing masks?
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("Type Yes or No: ")

            if choice.lower() == "yes":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I had fun hanging out with my friend while staying safe from the disease!")
                mental_health += 10
                
                break
            if choice.lower() == "no":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I wish I could hang out with my friend but I don't want to risk catching the disease.")
                health += 10
                mental_health -= 30
                
                break
            else:
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1

        #Scene 3: Go to dinner with friends?
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))

        while True:
            choice = input("""What should I do?
            0: Go to Olive Garden with my friends
            1: Suggest having a picnic dinner in a field with social distancing
            2: Decline the invite
            Type the corresponding number: """)

            if choice == "0":
                chance_of_sick = random.random() #Generates a float between 0.0 and 1.0
                if chance_of_sick > 0.3:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("I had a great dinner with my friend but now my stomach doesn't feel good and my throat hurts.")
                    mental_health += 10
                    health -= 30
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("I had a great dinner with my friend, but my waiter was looking very sickly.")
                    health -= 20
                    mental_health += 10
                
                break
            if choice == "1":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("My friend agreed to having a social distancing picnic. I'm glad we are staying safe!")
                mental_health += 10
                health += 10
                
                break
            if choice == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I wish I could hang out with my friend but I don't want to risk catching the disease. I'll eat something healthy from my fridge instead.")
                health += 10
                mental_health -= 30
                
                break
            else:
                slow_type(error_msg)
                continue
            
        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1

        #Scene 4: Party with friends?
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))

        while True:
            choice = input("""What should I do? 
            0: Stay home
            1: Go with friends but lay off the alcohol
            2: Get wasted
            Type the corresponding number: """)

            if choice == "0":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I can relax but I still feel lonely.")
                health += 10
                mental_health -= 30
                
                break
            if choice == "1":
                chance_of_sick = random.random() #Generates a float between 0.0 and 1.0
                if chance_of_sick > 0.1:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("I'm having fun with my friends, but my throat is getting sore and my social battery is dying.")
                    health -= 30
                    mental_health -= 5
    
                else:
                    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    print()
                    slow_type("I'm having fun with my friends! Yay!")
                    health += 0
                    mental_health += 20
                
                break
            if choice == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I'm having the time of my life but I'm starting to feel nauseous.")
                health -= 20
                
                break
            else:
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1
        
        #Scene 5: Vaccine
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("Choose Yes or No: ")

            if choice.lower() == "no":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("Well, my immune system will have to fight this disease on its own.")
                health -= 0
                mental_health += 0
                
                break
            if choice.lower() == "yes":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I got the vaccine! Now my immune system is protected.")
                health += 50
                mental_health += 10
                
                break
            else:
                print()
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
        scene += 1

        #Scene 6: Grocery shopping
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("""What should I do?
            0: Go grocery shopping and don't wear a mask since I don't feel sick
            1: Go grocery shopping and wear a mask
            2: Stay home
            Type the corresponding number: """)

            if choice == "0":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I got my groceries but now I'm starting to feel congested")
                health -= 30
                mental_health += 10
                
                break
            if choice == "1":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I got my groceries!")
                health += 10
                mental_health += 10
                
                break
            if choice == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I don't have any food at home. I guess I'll starve.")
                health -= 40
                mental_health -= 40
                
                break
            else:
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
            
        scene += 1

        #Scene 7: Neighbor is at the door with cookies
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("""What should I do?
            0: Don't answer the door
            1: Answer the door and tell them you don't want any cookies
            2: Answer the door and eat the cookies
            Type the corresponding number: """)

            if choice == "0":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I did not answer them but now I feel bad.")
                health += 5
                mental_health -= 30
                
                break
            if choice == "1":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I opened the door but kindly told them I didn't want any cookies. They must think I hate their cookies.")
                health -= 0
                mental_health -= 30
                
                break
            if choice == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I opened the door and kindly accepted their cookies. However, my stomach is starting to feel weird.")
                health -= 20
                mental_health += 10
                
                break
            else:
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)
            
        scene += 1

        #Scene 8: Go to amusement park with family?
        print()
        slow_type(scene_checker(scene))
        print(print_lady(health, mental_health))
        
        while True:
            choice = input("""What should I do?
            0: Go the amusement park with my family
            1: Suggest that we go hiking instead while social distancing
            2: Decline their invitation
            Type the corresponding number: """)

            if choice == "0":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I went to the amusement park, but I threw up after riding the roller coaster and now I have a cough")
                health -= 20
                mental_health += 10
                
                break
            if choice == "1":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I had fun hiking with my family while also staying safe from the disease.")
                health += 10
                mental_health += 10
                
                break
            if choice == "2":
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                print()
                slow_type("I haven't seen my family in months and I am depressed. But at least I'm staying safe from the disease")
                health += 10
                mental_health -= 40
                
                break
            else:
                slow_type(error_msg)
                continue

        if health <= 0:
            die()
            break
        if mental_health <= 0:
            sad()
            break
        else:
            health = over_hundred(health)
            mental_health = over_hundred(mental_health)
            next_day(health, mental_health)

        #Winning Ending
        slow_type("Hooray! I survived! Thanks for all your help! :)")
        break

def main():
    slow_type("Sarah's Pandemic Adventure!\n Help Sarah navigate life during the pandemic.\n")
    play_game()
    slow_type("The end! Want to start from the beginning?")
    choice = input("Yes or No? ")
    while True:
        if choice.lower() == "yes":
            print("\n\n\n")
            main()
        if choice.lower() == "no":
            slow_type("Thanks for playing!\n Credits: Kyla Lee, Linda Lam, Celeste Hoang, and Adora Wu :)")
            break
        break

# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)
if __name__=="__main__":
# call the main function
    main()
