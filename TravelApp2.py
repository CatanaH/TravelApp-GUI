import pickle
filename="pckl_test_file.pkl"
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
    def __init__(self,destination='',budget='None'):
        self.trip_plans = []
        self.destination = destination

        self.budget = budget

    def __str__(self):
        try:
            date=self.mon_date+' '+str(self.day_date)+'/'+str(self.year_date)
        except AttributeError:
            date='none'
        return self.destination + ': '+ date # +"budget: "+str(self.budget)

    def update_trip_title(self,tripname,mon_date,day_date,year_date, budget):
        months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','']
        self.destination = tripname
        try:
            mon_date=mon_date.capitalize()[:3]
            if mon_date in months:
                self.mon_date=mon_date
        except:
            self.mon_date=''
            ## TODO: add in error checking for mmm as str in list, and dd/yy as int
        try:
            if len(str(day_date)) <= 2:
                self.day_date=day_date
        except:
            self.day_date=''
        try:
            if len(str(year_date)) == 2:
                self.year_date=year_date
        except:
            self.year_date=''


        try: #must be number for later maths
            edited_ans=float(budget)
            self.budget = budget
        except:
            print("Budget must be a number")



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

def sort_trips_descending(trip_list): ## TODO: sort trips with new obj atrb. mon/dd/yy
    months=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec','']

    trips_no_date=[]#add to end of sorted list
    trips_with_dates=[] #collect obj to sort
    for trip in trip_list:
        try:
            x=(trip.mon_date,trip.day_date,trip.year_date) #maybe delete these later cause error check in trip obj should catch it
            if trip.mon_date not in months:
                trip.mon_date =''
            trips_with_dates.append(trip)
        except AttributeError:
            trips_no_date.append(trip)

    trip_list=sorted(trips_with_dates, key=lambda v: ( v.year_date,months.index(v.mon_date),v.day_date)) #months.index(v.mon_date)
    trip_list.extend(trips_no_date)
    print("sorted success")
    vacations=trip_list
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
    try:
        vacations = load_trip_files(filename)
        vacations=sort_trips_descending(vacations) ## TODO: need to fix sort feature for new date format
        return vacations
    except (FileNotFoundError):
        print("No pre-existing trip plans file found")
        return None
    # except: #,TypeError
    #     print('Program Error, Contact Administrator')


# def create_new_trip():
#     trip=Trip()
#     trip.update_trip_title()
#     return trip
def save_trip(locatorID,tripName,mon_date,day_date,year_date,budget,controller=None):
    try: #makes sure all data is proper then redirects; except catches errors and does popups
        if locatorID == None: #to create a new trip obj
            trip=Trip()
            trip.update_trip_title(tripName,mon_date,day_date,year_date,budget)
            locatorID=trip #provides new locator ID to work with
        else:
            locatorID.update_trip_title(tripName,mon_date,day_date,year_date,budget)
        # print(trip)
        print(vacations)
        create_vacaylist_for_save(vacations,locatorID)
        save_trip_list(vacations,filename)  #comment outwhile testing to prevent bad data saves
        return locatorID

    except TabError: #include specific errors and trigger popups (TabError for test, delete later)
        pass


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

        # elif edit_trip == 'delete trip':
        #         # print(trip)
        #         # trip_plans_display(trip)
        #         # confirm=input("are you sure you want to delete this entire trip? [Y/n]")
        #         if confirm=='Y':
        #             vacations.pop(vacations.index(locatorID))
        #             print("trip removed from vacation database")
        #             # return (vacations,None)
        #         else:
        #             print("action cancelled")

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


def create_vacaylist_for_save(vacations,locatorID,choice=None,trip_num=None):
###### this is for saving trip
    if vacations == None:
        print("creating new triplist")
        vacations=[trip,]
    elif locatorID in vacations:
        #dont need to rewirte list, obj already references whats been edited
        pass
    elif locatorID not in vacations:
        try:
            print("adds new trip to end of trip list")
            vacations.append(locatorID)
            # for i in vacations:   #if list has any Nonetype objects remove them
            #     if i == None:
            #         vacations.pop(vacations.index(i))
        except AttributeError: #if vacations is only one item, convert to list to prevent nested lists
            #only had this problem in the begining, prob dont need anymore
            print("adds new trip and creates triplist")
            vacations=[vacations,]
            vacations.append(locatorID)
    else:
        print('Failure adding item to vacations list\n')
        return None #to avoid breaking if this clause runs

    # return trip_list  ###vacations is global, shouldnt have to return to
    #save trip to put into save_trip_list. should be able to just call it


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

def delete_trip(triplist,locatorID):
    triplist.pop(triplist.index(locatorID))
    save_trip_list(triplist,filename)
