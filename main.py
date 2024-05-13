#class imports
import pygame
from screens import Screens
from sounds import Sounds
from pakuri import Pakuri
from battle_dynamics import BattleDynamics

#begins pygame
pygame.init()
pygame.mixer.init()

#object initialization
screen = Screens(900, 900)
music = Sounds()
battle = BattleDynamics()


#counters and statements
current = None #move user currently selects
previous = None #move user previously selected

timer = pygame.time.Clock() #start pygame timer, this will keep track of system time
speed = 2 #speed at which the player actions text is displayed on the screen. INCREASE TO SLOW DOWN TEXT DISPLAY
counter = 0
textCounter = 0
#text = [""] * 4
activeDialogue = 0
isItDone = False
winCount = 0

#Player Teams and Turn
playerTurn = 1
pakuriTeamSize = 5
playerOneTeam = [Pakuri("Player One")] * 6
playerTwoTeam = [Pakuri("Player Two")] * 6

playerOneDisplayed = playerOneTeam[0]
playerTwoDisplayed = playerTwoTeam[0]

dialogue = ""
previousScreenState = ""
screenState = "welcome"

#soundQueues = 0 #will keep track of which sounds to play
selectButtonCounter = 0 #will keep track of how many times both players selected pakuris

run = True #determine when game ends
updateDialogue = False #will determine whether player actions need to be displayed


#boot up
screen.welcomeScreen()
pygame.mixer.music.load("music/welcome_screen_music.mp3")
pygame.mixer.music.play(loops=-1) #Will play indefinitely until next pygame.mixer

