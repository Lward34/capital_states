""" prompts user to get state capital, population, and flower """
import matplotlib.pyplot as plt
from PIL import Image


# define an empty list that will carry all the data
_capital_states={
    'Alabama': "Capital:Montgomery, population:4877680, flower:Camellia, AL.png",
    'Alaska': "Capital:Juneau, population:735139, flower:Forget-Me-Not, AK.png",
    'Arizona': "Capital:Phoenix, population:7158020, flower:Saguaro Cactus Blossom, AZ.png",
    'Arkansas': "Capital:Little Rock, population:3009730, flower:Apple Blossom",
    'California': "Capital:Sacramento, population:39461600, flower:Golden Poppy",
    'Colorado': "Capital:Denver, population:5691290, flower:Mountain Columbine",
    'Connecticut': "Capital:Hartford, population:3571520, flower:Mountain Laurel",
    'Delaware': "Capital:Dover, population:965479, flower:Peach Blossom",
    'Florida': "Capital:Tallahassee, population:21244300, flower:Orange Blossom",
    'Georgia': "Capital:Atlanta, population:10511100, flower:Cherokee Rose",
    'Hawaii': "Capital:Honolulu, population:1420590, flower:Yellow Hibiscus",
    'Idaho': "Capital:Boise, population:1750540, flower:Syringa",
    'Illinois': "Capital:Springfield, population:12723100, flower:Violet",
    'Indiana': "Capital:Indianapolis, population:6695500, flower:Peony",
    'Iowa': "Capital:Des Moines, population:3148620, flower:Wild Rose",
    'Kansas': "Capital:Topeka, population:2911360, flower:Sunflower",
    'Kentucky': "Capital:Frankfort, population:4461150, flower:Goldenrod",
    'Louisiana': "Capital:Baton Rouge, population:4659690, flower:Magnolia",
    'Maine': "Capital:Augusta, population:1339060, flower:Pine Cone & Tassel",
    'Maryland': "Capital:Annapolis, population:6035800, flower:Black-Eyed Susan",
    'Massachusetts': "Capital:Boston, population:6882640, flower:Mayflower",
    'Michigan': "Capital:Lansing, population:9984070 flower:Apple Blossom",
    'Minnesota': "Capital:St.Paul, population:5606250, flower:Lady Slipper",
    'Mississippi': "Capital:Jackson, population:2981020, flower:Magnolia",
    'Missouri': "Capital:Jefferson City, population:6121620, flower:Hawthorne",
    'Montana': "Capital:Helena, population:1060660, flower:Bitterroot",
    'Nebraska': "Capital:Lincoln, population:1925610, flower:Goldenrod",
    'Nevada': "Capital:Carson City, population:3027340, flower:Sagebrush",
    'New Hampshire': "Capital:Concord, population:1353460, flower:Purple Lilac",
    'New Jersey': "Capital:Trenton, population:8886020, flower:Violet",
    'New Mexico': "Capital:Santa Fe, population:2092740, flower:Yucca",
    'New York': "Capital:Albany, population:19530400, flower:Rose",
    'North Carolina': "Capital:Raleigh, population:10381600, flower:Flowering Dogwood",
    'North Dakota': "Capital:Bismarck, population:758080, flower:Prairie Rose",
    'Ohio': "Capital:Columbus, population:11676300, flower:Red Carnation",
    'Oklahoma': "Capital:Oklahoma City, population:3940240, flower:Oklahoma Rose",
    'Oregon': "Capital:Salem, population:4181890, flower:Oregon Grape",
    'Pennsylvania': "Capital:Harrisburg, population:12800900, flower:Mountain Laurel",
    'Rhode Island': "Capital:Providence, population:1058290, flower:Violet",
    'South Carolina': "Capital:Columbia, population:5084160, flower:Yellow Jessamine",
    'South Dakota': "Capital:Pierre, population:878698, flower:American Pasque flower",
    'Tennessee': "Capital:Nashville, population:6771630, flower:Iris",
    'Texas': "Capital:Austin,population:28628700,flower:Bluebonnet",
    'Utah': "Capital:Salt Lake City, population:3153550, flower:Sego Lily",
    'Vermont': "Capital:Montpelier, population:624358, flower:Red Clover",
    'Virginia': "Capital:Richmond, population:8501290, flower:Dogwood",
    'Washington': "Capital:Olympia, population:7523870, flower:Coast Rhododendron",
    'West Virginia': "Capital:Charleston, population:1804290, flower:Rhododendron",
    'Wisconsin': "Capital:Madison, population:5807410, flower:Wood Violet",
    'Wyoming': "Capital:Cheyenne, population:577601,flower:India Paintbrush",
}

