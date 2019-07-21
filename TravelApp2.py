import pickle
'''
travel app; 'Transport','Lodging','Event','Meal','Merchandise','Fee'
use classes to sort and organize and call data as needed

#possible future feature: organizes on calendar, shows what has not been booked for dates, ex. no hotel wednesday night

enter ahead of time:
flight:price, datetime,airline, airports, conf# seat#?
housing: price, dates, location, conf#
transport: price, dates, company, pickup/dropoff, conf#
entertainment: event, price, datetime, conf#, location

track as u go:
food: price, datetime
merch: item, location, price
Fee:
'''
# charge_options = ['Transport','Lodging','Event','Meal','Merchandise','Fee']


class ReservedCost():
    #type: transport,lodging,event; sub_type:[flight,train,boat],[hotel,bnb,camping]
    def __init__(
    self,type='', price='Unknown', pay_method='', pointa='',
        start_date='', start_time='', pointb='', end_date='',
        end_time='', sub_type='', conf='', company='', misc=None
    ):
        self.type=type
        self.price=price
        self.pay_method=pay_method
        self.pointa=pointa
        self.start_date=start_date
        self.start_time = start_time
        self.pointb = pointb
        self.end_date = end_date
        self.end_time = end_time
        self.sub_type = sub_type
        self.conf = conf
        self.company = company
        self.misc=misc


    def edit_cost(self):
        ## CLI for EditCostPage
        edit_lst=[] #should maybe be using a dictionary here? for printing and item assignment instead of list?
        for i in [(self.type,'type'),(self.sub_type,'sub_type'),(self.price,'price'),(self.pay_method,'payment method'),(self.pointa,'pointa'),(self.start_date,'start date mm/dd/yy'),(self.start_time,'start time'),(self.pointb,'pointb'),(self.end_date,'end date mm/dd/yy'),(self.end_time,'end_time'),(self.conf,'conf'),(self.company,'company'),(self.misc,'misc')]:
            print("{}={}\ttype new info or 'enter' to skip".format(i[1],i[0]))
            edited_ans=input()
            if edited_ans =='':
                edit_lst.append(i[0])
            else:
                edit_lst.append(edited_ans)

        if len(edit_lst) ==13:
            self.type=edit_lst[0]
            self.sub_type =edit_lst[1]
            self.price=edit_lst[2]
            self.pay_method=edit_lst[3]
            self.pointa=edit_lst[4]
            self.start_date=edit_lst[5]
            self.start_time = edit_lst[6]
            self.pointb = edit_lst[7]
            self.end_date = edit_lst[8]
            self.end_time = edit_lst[9]
            self.conf = edit_lst[10]
            self.company = edit_lst[11]
            self.misc=edit_lst[12]
            print("All updated")
        else:
            print("error, could not update")


    def __str__(self):
        #CLI frame for EditCostPage
        return(("type= {}\nprice=${}\npay_method={}\npointa={}\nstart_date={}\nstart_time= {}\npointb= {}\nend_date= {}\nend_time= {}\nsub_type= {}\nconf= {}\ncompany= {}\nmisc= {}").format(self.type,\
            self.price, self.pay_method, self.pointa, self.start_date,\
            self.start_time, self.pointb, self.end_date,self.end_time,\
            self.sub_type, self.conf, self.company, self.misc))




class UnreservedCost():
    #type=[food,merch,fee]
    def __init__(self, type='', price='Unknown', item='', pay_method='',
        date='', loc='', misc=None
    ):
    #migth be able to change preassignment to '' and remove the whole kwargs thing
    #and edit variables only thru the edit_cost()
        self.type = type
        self.price = price
        self.item = item
        self.pay_method = pay_method
        self.date = date
        self.loc = loc
        self.misc = misc

    def edit_cost(self):
        ## CLI for EditCostPage
        edit_lst=[]
        for i in [(self.type,'type'),(self.item,'item'),(self.price,'price'),(self.pay_method,'pay_method'),(self.date,'date mm/dd/yy'),(self.loc,'loc'),(self.misc,'misc')]:
            print("{}={}\ttype new info or 'enter' to skip".format(i[1],i[0]))
            edited_ans=input()
            if edited_ans =='':
                edit_lst.append(i[0])
            else:
                edit_lst.append(edited_ans)

        if len(edit_lst) ==7:
            i=edit_lst
            self.type = i[0]
            self.item = i[1]
            self.price = i[2]
            self.pay_method = i[3]
            self.date = i[4]
            self.loc = i[5]
            self.misc = i[6]
            print("All updated")
        else:
            print("error, could not update")


    def __str__(self):
        ## CLI frame for EditCostPage
        return ("type= {}\nprice= ${}\nitem= {}\npay_method= {}\ndate= \
            {}\nloc = {}\nmisc = {}".format(self.type,self.price,self.item,
            self.pay_method,self.date,self.loc,self.misc
            ))