#game loop
while run:
    timer.tick(60)

    #battle music will begin playing after introductory battle music ends. Outside of the pygame.event so that it occurs automatically
    if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("music/during_battle_music.mp3")
            pygame.mixer.music.play(loops=-1)

    #will display player actions through here
    if updateDialogue == True:
        if dialogue.isdigit():
            #playerOne menu dialogue
            if int(dialogue)%2 != 0:
                print("IM IN DIALOGUE 1")
                if textCounter == 0:
                    pygame.draw.rect(screen.screen,(255, 255, 255), (40, 650, 550, 200))
                    pygame.draw.rect(screen.screen,(0, 0, 0), (40, 650, 550, 200), 9)

                print("ORIGINAL: ", displayedDialogue)
                #print("text:", text[activeDialogue], "### Text hardcoded: ", text[0])
                if counter < speed * len(displayedDialogue):
                    counter += 1
                    textCounter += 1

                elif counter >= speed * len(displayedDialogue):
                    isItDone = True
                #print("text: ", displayedDialogue)


                snip = font.render(displayedDialogue[0:(counter // speed)], False, (0, 0, 0))

                screen.screen.blit(snip, text2Rect)

                if isItDone and activeDialogue < len(text)-1:
                    activeDialogue += 1
                    isItDone = False
                    displayedDialogue = text[activeDialogue]
                    print(displayedDialogue)
                    counter = 0


                if activeDialogue == len(text)-1:
                    updateDialogue = False
                    activeDialogue = 0
                    textCounter = 0
                    if (updateDialogue == False and screen.whoWins() != "No One" and winCount == 0):

                        pygame.time.delay(300)
                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, screen.whoWins())
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        print(text[0])
                        updateDialogue = True
                        winCount += 1




            #playerTwo menu dialogu
            elif int(dialogue)%2 == 0:
                winCount = 0
                print("IM IN DIALOGUE 2")
                if textCounter == 0:
                    pygame.draw.rect(screen.screen,(255, 255, 255), (40, 650, 550, 200))
                    pygame.draw.rect(screen.screen,(0, 0, 0), (40, 650, 550, 200), 9)

                print("ORIGINAL: ", displayedDialogue)
                #print("text:", text[activeDialogue], "### Text hardcoded: ", text[0])
                if counter < speed * len(displayedDialogue):
                    counter += 1
                    textCounter += 1

                elif counter >= speed * len(displayedDialogue):
                    isItDone = True
                #print("text: ", displayedDialogue)


                snip = font.render(displayedDialogue[0:(counter // speed)], False, (0, 0, 0))

                screen.screen.blit(snip, text2Rect)

                if isItDone and activeDialogue < len(text)-1:
                    activeDialogue += 1
                    isItDone = False
                    displayedDialogue = text[activeDialogue]
                    print(displayedDialogue)
                    counter = 0


                if activeDialogue == len(text)-1:
                    updateDialogue = False
                    activeDialogue = 0
                    textCounter = 0
                    if (updateDialogue == False and screen.whoWins() != "No One" and winCount == 0):
                        pygame.time.delay(300)
                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, screen.whoWins())
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        print(text[0])
                        updateDialogue = True
                        winCount += 1

    if winCount == 1 and updateDialogue == False: run = False

    #display next player's turn in dialogue box
    if (updateDialogue == False and screenState == "Battle" and
          (previousScreenState == "Move Menu" or previousScreenState == "Pakuri Battle Menu")):
        pygame.time.delay(500)
        screen.updateBattleScreen("BATTLE", playerTurn)

    if (updateDialogue == False and (playerOneDisplayed.get_species() != "Player One" or playerTwoDisplayed.get_species() != "Player Two")
            and ((playerOneDisplayed.is_alive() is not True) or playerTwoDisplayed.is_alive() is not True)):
        playerOneDisplayed, playerTwoDisplayed = screen.getDisplayedPakuri()

        print("Player One Pakuri: " + playerOneDisplayed.get_species())
        print("Player Two Pakuri: " + playerTwoDisplayed.get_species())
        pygame.time.delay(300)
        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "DEAD")
        dialogue = str(playerTurn)
        displayedDialogue = text[activeDialogue]
        print(text[0])
        updateDialogue = True

    if (updateDialogue == False and screenState == "Battle" and
            previousScreenState == "Move Menu" and (battle.attackEffectiveness() != "Normal Power")):
        pygame.time.delay(300)
        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, battle.attackEffectiveness())
        dialogue = str(playerTurn)
        displayedDialogue = text[activeDialogue]
        print(text[0])
        updateDialogue = True

    for event in pygame.event.get():
        # ends program by clicking top right x
        if event.type == pygame.QUIT:
            run = False

        # this game will be based off of user mouse clicks
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # screenStates help us filter out which buttons the program should be looking for to be printed
            # welcome screen, beginning screen where player has access to 4 options: pakuri selection AKA Battle, pakuri information,
            # Instructions, and Credits
            if screenState == "welcome":
                # for reference:
                # button1 = Battle -> PlayerOne must pick pakuri then PlayerTwo picks
                # button2 = Info -> will display Pakudex, user will be able to see moveset, Pakuri, and its type
                # button3 = Instructions -> How to play
                # button4 = Credits -> Authors, Information, Education, etc
                if screen.button1.is_clicked(pygame.mouse.get_pos()):
                    previousScreenState = "welcome"
                    screenState = "playerOne pakuri selection"

                    print("Battle Button clicked!")
                    screen.pakuriSelectionOne()

                elif screen.button2.is_clicked(pygame.mouse.get_pos()):
                    print("Pakuri button clicked!")
                    screen.pakuriInfo()
                    screenState = "Pakudex"
                elif screen.button3.is_clicked(pygame.mouse.get_pos()):
                    print("Instructions button clicked!")
                    screen.Instructions()
                    screenState = "instructions"
                elif screen.button4.is_clicked(pygame.mouse.get_pos()):
                    print("Credits button clicked!")
                    screen.credits()
                    screenState = "credits"
            #Phase One of Pakuri Showdown has players 1 and 2 in their respective pakuri selection screens:
            #What determines who picks their pakuri is through the screenState
            elif screenState == "credits":
                if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                    screen.welcomeScreen()
                    screenState = "welcome"

            elif screenState == "instructions":
                if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                    screen.welcomeScreen()
                    screenState = "welcome"

            elif screenState == "Pakudex":
                for i in range(20):
                    #determines whether players has selected any of the pakuri names
                    if screen.pakuriSelection[i].is_clicked(pygame.mouse.get_pos()):
                        #displays the selected pakuri
                        font = screen.pakuriSelection[i].get_font()
                        screen.pakuriImage(screen.pakuriSelection[i].buttonName())
                        print(screen.pakuriSelection[i].buttonName())
                        screen.selectedButton(screen.pakuriSelection[i], font)
                        current = screen.pakuriSelection[i]
                        #position is maintained in order to determine which pakuri the user wishes to add to their team
                        position = i
                        #breaks loop immediately after selecting one

                        break

                if current != previous and (previous != None):
                    screen.unselectButton(previous, font)

                    screen.selectedButton(current, font)

                previous = current

                if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                    screen.welcomeScreen()
                    screenState = "welcome"

            elif screenState == "playerOne pakuri selection":
                #displays all pakuri names on the left hand side
                for i in range(20):
                    #determines whether players has selected any of the pakuri names
                    if screen.pakuriSelection[i].is_clicked(pygame.mouse.get_pos()):
                        #displays the selected pakuri
                        font = screen.pakuriSelection[i].get_font()
                        screen.pakuriImage(screen.pakuriSelection[i].buttonName())
                        print(screen.pakuriSelection[i].buttonName())
                        screen.selectedButton(screen.pakuriSelection[i], font)
                        current = screen.pakuriSelection[i]
                        #position is maintained in order to determine which pakuri the user wishes to add to their team
                        position = i
                        #breaks loop immediately after selecting one

                        break

                if current != previous and (previous != None):
                    screen.unselectButton(previous, font)

                    screen.selectedButton(current, font)

                previous = current
                #determines whether the select button is clicked
                if screen.selectButton.is_clicked(pygame.mouse.get_pos()):
                    print("select button clicked!")

                    #adds the pakuri player selected to their team
                    playerOneTeam[selectButtonCounter] = Pakuri(screen.pakuriSelection[position].buttonName())
                    print("Player One took ", playerOneTeam[selectButtonCounter].get_species())

                    #player pakuri count in their party increases by incrementing the selectButtonCounter
                    selectButtonCounter += 1

                    #will display how many more pakuris the player has left to select from
                    screen.unselectButton(current, font)
                    screen.pakuriSelectionOne()
                    screen.updatePakuriCounter(pakuriTeamSize - selectButtonCounter)

                #this if statement determines how many pakuris a player may select
                if(selectButtonCounter == pakuriTeamSize): #CHANGE BACK TO 5, kept at 1 for debugging purposes
                    #reset back to 0 for the next player's selection phase
                    selectButtonCounter = 0

                    #In the case that a player wished to reselect their team, they would be automatically sent back to the Pre Battle Stage
                    if (previousScreenState == "Pre-Battle Stage"):
                        previousScreenState = "playerOne pakuri selection"
                        screenState = "Pre-Battle Stage"
                        screen.confirmationScreen(playerOneTeam, playerTwoTeam)
                    else:
                        previousScreenState = "playerOne pakuri selection"
                        screenState = "playerTwo pakuri selection"
                        screen.pakuriSelectionTwo()

            #works the same as playerOne pakuri selection screenState
            elif screenState == "playerTwo pakuri selection":

                for i in range(20):
                    # determines whether players has selected any of the pakuri names
                    if screen.pakuriSelection[i].is_clicked(pygame.mouse.get_pos()):
                        # displays the selected pakuri
                        font = screen.pakuriSelection[i].get_font()
                        screen.pakuriImage(screen.pakuriSelection[i].buttonName())
                        print(screen.pakuriSelection[i].buttonName())
                        screen.selectedButton(screen.pakuriSelection[i], font)
                        current = screen.pakuriSelection[i]
                        # position is maintained in order to determine which pakuri the user wishes to add to their team
                        position = i
                        # breaks loop immediately after selecting one

                        break
                if current != previous and (previous != None):
                    screen.unselectButton(previous, font)

                    screen.selectedButton(current, font)
                previous = current

                if screen.selectButton.is_clicked(pygame.mouse.get_pos()):
                    print("select button clicked!")
                    playerTwoTeam[selectButtonCounter] = Pakuri(screen.pakuriSelection[position].buttonName())
                    print("Player Two took ", playerTwoTeam[selectButtonCounter].get_species())
                    selectButtonCounter += 1
                    screen.unselectButton(current, font)
                    screen.pakuriSelectionTwo()
                    screen.updatePakuriCounter(pakuriTeamSize - selectButtonCounter)

                if(selectButtonCounter == pakuriTeamSize): #CHANGE BACK TO 5
                    selectButtonCounter = 0
                    previousScreenState ="playerTwo pakuri selection"
                    screenState = "Pre-Battle Stage"
                    screen.confirmationScreen(playerOneTeam, playerTwoTeam)

            elif screenState == "Pre-Battle Stage":
                previous = None
                current = None
                if screen.confirmButton.is_clicked(pygame.mouse.get_pos()):
                    print("Confirm button clicked!")
                    previousScreenState = "Pre-Battle Stage"
                    screenState = "Battle"

                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("music/battle_music.mp3")
                    pygame.mixer.music.play()

                    screen.battleScreen()

                elif screen.p1ReselectButton.is_clicked(pygame.mouse.get_pos()):
                    print("Player 1 wants to reselect!")
                    previousScreenState = "Pre-Battle Stage"
                    screenState = "playerOne pakuri selection"
                    playerOneTeam = [Pakuri("Player One")] * 6
                    screen.pakuriSelectionOne()

                elif screen.p2ReselectButton.is_clicked(pygame.mouse.get_pos()):
                    previousScreenState = "Pre-Battle Stage"
                    screenState = "playerTwo pakuri selection"
                    print("Player 2 wants to reselect!")
                    playerTwoTeam = [Pakuri("Player Two")] * 6
                    screen.pakuriSelectionTwo()

            elif screenState == "Battle":
                if updateDialogue == False:
                    if screen.fightButton.is_clicked(pygame.mouse.get_pos()):
                        print("FIGHT FIGHT FIGHT")
                        print("Button Name is: ", screen.fightButton.buttonName())
                        screen.updateBattleScreen("FIGHT", playerTurn)
                        screenState = "Move Menu"


                    elif screen.pakuriButton.is_clicked(pygame.mouse.get_pos()):
                        print("SHOW ME MY TEAM!!!")
                        screen.updateBattleScreen("PAKURI", playerTurn)
                        screenState = "Pakuri Battle Menu"

                    elif screen.forfeitButton.is_clicked(pygame.mouse.get_pos()):
                        print("I SURRENDER!!!")
                        screen.updateBattleScreen("FORFEIT", playerTurn)
                        screenState = "Forfeit Menu"

                    elif screen.exitButton.is_clicked(pygame.mouse.get_pos()):
                        print("GOODBYE!")
                        screen.updateBattleScreen("EXIT", playerTurn)
                        screenState = "Exit Menu"

            elif screenState == "Move Menu":
                if updateDialogue == False:
                    for i in range(4):
                        if screen.displayedPakuriMoves[i].is_clicked(pygame.mouse.get_pos()):
                            screen.selectedButton(screen.displayedPakuriMoves[i])
                            current = screen.displayedPakuriMoves[i]
                            break
                    if current != previous and (previous!=None):
                        screen.unselectButton(previous)

                        screen.selectedButton(current)

                    previous = current

                    if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING BACK!!!")
                        screen.updateBattleScreen("BACK", playerTurn)
                        previousScreenState = "Move Menu"
                        screenState = "Battle"

                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "BACK")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        updateDialogue = True

                    elif screen.confirmOptionButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING CONFIRM", playerTurn)
                        previousScreenState = "Move Menu"

                        screen.aquireMoveName(current.buttonName())
                        playerOneDisplayed, playerTwoDisplayed = screen.getDisplayedPakuri()
                        battle.moveSelected(current.buttonName(), playerTurn, playerOneDisplayed, playerTwoDisplayed)

                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "CONFIRM")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        print(text[0])
                        updateDialogue = True

                        screen.updateBattleScreen("CONFIRM", playerTurn)
                        print(screen.speechPrint())
                        screenState = "Battle"
                        previous = None
                        current = None
                        playerTurn += 1

            elif screenState == "Pakuri Battle Menu":
                if updateDialogue == False:
                    pakuriPartyList = screen.getPakuriDisplayedTeam(playerTurn)
                    print(pakuriPartyList)
                    for i in range(4):
                        if pakuriPartyList[i].is_clicked(pygame.mouse.get_pos()):
                            font = pakuriPartyList[i].get_font()

                            print(pakuriPartyList[i].buttonName())
                            screen.selectedButton(pakuriPartyList[i], font)
                            current = pakuriPartyList[i]
                            position = i
                            break

                    if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING BACK!!!")
                        screen.updateBattleScreen("BACK", playerTurn)
                        screenState = "Battle"
                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "BACK")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        updateDialogue = True

                    elif screen.switchButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING SWITCH")
                        screen.updateBattleScreen("SWITCH", playerTurn, current.buttonName())
                        previous = None
                        current = None
                        previousScreenState = "Pakuri Battle Menu"
                        screenState = "Battle"
                        playerTurn += 1

            elif screenState == "Forfeit Menu":
                if updateDialogue == False:
                    if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING BACK!!!")
                        screen.updateBattleScreen("BACK", playerTurn)
                        screenState = "Battle"

                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "BACK")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        updateDialogue = True

                    elif screen.sureButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING FORFEIT")
                        screen.updateBattleScreen("SURE?", playerTurn, "FORFEIT")
                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "Forfeit")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        updateDialogue = True

            elif screenState == "Exit Menu":
                if updateDialogue == False:
                    if screen.backButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING BACK!!!")
                        screen.updateBattleScreen("BACK", playerTurn)
                        screenState = "Battle"
                        (text, text2Rect, font) = screen.getUpdatedDialogue(playerTurn, "BACK")
                        dialogue = str(playerTurn)
                        displayedDialogue = text[activeDialogue]
                        updateDialogue = True

                    elif screen.sureButton.is_clicked(pygame.mouse.get_pos()):
                        print("IM PRESSING SURE")
                        run = False




    pygame.display.update()

pygame.mixer.music.stop()
pygame.mixer.quit()
pygame.quit()