def display_sorted_us(_capital_states):
    """Function Alphabetically display all U.S.States along with capital,
    state population, and flowers.
    Reference US States Rank: https://worldpopulationreview.com/states
    Args:None
    Returns:None
    """
    for y_list, x_list in sorted(_capital_states.items()):
        print(y_list, x_list)


def search_of_states(_capital_states, input_state):
    """displays the search state information"""
    found = False
    for states in _capital_states:
        # compare the parameter with every state
        if input_state == states.lower():
            # if found states, prints the Capital, population,and flower
            print(_capital_states[states])

            imgFileName =  ".\\images\\" + _capital_states[states][-6:];
            im = Image.open ( imgFileName )
            im.show ()

            found = True
            break
    if not found:
        print("State not found!")
    else:
        pass



def display_bar_graph():
    """Display a bar graph of the top five populated states showing their overall population
    Reference:Hunter, John, et al(2020) “Image Tutorial¶.” Image Tutorial,Matplotlib 3.3.3 Doc.
    matplotlib.org/tutorials/introductory/images.html#sphx-glr-tutorials-introductory-images-py.
    """
    # x,y values
    top = ['California', 'Florida', 'New York', 'Pennsylvania', 'Texas']
    values = [39747267, 21994600, 19491339, 12804100, 29087070]
    # function to plot and show graph
    plt.title('The top 5 populated States in U.S.')
    # Add title and custom
    plt.bar(top, values, color=['red', 'blue'], width=0.9)
    plt.plot([1, 2, 3, 4])
    plt.ylabel("Population")
    plt.legend()
    plt.show()


def update_population_state():
    """The function prompts user to enter state and population they want to update
    #Reference: http://easypythondocs.com/validation.html
    """
    while True:
        found = False
        state_update = input("Enter the state you want to update the population for: ")
        population = int(input('\nEnter State population: '))
        for _ in _capital_states:
            if _capital_states['state'] == state_update:
                state_update[int(population)] += population
                print("New update is:   " + _capital_states, state_update)
                found = True
                break
        if found:
            break
        else:
            print("Invalid input, please verify & Re-Enter input")
    print('You update state is: ' + state_update)

while True:
    print("\nWelcome to the U.S State Capital and Flower list Application")
    print("*********************************************")
    print('Select from the following menu')
    print('(1):Display all the U.S. states in Alphabetical order along')
    print('with the Capital,state Population, and Flower', )
    print('(2):Search for a specific state and display the appropriate')
    print('Capital name, State Population, and an image of the associate state Flower')
    print('(3):Provide a Bar graph of the top 5 populated States')
    print('showing their overall population.')
    print('(4):Updated the overall state population for a specific state')
    print('(5):Exit the program')
    option = input('Please choose one of the following options: ')


    # checks the response and manages the options
    if option == '1':
        display_sorted_us ( _capital_states )
    elif option == '2':
        input_state = input ( "Enter the state name: " ).lower ( )
        search_of_states ( _capital_states, input_state)
    elif option == '3':
        display_bar_graph ( )
    elif option == '4':
        update_population_state ( )
    elif option == '5':  # Exits the program
        print ( "Thank you for using the U.S.State capital and Flower list Program!" )
        break
    # Checks for valid user input
    else:
        print ( "That is not a correct entry, please select 1-5" )