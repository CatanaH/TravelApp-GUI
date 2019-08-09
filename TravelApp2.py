import pickle
import pdb  #python debugger. use pdb.set_trace()
filename = "pckl_test_file.pkl"
'''
travel app;
chanrge options: 'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'
uses classes to sort and organize and call data as needed

#possible future feature: organizes on calendar, shows what has not been booked for dates, ex. no hotel wednesday night


example inputs:
lodging: price, dates, location, conf#
transportation: price, dates, company, pickup/dropoff, conf#
event: event, price, datetime, conf#, location
food: price, datetime
merch: item, location, price
Fee:
'''
def verify_month(mon_date):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '']
    try:
        print(mon_date)
        mon_date = mon_date.capitalize()[:3]
        if mon_date in months:
            return mon_date
        else:
            return ''
    except:
        return ''
def verify_day(day_date):
    try:
        if int(day_date)>0 and int(day_date)<=31:
            return day_date
        else: #possibly change to finally statement to catch all
            return ''
    except:
        return ''
    pass
def verify_year(year_date):
    try:
        if int(year_date)>10 and int(year_date)<=99:#possibly set better date range
            return year_date
        else: #possibly change to finally statement to catch all
            return ''
    except:
        return ''
#possibly combine dates into one function

class ReservedCost():
    def __init__(self, type, price = '', pay_method = '', pointa = '', #possibly remove this and only assign attr in editcost
        start_date_month = '',start_date_day = '',start_date_year = '',
        start_time = '', pointb = '', end_date_month = '',end_date_day = '',
        end_date_year = '', end_time = '', sub_type = '', conf = '', company = '', misc = ''
    ):
        self.type = type
        self.price = price
        self.pay_method = pay_method
        self.pointa = pointa
        self.start_date_month = verify_month(start_date_month)
        self.start_date_day = verify_day(start_date_day)
        self.start_date_year = verify_year(start_date_year)
        self.start_time  =  start_time
        self.pointb = pointb
        self.end_date_month = verify_month(end_date_month)
        self.end_date_day = verify_day(end_date_day)
        self.end_date_year = verify_year(end_date_year)
        self.end_time = end_time
        self.sub_type = sub_type
        self.conf = conf
        self.company = company
        self.misc = misc


    def edit_cost(self,type, price = '', pay_method = '', pointa = '', #possibly remove '' i think all variables are being fed in, no blanks
        start_date_month = '',start_date_day = '',start_date_year = '',
         start_time = '', pointb = '', end_date_month = '',end_date_day = '',end_date_year = '',
        end_time = '', sub_type = '', conf = '', company = '', misc = ''
    ):
        self.type = type
        try:
            self.price = float(price)
        except:
            self.price = ''
        self.pay_method = pay_method
        self.pointa = pointa
        self.start_date_month = verify_month(start_date_month)
        self.start_date_day = verify_day(start_date_day)
        self.start_date_year = verify_year(start_date_year)
        self.start_time  =  start_time
        self.pointb = pointb
        self.end_date_month = verify_month(end_date_month)
        self.end_date_day = verify_day(end_date_day)
        self.end_date_year = verify_year(end_date_year)
        self.end_time = end_time
        self.sub_type = sub_type
        self.conf = conf
        self.company = company
        self.misc = misc



    def __str__(self):
        #CLI frame for EditCostPage
        try:
            return(("type={}\nprice=${}\npay_method={}\npointa={}\nstart_date={}\nstart_time= {}\npointb= {}\nend_date= {}\nend_time= {}\nsub_type= {}\nconf= {}\ncompany= {}\nmisc= {}").format(self.type, \
                self.price, self.pay_method, self.pointa, self.start_date,
                self.start_time, self.pointb, self.end_date,
                self.end_time,
                self.sub_type, self.conf, self.company, self.misc))
        except:
            return(("type={}\nprice=${}\npay_method={}\npointa={}\nstart_date={}/{}/{}\nstart_time= {}\npointb= {}\nend_date= {}/{}/{}\nend_time= {}\nsub_type= {}\nconf= {}\ncompany= {}\nmisc= {}").format(self.type, \
                self.price, self.pay_method, self.pointa, self.start_date_month,self.start_date_day,self.start_date_year,
                self.start_time, self.pointb, self.end_date_month,self.end_date_day,self.end_date_year,
                self.end_time,
                self.sub_type, self.conf, self.company, self.misc))



