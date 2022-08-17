destinations = ['Museum Mile', 'Restaurant Row','Chinatown', 'Times Square', 'Central Park']
restaurants = ["Junior's", "Jolibee's", "iTruli", "Bubba Gump", "Woorijip"]
transportation = ['bus', 'bike', 'call Uber', 'e-scooter', 'subway train']
entertainment = ['tickets to the theater', 'drinks at an adult lounge', 'show at a comedy club', 'taping at a live show', 'tickets for a baseball game']
import random

# initial destination
def where_to_first(destinations):
    first_random_destination = random.choice(destinations)
    return first_random_destination
initial_destination = where_to_first(destinations)  # calls function
print(f'{initial_destination}')


# initial restaurant
def where_to_first(restaurants):
    first_random_restaurant = random.choice(restaurants)
    return first_random_restaurant
initial_restaurant = where_to_first(restaurants)
print(f'{initial_restaurant}')

# initial transportation
def where_to_first(transportation):
    first_random_transportation = random.choice(transportation)
    return first_random_transportation
initial_transportation = where_to_first(transportation)
print(f'{initial_transportation}')

# initial entertainment
def where_to_first(entertainment):
    first_random_entertainment = random.choice(entertainment)
    return first_random_entertainment
initial_entertainment = where_to_first(entertainment) 
print(f'{initial_entertainment}')
print(f'Our recommended NYC destination is {initial_destination}. You may eat at {initial_restaurant}, commute via {initial_transportation}, and enjoy {initial_entertainment}.')

# #remove one from the list



#remove rejected selection
def remove_rejected_destination(destinations):
    itinerary = [{initial_destination}, {initial_restaurant},{initial_transportation}, {initial_entertainment}]
    revised_destination=itinerary.remove({initial_destination})
# if initial_destination in destinations:
#     destinations=destinations.remove(initial_destination)
# print(f'{initial_destination} is no longer available.')
print(f'Your remaining options are {remove_rejected_destination}')
#revisit this!!!

# #cycle through categories
# def change_plans(itinerary):
#     for which_change in itinerary:
#         print('Which of your choices would you like to change? {which_change}')
#         change_itinerary=input('Please enter: ')
#         if change_itinerary == initial_destination:
#             result
#             destinations= destinations.remove({initial_destination})
#         # print(destinations)
#         new_itinerary=input('Which is your new destination? ')
        
    
# change_plans(itinerary)
# print(destinations)


def remove_destinations(destinations):
    removed_destination = destinations.remove({initial_destination})
remove_destinations(destinations)
    
# # if satisfied with destination, yes then print results, no then else ask
def user_destination_response(destinations):
    great_destination=input('Are you satisfied with your destination? (y/n)? ')
    if great_destination=='y':
        print('Enjoy your visit.')
    else:
        next_random_destination=random.choice(destinations)
        change_destination = input(f'Would you rather visit? '(y/n))
        if change_destination!='y':
            initial_destination.append

user_destination_response(destinations)
        
#     change_restaurant= input('Would you like to eat at {initial_restaurant}? (y/n)')
#     change_transportation= input('Would you like to commute via {initial_transportation}? (y/n)')
#     change_entertainment= input('Would you enjoy {initial_entertainment} ? (y/n)')
    

# # which feature?
# # if destination, yes then append destination, no then else ask
# if restaurant, yes then append restaurant, no then else ask
# if transportation, yes then append transportation, no then else ask
# if entertainment, yes then append entertainment, no then
# print results
# if satisfied with the results(loop up)
# complete the day trip

