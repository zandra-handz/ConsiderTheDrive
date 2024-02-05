#terminal printing menu for Distance class :)
from DistanceClass import Distance 
from DistanceClass import validate_address


api_key = 'GOOGLE_MAPS_API_KEY'


def menu_create_distance_object():

    address_a = ""
    address_b = ""
    address_c = ""

    while address_a == "":
        address_a = input("Enter your starting point (street, city, state, zip): ")

        if not validate_address(api_key, address_a):
            print("Address not found.")
            address_a = ""

    while address_b == "":
        address = input("Enter friend's starting point (street, city, state, zip): ")

        if not validate_address(api_key, address):
            print("Address not found.")
            address_b = ""

        else:
            friend_name = input("Enter friend's name: ")
            address_b = {friend_name: address}

    while address_c == "":
        address_c = input("Enter meet up location (street, city, state, zip): ")

        if not validate_address(api_key, address_c):
            print("Address not found.")
            address_c =""

    return Distance(api_key, origin_a = address_a, destination = address_c, **address_b)


def menu_add_additional_friend(distance_object):

    validated = False

    while not validated:
        address = input("Enter friend's starting point (street, city, state, zip): ")

        if address == "exit":
            return False

        if not validate_address(api_key, address):
            print("Address not found.")

        else:
            friend = input("Enter friend's name: ")
            distance_object.add_friend_address(friend, address)
            validated = True

    return True


def menu_print_results(distance_object):

    distance_and_duration_data = distance_object.compare_directions(many=True)
    print(f"Destination: {distance_object.destination}")

    for idx, (friend, data) in enumerate(distance_and_duration_data.items()):
      print(f"{idx + 1}: {friend} - {data['duration']} ({data['distance']})")


def print_suggested_places(data, keyword):

    if data:
        print(f"\nSuggested for {keyword}:")

        for idx, place in enumerate(data):
            print(f"{idx + 1}. {place['name']} - {place['address']} ")

            for distance_data, duration_data in zip(place['distances'], place['travel_times']):
                friend_distance = distance_data.popitem()
                friend_duration = duration_data.popitem()
                friend = friend_distance[0]
                distance = friend_distance[1]
                duration = friend_duration[1]

                print(f"{friend}: {duration} ({distance:.2f} miles)", end=" | ")

            print(" ")

    else:
        print(f"No data available for {keyword}")


def print_all_friends(data):
      
      if data:
        print(f"\nFriends attending meet-up:")

        for idx, info in data.items():
            print(f"{idx + 1}. {info['friend']} - {info['address']} ")


def welcome_message():

  print("Welcome to Consider The Drive! This is the terminal menu implementation. :)")
  print("You will need two valid starting addresses and one valid destination address to use this program.")
  input("Press enter to continue!")


def main():

    try:
        welcome_message()
        distance_considerer = menu_create_distance_object()
        finished_adding_friends = False

        while not finished_adding_friends:
            answer = input("Add another friend to this meet-up? (y for yes, any other key for no) ")

            if answer == "y":
                print_all_friends(distance_considerer.get_all_friend_info())
                result = menu_add_additional_friend(distance_considerer)

                if result == True:
                    print("Success!")

                else:
                    print("No friend added.")

            else:
                finished_adding_friends = True

        menu_print_results(distance_considerer)
        finished_searching_for_suggesteds = False

        while not finished_searching_for_suggesteds:
            answer = input("Browse suggested places? (y for yes, any other key for no): ")

            if answer == "y":
                second_answer = input("Change default radius (5000) and default list length (8)? (y for yes, any other key for no): ")

                if second_answer == "y":
                    distance_considerer.change_radius(input("Enter radius: "))
                    distance_considerer.change_suggested_length(input("Enter list length: "))

                distance_considerer.change_keyword(input("Enter keyword: "))

                if len(distance_considerer.friend_origins) > 1:
                    distance_considerer.get_midpoint_for_multiple()

                else:
                    distance_considerer.get_midpoint()

                suggested_list_data = distance_considerer.get_directions_to_midpoint_places(many=True)
                print_suggested_places(suggested_list_data, distance_considerer.search)

            else:
                finished_searching_for_suggesteds = True

        input("Press any key to end!" )

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()