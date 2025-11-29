# clubs information
from pyscript import display
from pyscript import document

# 1. swimming club
swimming_club = {
    'description':'a club for swimming',
    'metting_time':'5:00-7:00m PM',
    'location':'pool',
    'number of member':'30'
} 

#2. baseball club
baseball_club = {
    'description':'a club for baseball',
    'metting_time':'3:00-:800m PM',
    'location':'ground',
    'number of member':'40'
}

#3.computer club
computer_club = {
    'description':'a club for computering',
    'metting_time':'4:00-6:00m PM',
    'location':'room 123',
    'number of member':'25'
}

# display club information
def displayClubInfo(event):
    clubValue = document.getElementById("clubs").value
    if clubValue == "swimming_club":
        display(swimming_club, target="output")
    elif clubValue == "baseball_club":
        display(baseball_club)
    elif clubValue == "computer_club":
        display(computer_club)
