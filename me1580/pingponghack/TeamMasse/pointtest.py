from gpiozero import Button
import json
import simplejson as json
import pygame
import time



redset = 0
blueset = 0
restart = False
win = "none"
winner = False
redpoints = 0
bluepoints = 0
Buttonred = Button(19)
Buttonblue = Button(21)
player1 = ""
player2 = ""
matchrunning = False


def startmatch(name1, name2):
    global player1, player2, matchrunning
    player1 = name1
    player2 = name2
    matchrunning = True




def pointred():
    global redpoints
    global winner
    global restart
    global bluepoints
    global win
    global redset
    global blueset


    if matchrunning == False:
        return

    redpoints = redpoints + 1
    
    if (redpoints >= 11) and (redpoints - bluepoints >= 2) and (winner == False):
        if (redset < 1):
            redset += 1
            bluepoints = 0
            redpoints = 0
            print("Red has won a set!")

            print("New set!")
            
        else :
            print("You have won the match, player red!")

            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("klappklapp.wav")
            sounda.play()
            pygame.mixer.quit()

            
            redset = 2
            
            info = [{'Redpoints': redpoints,
                 'Bluepoints' : bluepoints,
                 'Winner' : "red",
                 'Redset' : redset,
                 'Blueset' : blueset
                }]
            with open('info.txt', 'w') as outfile:
                json.dump(info,outfile)

            time.sleep (4)
            winner = True

    elif (winner == True) and (restart == False):
        redpoints -= 1
        print("Press a button again to restart.")

        restart = True

    elif (restart == True):
        redpoints = 0
        bluepoints = 0
        winner = False
        win = "none"
        restart = False
        redset = 0
        blueset = 0
    else:
        print("Player red has " + str(redpoints) + " points!")
        
    info = [{'Redpoints': redpoints,
             'Bluepoints' : bluepoints,
             'Winner' : "red",
             'Redset' : redset,
             'Blueset' : blueset,
             'redplayer' : player1,
             'blueplayer' : player2
            }]
    with open('info.txt', 'w') as outfile:
        json.dump(info,outfile)







            
            
def pointblue():
    global winner
    global restart
    global bluepoints
    global redpoints
    global win
    global redset
    global blueset


    if matchrunning == False:
        return

    bluepoints = bluepoints + 1
    
    if (bluepoints >= 11) and (bluepoints - redpoints >= 2) and (winner == False):
        if (blueset < 1):
                blueset += 1
                bluepoints = 0
                redpoints = 0
                print("Blue has won a set!")
                print("New set!")

        else:
            print("You have won the match, player blue!")

            pygame.init()
            pygame.mixer.init()
            sounda= pygame.mixer.Sound("klappklapp.wav")
            sounda.play()
            time.sleep (4)
            pygame.mixer.quit()
            
            blueset = 2
            
            winner = True

    elif (winner == True) and (restart == False):
        bluepoints -= 1
        print("Press a button again to restart.")

        restart = True

    elif (restart == True):
        redpoints = 0
        bluepoints = 0
        winner = False
        win = "none"
        restart = False
        redset = 0
        blueset = 0

    else:
        print("Player blue has " + str(bluepoints) + " points!")

    info = [{'Redpoints': redpoints,
             'Bluepoints' : bluepoints,
             'Winner' : "red",
             'Redset' : redset,
             'Blueset' : blueset,
             'redplayer' : player1,
             'blueplayer' : player2
            }]
    with open('info.txt', 'w') as outfile:
        json.dump(info,outfile)

        
Buttonred.when_pressed = pointred 
Buttonblue.when_pressed = pointblue


