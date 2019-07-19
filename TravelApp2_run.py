import pickle
from TravelApp2 import ReservedCost,UnreservedCost,Trip,new_or_edit,save_trip_list,create_new_trip,create_vacaylist_for_save,create_edit_trip
filename="pckl_test_file.pkl"

while True:
    #use while loop to keep active till quiting program
    choice,vacations=new_or_edit(filename)
    print("you chose to: "+choice)

    #need to check weather new or edit func
    if choice.lower() == 'new':
        trip= create_new_trip()
        print("new trip created")
        trip_list=create_vacaylist_for_save(vacations,trip,choice)
        print("new trip list created")
        print("saving trip....")
        save_trip_list(trip_list,filename)

    elif choice.lower() == 'edit':
        print("\nnow edit function")
        trip,trip_num=create_edit_trip(choice,vacations)
        if trip != None and trip_num!=None:
            print("Trip created")
            trip_list=create_vacaylist_for_save(vacations,trip,choice,trip_num)
            print("new trip list created")

        elif trip != None and trip_num==None: #to save deletes
            print("saving vacations minus deletes")
            trip_list=trip
        else:
            #not really neded if save is only used after changes and not every time its run
            print("just saving pre-existing trip list")
            trip_list=vacations
        print("saving trip....")
        save_trip_list(trip_list,filename)
    elif choice.lower() == 'quit':
        break