############################# tkinter stuff ###################################
from tkinter import *


class DateEntry(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.mon_date = StringVar()
        self.day_date = StringVar()
        self.year_date = StringVar()
        limit_entry(self.mon_date,3)
        limit_entry(self.day_date,2)
        limit_entry(self.year_date,2)

        self.mon_date_entry = Entry(self,font=('arial',14),bd=2,insertwidth=2, width=3,textvariable=self.mon_date) #month
        self.date_slash_1 = Label(self, text='/')
        self.day_date_entry = Entry(self, font=('arial',14),bd=2,insertwidth=2,width=2,textvariable=self.day_date) #day
        self.date_slash_2 = Label(self, text='/')
        self.year_date_entry = Entry(self, font=('arial',14),bd=2,insertwidth=2,width=2,textvariable=self.year_date) #year

        self.mon_date_entry.pack(side=LEFT)
        self.date_slash_1.pack(side=LEFT)
        self.day_date_entry.pack(side=LEFT)
        self.date_slash_2.pack(side=LEFT)
        self.year_date_entry.pack(side=LEFT)


def limit_entry(str_var,length):
    def callback(str_var):
        c = str_var.get()[0:length]
        str_var.set(c)
    str_var.trace("w", lambda name, index, mode, str_var=str_var: callback(str_var))


def main():

    def popupmsg(controller,msg,vacations,locatorID):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Confirm Delete", command = lambda: [popup.destroy(),delete_trip(vacations,locatorID),controller.refresh_show_frame(TripListPage)]) #some reason this is throwing an error when the whole app is closed
        B1.pack()
        B2 = Button(popup, text="Cancel", command = popup.destroy)
        B2.pack()
        popup.mainloop()

    class TravelApp(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            self.container = Frame(self)
            self.container.pack(side="top", fill="both", expand = True)
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (TripListPage,EditTripPage,TripDetailsPage, EditCostPage): # EditTripPage,TripDetailsPage, EditCostPage
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(TripListPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            # print("UNDER SHOW FRAME:") #testing
            # print(locatorID) #testing
            frame.tkraise()

        def refresh_show_frame(self,cont,locatorID=None):
            # print("start refresh")
            self.refresh_frame(cont, locatorID)
            self.show_frame(cont)
            # print("END refresh_show_frame") #testing

        def refresh_frame(self,cont, locatorID=None):
            # print("start refresh") #testing
            frame = self.frames[cont]
            frame.destroy()

            frame = cont(self.container, self, locatorID)
            self.frames[cont] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            # print("REfresh done") #testing
            # print(locatorID) #testing

    class TripListPage(Frame):
        def __init__(self, parent, controller,locatorID=None):
            Frame.__init__(self,parent)

            button = Button(self, text="ADD a new trip",
                                command=lambda: controller.refresh_show_frame(EditTripPage)) #testing, no set to correct destination temp.
            button.grid(row=0,column=0)

            try:
                for n, trip in enumerate(sort_trips_descending(vacations)):
                    label = Label(self, text=trip.__str__())
                    label.grid(row=(n+1),column=0,sticky='W')
                    button2 = Button(self, text="EDIT existing trip",
                            command=lambda trip=trip: controller.refresh_show_frame(TripDetailsPage,locatorID=trip))
                    button2.grid(row=(n+1),column=1)
            except TypeError:
                pass ## TODO: add label saying no vacays, click add to et started


    class EditTripPage(Frame):
        def __init__(self, parent, controller,locatorID=None):
            Frame.__init__(self, parent)

            trip_name_var=StringVar()
            start_date_var=StringVar()
            budget_var=StringVar() #when intvar, breaks if char

            if locatorID!=None:
                prev_pg=TripDetailsPage
            else:
                prev_pg=TripListPage

            label = Label(self, text="Create or Edit Trip Details Here")
            label.grid(row=0,column=0)
            if locatorID != None:
                label = Label(self, text=locatorID.__str__())
                label.grid(row=1,column=0)

            if locatorID != None:
                button_del = Button(self, text="DELETE entire trip",
                            command=lambda: [popupmsg(controller,"test test",vacations,locatorID),controller.refresh_show_frame(TripListPage)])
                button_del.grid(row=5,column=0)

            button1 = Button(self, text="CANCEL",
                        command=lambda:[controller.refresh_show_frame(prev_pg,locatorID)])
            button1.grid(row=4,column=0)

            button2 = Button(self, text="SAVE", state='disabled', command=lambda:
                controller.refresh_show_frame(TripDetailsPage,save_trip(
                locatorID,trip_name_var.get(),start_date_entry.mon_date.get(),
                start_date_entry.day_date.get(),start_date_entry.year_date.get(),
                budget_var.get())))
            button2.grid(row=4,column=1)

            def savebtn_active(event):
                if event.keysym == 'BackSpace': #reads count before button press, had to add this to count right
                    length=len(trip_name_var.get())-1
                else: #currently counting any button, including 'shift' as input len
                    length=len(trip_name_var.get())+1
                if length<2: #set to 2 for things like 'AZ'
                    button2.config(state='disabled')
                else:
                    button2.config(state='active')
            ####################### entries################
            trip_name_label = Label(self, font=('arial',12),text='Trip Destination:')
            trip_name_label.grid(row=1, sticky="E")
            trip_name_entry = Entry(self, font=('arial',14),width=20, bd=2,insertwidth=2, textvariable=trip_name_var)
            trip_name_entry.bind('<Key>',savebtn_active, add='+')
            trip_name_entry.bind('<Delete>',savebtn_active, add='+')
            trip_name_entry.grid(row=1,column=1)


            start_date_label = Label(self, font=('arial',12),text='Start Date mmm/dd/yr:')
            start_date_label.grid(row=2, sticky="E")
            start_date_entry = DateEntry(self)
            start_date_entry.grid(row=2,column=1)

            budget_label = Label(self, font=('arial',12),text='Budget Total:')
            budget_label.grid(row=3, sticky="E")
            budget_entry = Entry(self, font=('arial',14),width=20, bd=2,insertwidth=2, textvariable=budget_var)
            budget_entry.grid(row=3,column=1)
            # budget_entry.insert(0,'$ ') ## TODO: displays $ disapears when typing, change to greyed out one that stays?
            if locatorID != None:
                button2.config(state='active')
                trip_name_entry.insert(0,locatorID.destination)
                try:
                    datelist=[start_date_entry.mon_date_entry.insert(0,locatorID.mon_date),start_date_entry.day_date_entry.insert(0,locatorID.day_date),start_date_entry.year_date_entry.insert(0,locatorID.year_date)]
                    for d in datelist:
                        try:
                            d
                        except:
                            continue
                except:
                    pass
                try:
                    budget_entry.insert(0,locatorID.budget)
                except:
                    pass


    class TripDetailsPage(Frame):
        def __init__(self, parent, controller,locatorID=None):
            Frame.__init__(self, parent)

            label = Label(self, text="View list of trip costs here:")
            label.grid()
            if locatorID != None:
                for n,cost in enumerate(locatorID.trip_plans):
                    label = Label(self, text=cost.__str__()) ## TODO: add more print details
                    label.grid(row=(1+n),column=0)
                    button4 = Button(self, text="EDIT existing cost",
                                command=lambda: controller.refresh_show_frame(EditCostPage,locatorID=locatorID))
                    button4.grid(row=(1+n),column=1)

            button1 = Button(self, text="Back to Home(DONE)",  #pop up to confirm then redirects page
                            command=lambda: controller.refresh_show_frame(TripListPage))
            button1.grid(row=0,column=3)
            button2 = Button(self, text="EDIT trip details",
                            command=lambda: controller.refresh_show_frame(EditTripPage,locatorID=locatorID))
            button2.grid(row=1,column=3)
            button3 = Button(self, text="ADD new cost",  #pop up asks what kind of cost
                            command=lambda: controller.refresh_show_frame(EditCostPage,locatorID=locatorID))
            button3.grid(row=2,column=3)


    class EditCostPage(Frame):
        def __init__(self, parent, controller,locatorID=None):
            Frame.__init__(self, parent)
            label = Label(self, text="Edit costs or create new one here")
            label.grid()

            button1 = Button(self, text="CANCEL/DELETE, Back to trip details", ##pop up confirmation then redirects page
                            command=lambda: controller.refresh_show_frame(TripDetailsPage,locatorID=locatorID))
            button1.grid(row=1,column=0)
            button2 = Button(self, text="SAVE, Back to trip details",
                            command=lambda: controller.refresh_show_frame(TripDetailsPage,locatorID=locatorID))
            button2.grid(row=1,column=1)



    global vacations #only need because gui is inside main() and functions arent, can probably merge all later
    vacations=new_or_edit(filename)
    root = TravelApp()
    # root.geometry('500x600') #window is auto sizing, this isnt currently needed
    root.mainloop()

if __name__ == '__main__':
    main()
##############################################################################




# TODO: set up delete buttons
# TODO: setup edit cost page same way as 'save' on edit trip page



#pkl file should actually save every time save is clicked.
# could prob work with original file and append like for create_vacaylist_for_save,
# not re-read it everytime but at least save it and use that file.
# so, 'r' file only once at app open, save at every 'save' click, just keep editing
# trip_list as you go, so if program is closed by [X] nothing is lost...

#otherwise have to build in pop up to verify close and save that is linked into base .destroy logic of tkinter
