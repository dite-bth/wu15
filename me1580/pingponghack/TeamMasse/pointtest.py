from gpiozero import Button
import json
import simplejson as json

redset = 0
blueset = 0
restart = False
win = "none"
winner = False
redpoints = 0
bluepoints = 0
Buttonred = Button(19)
Buttonblue = Button(21)









def pointred():
    global redpoints
    global winner
    global restart
    global bluepoints
    global win
    global redset
    global blueset
    
    redpoints = redpoints + 1
    
    if (redpoints >= 11) and (redpoints - bluepoints >= 2) and (winner == False):
        if (redset < 1):
            redset += 1
            print("Red has won a set!")
            info = [{'Redpoints': redpoints,
                    'Bluepoints' : bluepoints,
                    'Winner' : "red",
                    'Redset' : redset,
                    'Blueset' : blueset
                    }]
            with open('info.txt', 'w') as outfile:
                json.dump(info,outfile)
            bluepoints = 0
            redpoints = 0
            print("New set!")
            
        else :
            print("You have won the match, player red!")
            redset = 2
            info = [{'Redpoints': redpoints,
                    'Bluepoints' : bluepoints,
                    'Winner' : "red",
                    'Redset' : redset,
                    'Blueset' : blueset
                    }]
            with open('info.txt', 'w') as outfile:
                json.dump(info,outfile)

            winner = True

    elif (winner == True) and (restart == False):
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
                'Bluepoints' : bluepoints
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

    bluepoints = bluepoints + 1
    
    if (bluepoints >= 11) and (bluepoints - redpoints >= 2) and (winner == False):
        if (blueset < 1):
                blueset += 1
                print("Blue has won a set!")
                info = [{'Redpoints': redpoints,
                        'Bluepoints' : bluepoints,
                        'Winner' : "red",
                        'Redset' : redset,
                        'Blueset' : blueset
                        }]
                with open('info.txt', 'w') as outfile:
                    json.dump(info,outfile)
                bluepoints = 0
                redpoints = 0
                print("New set!")

        else:
            print("You have won the match, player blue!")
            blueset = 2
            info = [{'Redpoints': redpoints,
                    'Bluepoints' : bluepoints,
                    'Winner' : "blue",
                    'Redset' : redset,
                    'Blueset' : blueset
                    }]
            with open('info.txt', 'w') as outfile:
                json.dump(info,outfile)

            winner = True

    elif (winner == True) and (restart == False):
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
                'Bluepoints' : bluepoints
                }]
        with open('info.txt', 'w') as outfile:
            json.dump(info,outfile)


Buttonred.when_pressed = pointred 
Buttonblue.when_pressed = pointblue