class Trip():
    def __init__(self, destination = '', budget = 'None'):
        self.trip_plans = []
        self.destination = destination

        self.budget = budget

    def __str__(self):
        try:
            date = self.mon_date+' '+str(self.day_date)+'/'+str(self.year_date)
        except AttributeError:
            date = 'none'
        return self.destination + ': '+ date # +"budget: "+str(self.budget)

    def update_trip_title(self, tripname, mon_date, day_date, year_date, budget):
        self.destination = tripname
        self.mon_date=verify_month(mon_date)
        self.day_date = verify_day(day_date)
        self.year_date = verify_year(year_date)
        try: #must be number for later maths otherwise make blank
            self.budget = float(budget)
        except:
            self.budget = ''

    def trip_total_price(self):
        #loops to grab price int and add them together
        trip_total = 0
        costs = 0
        for cost in self.trip_plans:
            try:
                trip_total += float(cost.price)
                costs += 1
            except ValueError:
                continue
        return trip_total

    def within_budget_check(self):
        try:
            self.budget = float(self.budget)
        # if type(self.budget) == int or type(self.budget)==float:
            total = self.trip_total_price()
            if self.budget > total:
                remaining = self.budget-total
                return("Running Total=${t} Budget=${b} You have ${r} remaining".format(t = total, b = self.budget, r = remaining))
            else:
                remaining = total-self.budget
                return("Running Total=${t} Budget=${b} You are ${r} over budget".format(t = total, b = self.budget, r = remaining))

        except AttributeError:
            return("error doesnt have a budget")
        except ValueError:
            return("Budget must be a number")

    #####edit travel plans here####
    def add_reserved_cost(self, **kwargs):
        x = ReservedCost(**kwargs)
        self.trip_plans.append(x)

    def remove_cost(self, vacations, costID):
        ## button on EditCostPage, triggers pop up to confirm, then redirects to TripDetailsPage
        try:
            self.trip_plans.remove(costID)
            save_trip_list(vacations, filename)
        except ValueError:
            # TODO: add popup alert o tell user it could not be deleted
            pass


'''
############## functions ################
'''
def load_trip_files(filename):
    with open(filename, 'rb') as f:
        vacations = pickle.load(f)
        return vacations


def sort_trips_descending(trip_list):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '']

    trips_no_date = []#add to end of sorted list
    trips_with_dates = [] #collect obj to sort
    for trip in trip_list:
        try:
            x = (trip.mon_date, trip.day_date, trip.year_date) #maybe delete these later cause error check in trip obj should catch it
            if trip.mon_date not in months:
                trip.mon_date =''
            trips_with_dates.append(trip)
        except AttributeError:
            trips_no_date.append(trip)

    trip_list = sorted(trips_with_dates, key = lambda v: ( v.year_date, months.index(v.mon_date), v.day_date))
    trip_list.extend(trips_no_date)
    vacations = trip_list
    return(trip_list)


def new_or_edit(filename):
    try:
        trip_list = load_trip_files(filename)
        trip_list = sort_trips_descending(trip_list)
        return trip_list
    except (FileNotFoundError):
        # No pre-existing trip plans file found
        return None


def save_cost(locatorID, costID, **kwargs):
    if type(costID)!= str and type(costID) != None: ## TODO: figure out how to test for obj type, to simpify this if statement
        #to overwrite existing ones
        # costID.edit_cost(**kwargs)
        if costID not in locatorID.trip_plans: #checks if obj not in trip list
            print("appending new cost")
            # pdb.set_trace()
            costID.edit_cost(**kwargs)
            locatorID.trip_plans.append(costID)
        else:
            print('catching here')
            costID.edit_cost(**kwargs)
    elif type(costID) == str:#to create new cost obj
        print("Creating new cost")
        locatorID.add_reserved_cost(**kwargs)
    else:
        #maybe popup saying didnt work?
        print('passing thru else statement line 209')
        pass
    print("saving cost")
    save_trip_list(vacations, filename)  #comment outwhile testing to prevent bad data saves
    return locatorID