class Trip():
    def __init__(self,destination='', approx_date='None',budget='None'):
        self.trip_plans = []
        self.destination = destination
        self.approx_date = approx_date
        self.budget = budget

    def print_details(self):
        ## CLI print format for TripListPage, EditTripPage,TripDetailsPage
        date=''
        for i in self.approx_date:
            date += (i+' ')
        return self.destination + ' - '+ date # +"budget: "+str(self.budget)

    def update_trip_title(self):
        ## CLI frame for EditTripPage
        edit_lst=[]
        for i in [(self.destination,'Trip Destination'),(self.approx_date,'Approximate Date'),(self.budget,'Budget')]:
            print("{} = {}".format(i[1],i[0]))
            while True:

                edited_ans=input("type new info or 'enter' to skip ")
                if edited_ans =='' and i[0]!='':#only if prenamed and not changing
                    edit_lst.append(i[0])
                    break
                elif edited_ans!='': #only runs if an answer is typed
                    if i[1]=='Trip Destination': #verifies correct name for trip
                        appr_name=input("Is this correct? "+edited_ans+" ")
                        if appr_name.lower()[0]=='y':
                            edit_lst.append(edited_ans)
                            break
                    elif i[1]=='Approximate Date':
                        print("date running")
                        approx_date=edited_ans.split('/') #split into [month,yy] for later manipulation
                        if len(approx_date)==2:
                            print("date length qualified")
                            edit_lst.append(approx_date)
                            break
                        else:
                            print("date must be in 'month/yy' format or 'None'")
                            continue
                    elif i[1]=='Budget':
                        try: #must be number for later maths
                            edited_ans=int(edited_ans)
                            edit_lst.append(edited_ans)
                            break
                        except:
                            print("Budget must be integer")
                            continue

        if len(edit_lst) ==3:
            self.destination = edit_lst[0]
            self.approx_date = edit_lst[1]
            self.budget = edit_lst[2]
            print("All updated")
        else:
            print("error, could not update")

    def trip_total_price(self):
        #loops to grab price int and add them together
        trip_total = 0
        costs=0
        for cost in self.trip_plans:
            try:
                trip_total+=int(cost.price)
                costs+=1
            except ValueError:
                continue
        print("\nrunning trip total is.. $"+str(trip_total))
        return trip_total

    def within_budget_check(self):
        print(self.budget)
        print(type(self.budget))
        if type(self.budget) == int:
            t= self.trip_total_price()
            if self.budget > t:
                r=self.budget-t
                print("You have ${} remaining".format(r))
            else:
                r=t-self.budget
                print("You are ${} over budget".format(r))
        else:
            print("can't print budget")
    #####set up travel plans thru the appropriate classes here####
    def add_reserved_cost(self,**kwargs):
        x = ReservedCost(**kwargs)
        x.edit_cost()
        self.trip_plans.append(x)

    def add_unreserved_cost(self,**kwargs):
        x = UnreservedCost(**kwargs)
        x.edit_cost()
        self.trip_plans.append(x)

    def add_cost(self):
        while True:
            #button in TripDetailsPage triggers popup that asks charge type,
            #then directs to EditCostPage with variable loading correct type
            print("What type of charge is it?\nTransport, Lodging, Event\nMeal, Merchandise, Fee")
            charge_options = ['transport','lodging','event','meal','merchandise','fee','t','l','e','f','q']
            charge_type_full = input()
            if len(charge_type_full)!=0:
                charge_type=charge_type_full.lower()[0]
                if charge_type_full.lower() in charge_options or charge_type in charge_options:
                    break
        if charge_type=='t':
            self.add_reserved_cost(type='Transportation')
        elif charge_type=='l':
            self.add_reserved_cost(type='Lodging')
        elif charge_type=='e':
            self.add_reserved_cost(type='Event')
        elif charge_type_full.lower()=='meal':
            self.add_unreserved_cost(type='Meal')
        elif charge_type_full.lower()[:4]=='merch':
            self.add_unreserved_cost(type='Merchandise')
        elif charge_type=='f':
            self.add_unreserved_cost(type='Fee')
        else:
            return None # for 'quit'

    def remove_cost(self, index_place):
        ## button on EditCostPage, triggers pop up to confirm, redirects to TripDetailsPage
        confirm = input("are you sure you want to delete this cost:\n{}\n[Y/n]".format(self.trip_plans[index_place]))
        if confirm == 'Y':
            self.trip_plans.pop(index_place)
            print("trip cost has been deleted")
        else:
            print("action cancelled\n")

'''
####start program and read pre existing data
to open saved file or create a new one
'''

def sort_trips_descending(trip_list):
    months=['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
    trips_no_date=[]#add to end of sorted list
    trips_with_dates=[] #collect obj to sort
    for trip in trip_list:
        if type(trip.approx_date)==list:
            trips_with_dates.append(trip)
        else:
            trips_no_date.append(trip)
    trip_list=sorted(trips_with_dates, key=lambda v: ( v.approx_date[1],months.index(v.approx_date[0])))
    trip_list.extend(trips_no_date)
    print("sorted success")
    return(trip_list)


def load_trip_files(filename):
    with open(filename, 'rb') as f:
        vacations = pickle.load(f)
        return vacations


def vacay_trips_display(vacations): #prints vacations in a numbered list
    ## CLI frame for TripListPage
    for num,trip in enumerate(vacations):
        print(str(num),end='. ',flush=True)
        print(trip)
    print("--end of Vacations list--\n") #test line/ delete later

def new_or_edit(filename):
    ##CLI for new or edit trip choices, will be buttons;
    # get rid of TRY, generate blank page, grey out 'edit' button
    #maybe split into more try functions so failure further down doesnt break out of the whole 'try'.
    try:
        vacations = load_trip_files(filename)
        vacations=sort_trips_descending(vacations)####
        vacay_trips_display(vacations)
        print("Would you like to create a new trip plan or edit an existing trip plan?")
        [print("end of options")]
        choice = input("enter 'new' or 'edit' ")
        choice=choice.lower()
        return choice,vacations

    except (FileNotFoundError):
        print("No pre-existing trip plans file found")
        create_new=input("\nwould you like to create a new one? ")
        if create_new=='quit':
            return (create_new,None)
        else:
            return ('new',None)
    # except: #,TypeError
    #     print('Program Error, Contact Administrator')
        #doesnt keep program running, it still breaks



def create_new_trip():
    trip=Trip()
    trip.update_trip_title()
    return trip

def create_edit_trip(choice,vacations):
    ##CLI frame TripListPage, create edit buttons next to each trip summary
    vacay_trips_display(vacations)
    print('which trip would you like to open? ')

    while True:
        trip_num=input('please enter the number') #using number choices to grab vs typed names
        try:
            trip_num=int(trip_num)
            if trip_num < len(vacations):
                break
        except:
            if trip_num =='quit':
                print("Quiting")
                return (None,None)
                # break

    trip=vacations[trip_num]
    print('\n')
    print(trip)
    def trip_plans_display(trip): #prints a numbered list of trip plans
    #CLI TripDetailsPage func
        for num,cost in enumerate(trip.trip_plans):
            print(str(num)+': '+cost.type)
        print("end of scheduled plans\n")

    trip_plans_display(trip) #summary to help make descision
    while True:
        #CLI TripDetailsPage, buttons: edit>>EditCostPage; add>>popup>>EditCostPage; rename/budget>>EditTripPage; done>>TripListPage
        #delete cost should be on edit cost page buttons, deletetrip on EditTripPage
        edit_trip=input("Details: view, add, edit, total, delete cost, renametrip, budget, delete trip, quit/done")
        if edit_trip=='':
            continue #looping if pressing enter
        elif edit_trip=='budget':
            trip.within_budget_check()
        elif edit_trip=='add':
            print("add chosen")
            trip.add_cost()
            print(trip.trip_plans[-1]) #prints most recently added detail

        elif edit_trip=='total':
            trip.trip_total_price()

        elif edit_trip=='renametrip':
            trip.update_trip_title()
            print(trip)

        elif edit_trip=='quit' or edit_trip=='done':
            print("Quit chosen, loop breaking")
            break

        elif edit_trip == 'delete trip':
                print(trip)
                trip_plans_display(trip)
                confirm=input("are you sure you want to delete this entire trip? [Y/n]")
                if confirm=='Y':
                    vacations.pop(trip_num)
                    print("trip removed from vacation database")
                    return (vacations,None)
                else:
                    print("action cancelled")

        else:
            trip_plans_display(trip)
            print('which cost would you like to {}? '.format(edit_trip))

            while True:
                cost_num=input('please enter the number') #using number choices to grab vs typed names
                try:
                    cost_num=int(cost_num)
                    if int(cost_num) < len(trip.trip_plans):
                        break
                except:
                    if cost_num =='quit' or cost_num=='done':
                        print("quit chosen")
                        edit_trip='quit' #need edit_trip assigned to something or it breaks further down
                        break
            if edit_trip=='quit':
                break
            elif edit_trip=='edit':
                print("\nedit chosen")
                trip.trip_plans[int(cost_num)].edit_cost()
                print(trip.trip_plans[int(cost_num)])
            elif edit_trip =='view':
                print(trip.trip_plans[int(cost_num)])

            elif edit_trip=="delete cost":
                trip.remove_cost(int(cost_num))

    print('Full trip details:')
    for t in trip.trip_plans: #print full details after
        print(t)
    print("end of full trip costs\n")

    return (trip,trip_num)


def create_vacaylist_for_save(vacations,trip,choice,trip_num=None):
###### this is for saving trip
    if vacations == None:
        print("creating new triplist")
        trip_list=[trip,]

    elif choice == 'edit':
        #should have prior writen logic to index trip to be edited, use same here
        print("indexing to overwrite trip")
        vacations[trip_num]=trip
        trip_list=vacations

    elif choice == 'new':
        try: #if list has any Nonetype objects remove them
            print("adds new trip to end of trip list")
            trip_list=vacations
            trip_list.append(trip)
            for i in trip_list:
                if i == None:
                    trip_list.pop(trip_list.index(i))
        except AttributeError: #if vacations is only one item, convert to list
            print("adds new trip and creates triplist")
            trip_list=[vacations,]
            trip_list.append(trip)

    elif choice == 'quit' or choice == 'done':
        return None

    else:
        print('Failure adding item to vacations list\n')
        return None #to avoid breaking if this clause runs

    # vacay_trips_display(trip_list)
    return trip_list  #Comment out when testing to avoid saving changes


def save_trip_list(trip_list, filename):
    '''
    to save trip obj data to be accessed at opening of program
    combine obj's into a list to be uploaded to file
    #I want all trips to be in one file, read/edited/saved to
    '''
    if trip_list == None:
        print("No Data to save\nCancelling operation.")
    else:
        try:
            with open(filename, 'wb') as output:  # Overwrites any existing file.
                pickle.dump(trip_list, output, -1)
                print('trip list officially saved')
        except UnboundLocalError:
            print('Cannot Save Trip, Error')
        except:
            print('other error')

############################# tkinter stuff ###################################
from tkinter import *

def main():
    class TravelApp(Tk):
            def __init__(self, *args, **kwargs):
                Tk.__init__(self, *args, **kwargs)

                container = Frame(self)
                container.pack(side="top", fill="both", expand = True)
                container.grid_rowconfigure(0, weight=1)
                container.grid_columnconfigure(0, weight=1)


                self.frames = {}
                for F in (TripListPage, EditTripPage,TripDetailsPage, EditCostPage):
                    frame = F(container, self)
                    self.frames[F] = frame
                    frame.grid(row=0, column=0, sticky="nsew")

                self.show_frame(TripListPage,vacations[0])

            def show_frame(self, cont, locatorID=None):
                frame = self.frames[cont]
                print("UNDER SHOW FRAME:")
                print(locatorID)
                frame.assign_locator(locatorID)
                frame.tkraise()

    class TripListPage(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self,parent)

            try:
                for trip in vacations:
                    label = Label(self, text=trip.print_details())
                    label.pack(pady=10,padx=10)
                    button2 = Button(self, text="EDIT existing trip",
                            command=lambda: controller.show_frame(EditTripPage,locatorID=trip))
                    button2.pack()
                    #TODO: edit button should redirect to specific TripDetailsPage
            except TypeError:
                #currently displays blank page with ADD button active
                pass

            button = Button(self, text="ADD a new trip",
                                command=lambda: controller.show_frame(EditTripPage,vacations[0]))
            button.pack()

        def assign_locator(self,locatorID):
            self.locatorID=locatorID
            print("inside Main page:") ###why arent these triggering?!!!
            print(locatorID)
            print(self.locatorID)

    class EditTripPage(Frame):
            def __init__(self, parent, controller,locatorID=None):
                self.locatorID=locatorID
                Frame.__init__(self, parent)

                # label = Label(self, text="Create or Edit Trip Details Here")
                # label.pack(pady=10,padx=10)
                #
                # label = Label(self, text=locatorID.print_details())
                # label.pack(pady=10,padx=10)
                if locatorID != None:
                    label = Label(self, text=locatorID.print_details())
                    label.pack(pady=10,padx=10)

                button1 = Button(self, text="Back to Home(DELETE)",  #pop up to confirm then redirects page
                                    command=lambda: controller.show_frame(TripListPage))
                button1.pack()

            def assign_locator(self,locatorID):
                self.locatorID=locatorID
                print("inside Edit trip page:") ###why arent these triggering?!!!
                print(locatorID)
                print(self.locatorID)

                # button2 = Button(self, text="Continue to details page (SAVE)",
                #                     command=lambda: controller.show_frame(TripDetailsPage))
                # button2.pack()

    class TripDetailsPage(Frame):

            def __init__(self, parent, controller,locatorID=None):
                Frame.__init__(self, parent)
                label = Label(self, text="View list of trip costs here")
                label.pack(pady=10,padx=10)

                button1 = Button(self, text="(DONE) Back to Home",
                                    command=lambda: controller.show_frame(TripListPage))
                button1.pack()

                button2 = Button(self, text="EDIT trip details",
                                    command=lambda: controller.show_frame(EditTripPage))
                button2.pack()

                button3 = Button(self, text="ADD new cost",  #pop up asks what kind of cost
                                    command=lambda: controller.show_frame(EditCostPage))
                button3.pack()

                button4 = Button(self, text="EDIT existing cost",
                                    command=lambda: controller.show_frame(EditCostPage))
                button4.pack()

    class EditCostPage(Frame):

            def __init__(self, parent, controller,locatorID=None):
                Frame.__init__(self, parent)
                label = Label(self, text="Edit costs or create new one here")
                label.pack(pady=10,padx=10)

                button1 = Button(self, text="CANCEL, Back to trip details", ##pop up confirmation then redirects page
                                    command=lambda: controller.show_frame(TripDetailsPage))
                button1.pack()

                button2 = Button(self, text="SAVE, Back to trip details",
                                    command=lambda: controller.show_frame(TripDetailsPage))
                button2.pack()


    filename="pckl_test_file.pkl"
    choice, vacations=new_or_edit(filename)
    root = TravelApp()
    root.geometry('700x400')
    root.mainloop()

if __name__ == '__main__':
    main()
##############################################################################

#left off at line 532,
#trying to figure out how to pass objects between frames,
# to choose what data is displayed i need access to which obj the user clicked,
# currently obj is being recognized at show_frame call but is not being transfered to frame location?
#i feel like i have locatorID in unessesary locations but keep getting errors if i take it out,

#TODO: get obj to read in new frame from button passed in previous frame.,