def save_trip(locatorID, tripName, mon_date, day_date, year_date, budget, controller = None):
    try: #makes sure all data is proper then redirects; except catches errors and does popups
        if locatorID == None: #to create a new trip obj
            trip = Trip()
            trip.update_trip_title(tripName, mon_date, day_date, year_date, budget)
            locatorID = trip #provides new locator ID to work with
        else:
            locatorID.update_trip_title(tripName, mon_date, day_date, year_date, budget)

        create_vacaylist_for_save(vacations, locatorID)
        save_trip_list(vacations, filename)  #comment outwhile testing to prevent bad data saves
        return locatorID

    except TabError: #include specific errors and trigger popups (TabError for test, delete later)
        pass


def delete_trip(triplist, locatorID):
    triplist.pop(triplist.index(locatorID))
    save_trip_list(triplist, filename)


def create_vacaylist_for_save(trip_list, locatorID):
    global vacations #must declare it global to effect outside this function
###### this is for saving trip
    if trip_list == None:
        #("creating new triplist")
        vacations = [locatorID, ]
    elif locatorID in trip_list:
        #dont need to rewrite list, obj already references whats been edited
        pass
    elif locatorID not in trip_list:
        vacations.append(locatorID)

    else:
        #('Failure adding item to vacations list\n')
        ## TODO: popup telling user it failed
        return None #to avoid breaking if this clause runs

def save_trip_list(trip_list, filename):
    '''
    to save trip obj data to be accessed at opening of program
    combine obj's into a list to be uploaded to file
    #I want all trips to be in one file, read/edited/saved to
    '''

    if trip_list == None:
        #No Data to save
        pass
    else: # TODO: add a little notification at top of frame saying if successful
        try:
            with open(filename, 'wb') as output:  # Overwrites any existing file.
                pickle.dump(trip_list, output, -1)
                print("trip list saved")
                #('trip list officially saved')
        except UnboundLocalError:
            #('Cannot Save Trip, Error')
            print('1')
            pass
        except:
            print('2')
            #('other error')
            pass

############################# tkinter stuff ###################################
from tkinter import *


class DateEntry(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        self.mon_date = StringVar()
        self.day_date = StringVar()
        self.year_date = StringVar()
        limit_entry(self.mon_date, 3)
        limit_entry(self.day_date, 2)
        limit_entry(self.year_date, 2)

        self.mon_date_entry = Entry(self, font = ('arial', 14), bd = 2, insertwidth = 2,  width = 3, textvariable = self.mon_date) #month
        self.date_slash_1 = Label(self, text = '/')
        self.day_date_entry = Entry(self, font = ('arial', 14), bd = 2, insertwidth = 2, width = 2, textvariable = self.day_date) #day
        self.date_slash_2 = Label(self, text ='/')
        self.year_date_entry = Entry(self, font =('arial', 14), bd =2, insertwidth =2, width =2, textvariable =self.year_date) #year

        self.mon_date_entry.pack(side = LEFT)
        self.date_slash_1.pack(side =LEFT)
        self.day_date_entry.pack(side =LEFT)
        self.date_slash_2.pack(side =LEFT)
        self.year_date_entry.pack(side =LEFT)


def limit_entry(str_var, length):
    def callback(str_var):
        c = str_var.get()[0:length]
        str_var.set(c)
    str_var.trace("w", lambda name, index, mode, str_var = str_var: callback(str_var))


def main():

    def popup_dlt_cost_conf(controller, vacations, locatorID, costID):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text = 'Delete Cost PopUp')
        label.pack(side = "top", fill = "x", pady = 10)
        B1 = Button(popup, text = "Confirm Delete", command = lambda: [popup.destroy(), locatorID.remove_cost(vacations, costID), controller.refresh_show_frame(TripDetailsPage, locatorID)]) #some reason this is throwing an error when the whole app is closed
        B1.pack()
        B2 = Button(popup, text = "Cancel", command = popup.destroy)
        B2.pack()
        popup.mainloop()

    def popup_dlt_trip_conf(controller, vacations, locatorID):
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text ='Delete Trip PopUp')
        label.pack(side ="top", fill = "x", pady = 10)
        B1 = Button(popup, text ="Confirm Delete", command = lambda: [popup.destroy(), delete_trip(vacations, locatorID), controller.refresh_show_frame(TripListPage)]) #some reason this is throwing an error when the whole app is closed
        B1.pack()
        B2 = Button(popup, text ="Cancel", command = popup.destroy)
        B2.pack()
        popup.mainloop()

    def popup_costtype(controller, msg, locatorID):
        popup = Tk()
        popup.geometry('125x100')
        popup.wm_title("Create a New Cost")
        label = Label(popup, text ='Please pick a cost type')
        label.grid(columnspan = 2)

        def act_btn(*args):
            if costtype_var.get() in list(choices):
                B1.config(state ='active')
        costtype_var = StringVar(popup)
        choices = { 'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'}
        costtype_var.set('choose cost') # set the default option
        popupMenu = OptionMenu(popup, costtype_var, *choices)
        popupMenu.grid(columnspan = 2, sticky ='ew')
        costtype_var.trace('w', act_btn)

        B2 = Button(popup, text = "Cancel", command = popup.destroy)
        B2.grid(row = 3)
        B1 = Button(popup, state = 'disabled', text = "create cost", command = (
            lambda: [popup.destroy(), controller.refresh_show_frame(
            EditCostPage, locatorID, costtype_var.get())]))
        B1.grid(row = 3, column = 1)
        popup.mainloop()

    def popup_change_costtype(controller,locatorID, costID):
        popup = Tk()
        popup.geometry('300x100')
        popup.wm_title("Change Cost Type")
        label = Label(popup, text ='Please pick a new cost type')
        label.grid(columnspan = 2)

        def act_btn(*args):
            if costtype_var.get() in list(choices):
                B1.config(state ='active')
        costtype_var = StringVar(popup)
        choices = { 'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'}
        try:
            costtype_var.set(costID.type) # set the default option
        except:
            costtype_var.set(costID)
        popupMenu = OptionMenu(popup, costtype_var, *choices)
        popupMenu.grid(columnspan = 2, sticky ='ew')
        costtype_var.trace('w', act_btn)

        label2 = Label(popup, text ='Are you sure? This change to cost type will be permanent.')
        label2.grid(row=3,columnspan = 2)

        B2 = Button(popup, text = "Cancel", command = popup.destroy)
        B2.grid(row = 4)
        def reassign_cost_type():
            costID.type=costtype_var.get()
        B1 = Button(popup, state = 'disabled', text = "Confirm Cost Type", command = (
            lambda: [reassign_cost_type(),popup.destroy(), controller.refresh_show_frame(
            EditCostPage, locatorID, costID)]))
        B1.grid(row = 4, column = 1)
        popup.mainloop()


    class TravelApp(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            self.container = Frame(self)
            self.container.pack(side = "top", fill = "both", expand = True)
            self.container.grid_rowconfigure(0, weight = 1)
            self.container.grid_columnconfigure(0, weight = 1)

            self.frames = {}
            for F in (TripListPage, EditTripPage, TripDetailsPage, EditCostPage):
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row = 0, column = 0, sticky = "nsew")

            self.show_frame(TripListPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

        def refresh_show_frame(self, cont, locatorID = None, costID = None):
            self.refresh_frame(cont, locatorID, costID)
            self.show_frame(cont)


        def refresh_frame(self, cont, locatorID, costID):
            frame = self.frames[cont]
            frame.destroy()

            frame = cont(self.container, self, locatorID, costID)
            self.frames[cont] = frame
            frame.grid(row = 0, column = 0, sticky = "nsew")


    class TripListPage(Frame):
        def __init__(self, parent, controller,locatorID=None, costID=None):
            Frame.__init__(self, parent)

            button = Button(self, text = "ADD a new trip",
                                command = lambda: controller.refresh_show_frame(EditTripPage)) #testing, no set to correct destination temp.
            button.grid(row = 0, column = 0)

            try:
                for n, trip in enumerate(sort_trips_descending(vacations)):
                    label = Label(self, text = trip.__str__())
                    label.grid(row = (n+1), column = 0, sticky = 'W')
                    button2  =  Button(self, text = "EDIT existing trip",
                            command = lambda trip = trip: controller.refresh_show_frame(TripDetailsPage, locatorID = trip))
                    button2.grid(row = (n+1), column = 1)
            except TypeError:
                pass ## TODO: add label saying no vacays, click add to et started


    class EditTripPage(Frame):
        def __init__(self, parent, controller, locatorID = None, costID = None):
            Frame.__init__(self, parent)

            trip_name_var = StringVar()
            # start_date_var = StringVar()
            budget_var = StringVar() #when intvar, breaks if char

            if locatorID != None:
                prev_pg = TripDetailsPage
            else:
                prev_pg = TripListPage

            label = Label(self, text = "Create or Edit Trip Details Here")
            label.grid(row = 0, column = 0)
            if locatorID != None:
                label = Label(self, text = locatorID.__str__())
                label.grid(row = 1, column = 0)

            if locatorID != None:
                button_del = Button(self, text = "DELETE entire trip",
                            command = lambda: popup_dlt_trip_conf(controller, vacations, locatorID))
                button_del.grid(row = 5, column = 0)

            button1 = Button(self, text = "CANCEL",
                        command = lambda:[controller.refresh_show_frame(prev_pg, locatorID)])
            button1.grid(row = 4, column = 0)

            button2 = Button(self, text = "SAVE", state = 'disabled', command = lambda:
                controller.refresh_show_frame(TripDetailsPage, save_trip(
                locatorID, trip_name_var.get(), start_date_entry.mon_date.get(),
                start_date_entry.day_date.get(), start_date_entry.year_date.get(),
                budget_var.get())))
            button2.grid(row = 4, column = 1)

            def savebtn_active(event):
                if event.keysym == 'BackSpace': #reads count before button press, had to add this to count right
                    length = len(trip_name_var.get())-1
                else: #currently counting any button, including 'shift' as input len
                    length = len(trip_name_var.get())+1
                if length<2: #set to 2 for things like 'AZ'
                    button2.config(state = 'disabled')
                else:
                    button2.config(state = 'active')
            ####################### entries################
            trip_name_label = Label(self, font = ('arial', 12), text = 'Trip Destination:')
            trip_name_label.grid(row = 1, sticky = "E")
            trip_name_entry  =  Entry(self, font = ('arial', 14), width = 20, bd = 2, insertwidth = 2, textvariable = trip_name_var)
            trip_name_entry.bind('<Key>', savebtn_active, add = '+')
            trip_name_entry.bind('<Delete>', savebtn_active, add = '+')
            trip_name_entry.grid(row = 1, column = 1)


            start_date_label = Label(self, font = ('arial', 12), text = 'Start Date mmm/dd/yr:')
            start_date_label.grid(row = 2, sticky = "E")
            start_date_entry = DateEntry(self)
            start_date_entry.grid(row = 2, column = 1)

            budget_label = Label(self, font = ('arial', 12), text = 'Budget Total:')
            budget_label.grid(row = 3, sticky = "E")
            budget_entry = Entry(self, font = ('arial', 14), width = 20, bd = 2, insertwidth = 2, textvariable = budget_var)
            budget_entry.grid(row = 3, column = 1)
            # budget_entry.insert(0,'$ ') ## TODO: displays $ disapears when typing, change to greyed out one that stays?
            if locatorID != None:
                button2.config(state = 'active')
                trip_name_entry.insert(0, locatorID.destination)
                try:
                    datelist = [start_date_entry.mon_date_entry.insert(0, locatorID.mon_date), start_date_entry.day_date_entry.insert(0, locatorID.day_date), start_date_entry.year_date_entry.insert(0, locatorID.year_date)]
                    for d in datelist:
                        try:
                            d
                        except:
                            continue
                except:
                    pass
                try:
                    budget_entry.insert(0, locatorID.budget)
                except:
                    pass


    class TripDetailsPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None):
            Frame.__init__(self, parent)

            label = Label(self, text = "View list of trip costs here:")
            label.grid()
            label2 = Label(self, text = locatorID.__str__())
            label2.grid(row=0,column=1)
            if locatorID != None:
                for n, cost in enumerate(locatorID.trip_plans):
                    label = Label(self, text = cost.__str__()) ## TODO: add more print details
                    label.grid(row = (1+n), column = 0)
                    button4 = Button(self, text = "EDIT existing cost",
                                command = lambda cost = cost: controller.refresh_show_frame(EditCostPage, locatorID, cost))
                    button4.grid(row = (1+n), column = 1)

            button1 = Button(self, text = "Back to Home(DONE)",  #pop up to confirm then redirects page
                            command = lambda: controller.refresh_show_frame(TripListPage))
            button1.grid(row = 0, column = 3)
            button2 = Button(self, text = "EDIT trip details",
                            command = lambda: controller.refresh_show_frame(EditTripPage, locatorID = locatorID))
            button2.grid(row = 1, column = 3)
            button3 = Button(self, text = "ADD new cost",  #pop up asks what kind of cost
                            command = lambda: popup_costtype(controller, 'pick a cost', locatorID))
                            #controller.refresh_show_frame(EditCostPage,locatorID = locatorID)
            button3.grid(row = 2, column = 3)
            if locatorID != None:
                label = Label(self, text = locatorID.within_budget_check())
                label.grid(row = 3, column = 3)


    class EditCostPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None):
            Frame.__init__(self, parent)

            #cant use type() since obj has attribute type
            if costID in ('Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'):
                temp_obj = ReservedCost(type=costID)
                costID = temp_obj
            try:
                type = costID.type
            except AttributeError:
                type = costID

            label = Label(self, text = "Edit costs or create new one here")
            label.grid()


            button1 = Button(self, text = "CANCEL", ##pop up confirmation then redirects page
                            command = lambda: controller.refresh_show_frame(TripDetailsPage, locatorID = locatorID))
            button1.grid(row = 1, column = 0)
            button2 = Button(self, text = "SAVE", command = lambda: controller.refresh_show_frame(TripDetailsPage,
                save_cost(locatorID, costID, type = type, price = price.get(), pay_method = pay_method.get(),
                pointa = pointa.get(), start_date_month = start_date.mon_date.get() ,start_date_day = start_date.day_date.get(),start_date_year = start_date.year_date.get(), start_time = start_time.get(),
                pointb = pointb.get(), end_date_month = end_date.mon_date.get() ,end_date_day = end_date.day_date.get(),end_date_year = end_date.year_date.get(), end_time = end_time.get(), sub_type = sub_type.get(),
                conf = conf.get(), company = company.get(), misc = misc.get())))
            button2.grid(row = 1, column = 1)


            if locatorID != None:
                button_del = Button(self, text = "DELETE Cost Item",
                    command = lambda: popup_dlt_cost_conf(controller, vacations, locatorID, costID))
                button_del.grid(row = 1, column = 2)#should this be costID? todo

            # #######################labels and entry fields ################################
            med_font = ('arial', 14)
            sub_type = StringVar()
            type = type
            price = StringVar()
            pay_method = StringVar()
            start_date = DateEntry(self)
            end_date = DateEntry(self)
            company = StringVar()
            conf = StringVar()
            pointa = StringVar()
            pointb = StringVar()
            start_time = StringVar()
            end_time = StringVar()
            misc = StringVar()

            # tells wich fields to print compared to label_entry_dict
            cost_type_dict = {
            'Fee':[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            'Merchandise':[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            'Meal':[1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            'Transportation':[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            'Lodging':[1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
            'Event':[1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1]}

            for cost in cost_type_dict: #selects filter for cost type
                if type == cost:
                    activate_entry = cost_type_dict[cost]
                    break
                else:
                    activate_entry = None
            # TODO: make this word prettier for ease of reading
            label_entry_dict = {'type':type,
                        'sub_type':sub_type,
                        'price':price,
                        'pay_method':pay_method,
                        'start_date':start_date, # TODO: start/end date need to be date fields
                        'end_date':end_date,
                        'company':company,
                        'conf_num':conf,
                        'point_a':pointa,
                        'point_b':pointb,
                        'start_time':start_time,
                        'end_time':end_time,
                        'misc':misc
                        }

            if activate_entry!=None:
                for n, x in enumerate(label_entry_dict):
                    if n % 2 == 0:
                        col = 0
                        row = 2+n
                    else:
                        col = 3
                        row = 1+n
                    if activate_entry[n]:
                        if x == 'type':
                            label = Label(self, font = med_font, text = type)
                            label.grid(row = row, column = col+1, sticky = "E")
                            button = Button(self, text = "Change Cost Type", command=lambda:[ costID.edit_cost(type = type, price = price.get(), pay_method = pay_method.get(),
                            pointa = pointa.get(), start_date_month = start_date.mon_date.get() ,start_date_day = start_date.day_date.get(),start_date_year = start_date.year_date.get(),
                            start_time = start_time.get(), pointb = pointb.get(), end_date_month = end_date.mon_date.get() ,end_date_day = end_date.day_date.get(),end_date_year = end_date.year_date.get(),                   end_time = end_time.get(), sub_type = sub_type.get(),
                            conf = conf.get(), company = company.get(), misc = misc.get()),popup_change_costtype(controller,locatorID,costID)])
                            button.grid(row = row, column = col)
                        else:
                            label = Label(self, font = med_font, text = x)# TODO: change to what type of ...+ for subtype
                            label.grid(row = row, column = col, sticky = "E")
                            if x == 'start_date' or x == 'end_date':  #creates date field instead of text entry
                                label_entry_dict[x].grid(row = row, column = col+1)
                                try:
                                    if x == 'start_date':
                                        start_date.mon_date_entry.insert(0, costID.start_date_month)
                                        start_date.day_date_entry.insert(0, costID.start_date_day)
                                        start_date.year_date_entry.insert(0, costID.start_date_year)
                                    else:
                                        end_date.mon_date_entry.insert(0, costID.end_date_month)
                                        end_date.day_date_entry.insert(0, costID.end_date_day)
                                        end_date.year_date_entry.insert(0, costID.end_date_year)
                                except AttributeError:
                                    continue
                            else:  #creates basic text entry
                                entry = Entry(self, font = med_font, width = 20, bd = 2, insertwidth = 2, textvariable = label_entry_dict[x])
                                entry.grid(row = row, column = col+1)
                                if costID != None:
                                    try: # TODO: move where this list is stored
                                        assign_lst = [costID.type, costID.sub_type, costID.price,
                                        costID.pay_method, '','', costID.company, costID.conf, costID.pointa, costID.pointb,
                                        costID.start_time, costID.end_time, costID.misc]
                                        entry.insert(0, str(assign_lst[n]))
                                    except AttributeError:
                                        continue
                    elif activate_entry[n]==0: #for erasing unused data if present
                        assign_lst = [costID.type, costID.sub_type, costID.price,
                        costID.pay_method, (costID.start_date_month,costID.start_date_day,costID.start_date_year),
                        (costID.end_date_month,costID.end_date_day,costID.end_date_year), 
                        costID.company, costID.conf, costID.pointa, costID.pointb,
                        costID.start_time, costID.end_time, costID.misc]
                        for x in assign_lst[n]:
                            x = None #reassigns to blank variable so when saved won't be hiding in the background.

            # pdb.set_trace()

    global vacations #only need because gui is inside main() and functions arent, can probably merge all later
    vacations = new_or_edit(filename)
    root = TravelApp()
    # root.geometry('500x600') #window is auto sizing, this isnt currently needed
    root.mainloop()

if __name__ == '__main__':
    main()
##############################################################################




# TODO:  customize what prints in edit cost labels

# TODO: add misc field to trip edit
# TODO: add date fields to edit cost page dates
# TODO: sort trip details by date
# TODO: make trip details display nicer, easier to read.
# TODO: build tests to automate and check when i make changes
# TODO: add scroll bar to long pages
# TODO: make the whole thing look nicer with styling
# TODO: figure out how to pass an event into the save btn_active so i dont have to rewrite it for both edit pages

#should be an add in field to add category to any charge... might be unnecessarily difficult. prob not do.
#have a add loging to transportation button for things like cruises. just for future tracking
#

## commit:
