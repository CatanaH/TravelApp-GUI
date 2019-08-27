import pickle
import os
import pdb  # python debugger. use pdb.set_trace()

filename = "pckl_test_file.pkl"
'''
travel app;
charge options: 'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'
uses classes to sort and organize and call data as needed

'''


class ReservedCost():
    def __init__(self, type=None):
        self.type = type

    def edit_cost(self, type, price='', pay_method='', pointa='',
                  start_date_month='', start_date_day='', start_date_year='',
                  start_time='', pointb='', end_date_month='', end_date_day='', end_date_year='',
                  end_time='', sub_type='', conf='', company='', misc=''
                  ):   # possibly remove '', i think all variables are being fed in, no blanks
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
        self.start_time = start_time
        self.pointb = pointb
        self.end_date_month = verify_month(end_date_month)
        self.end_date_day = verify_day(end_date_day)
        self.end_date_year = verify_year(end_date_year)
        self.end_time = end_time
        self.sub_type = sub_type
        self.conf = conf
        self.company = company
        self.misc = misc

        tlogo_dict = {'Transportation': 'vespasm.png',
                      'Lodging': 'bedsm.png',
                      'Event':'ad_tix.png',
                      'Meal': 'foodsm.png',
                      'Merchandise': 'bbagsm.png',
                      'Fee': 'moneysm.png'}
        self.type_logo = tlogo_dict[type]

    def __str__(self):
        return (("{}\t\t{}\n{}\t\t{}\t\t${}").format(
            self.sub_type, self.company, self.pointa, self.start_time, self.price))


class Trip():
    def __init__(self, destination='', budget='None'):
        self.trip_plans = []
        self.destination = destination

        self.budget = budget

    def __str__(self):
        try:
            date = self.mon_date + ' ' + str(self.day_date) + '/' + str(self.year_date)
        except AttributeError:
            date = 'none'
        return self.destination + '\n' + date  # +"budget: "+str(self.budget)

    def update_trip_title(self, tripname, mon_date, day_date, year_date, end_mon, end_day, end_year, budget, note):
        self.destination = tripname
        self.mon_date = verify_month(mon_date)
        self.mon_color = self.assign_color(self.mon_date)
        self.day_date = verify_day(day_date)
        self.year_date = verify_year(year_date)
        self.end_mon = verify_month(end_mon)
        self.end_day = verify_day(end_day)
        self.end_year = verify_year(end_year)
        try:  # must be number for later maths otherwise make blank
            self.budget = round(float(budget), 2)
        except:
            self.budget = ''
        self.note = note

    def trip_total_price(self):
        # loops to grab price int and add them together
        trip_total = 0
        costs = 0
        for cost in self.trip_plans:
            try:
                trip_total += float(cost.price)
                costs += 1
            except ValueError:
                continue
        return round(trip_total, 2)

    def within_budget_check(self):
        try:
            self.budget = float(self.budget)
            total = self.trip_total_price()
            if self.budget > total:
                remaining = self.budget - total
                return "Remaining: ${}".format(round(remaining, 2))
            else:
                remaining = total - self.budget
                return "Over Budget: ${}".format(round(remaining, 2))

        except (AttributeError, ValueError):
            return " "

    def assign_color(self, month):
        mon_col_dict = {'Jan': '#F0C5E8',  # C40093
                        'Feb': '#EDD4FB',  # 8D00DE
                        'Mar': '#D2BEFD',  # 096EBE
                        'Apr': '#B4C3FC',  # 038AB0
                        'May': '#D6F3FE',  # 02A3A3
                        'Jun': '#D1FFE2',  # 01A689
                        'Jul': '#E3FFCC',  # 01B850
                        'Aug': '#FBFEC7',  # D0E009
                        'Sep': '#FFF1B7',  # EFCB09
                        'Oct': '#FEDB9F',  # F29809
                        'Nov': '#FFB7BF',  # F52D24
                        'Dec': '#FEC2DF',  # E10064
                        '': 'white'}
        return mon_col_dict[month]

    #####edit travel plans here####
    def add_reserved_cost(self, **kwargs):
        x = ReservedCost()
        x.edit_cost(**kwargs)
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


def resource_path(relative_path):  # for accessing pictures and data files
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def verify_month(mon_date):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '']
    try:
        mon_date = mon_date.capitalize()[:3]
        if mon_date in months:
            return mon_date
        else:
            return ''
    except:
        return ''


def verify_day(day_date):
    try:
        if int(day_date) > 0 and int(day_date) <= 31:
            if len(str(day_date)) == 1:  # turns day into 2 digits (1 >> 01)
                day_date = '0' + str(day_date)
            return day_date
        else:  # possibly change to finally statement to catch all
            return ''
    except:
        return ''
    pass


def verify_year(year_date):
    try:
        if int(year_date) > 10 and int(year_date) <= 99:  # possibly set better date range
            return year_date
        else:  # possibly change to finally statement to catch all
            return ''
    except:
        return ''
# possibly combine dates into one function


def load_trip_files(filename):
    with open(filename, 'rb') as f:
        vacations = pickle.load(f)
        return vacations


def sort_trips_descending(trip_list):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '']

    trips_no_date = []  # add to end of sorted list
    trips_with_dates = []  # collect obj to sort
    for trip in trip_list:
        try:
            x = (trip.mon_date, trip.day_date,
                 trip.year_date)  # maybe delete these later cause error check in trip obj should catch it
            if trip.mon_date not in months:
                trip.mon_date = ''
            trips_with_dates.append(trip)
        except AttributeError:
            trips_no_date.append(trip)

    trip_list = sorted(trips_with_dates, key=lambda v: (v.year_date, months.index(v.mon_date), v.day_date))
    trip_list.extend(trips_no_date)
    vacations = trip_list
    return (trip_list)


def sort_costs_descending(trip_list):
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec', '']
    trips_no_date = []  # add to end of sorted list
    trips_with_dates = []  # collect obj to sort
    for trip in trip_list:
        try:
            x = (trip.start_date_month, trip.start_date_day, trip.start_date_year)
            if trip.start_date_month not in months:  ## TODO: possibly remove if error check in init catches this
                trip.start_date_month = ''
            trips_with_dates.append(trip)
        except AttributeError:
            trips_no_date.append(trip)

    trip_list = sorted(trips_with_dates,
                       key=lambda v: (v.start_date_year, months.index(v.start_date_month), v.start_date_day))
    trip_list.extend(trips_no_date)
    return (trip_list)


def new_or_edit(filename):
    try:
        trip_list = load_trip_files(filename)
        trip_list = sort_trips_descending(trip_list)
        return trip_list
    except (FileNotFoundError):
        # No pre-existing trip plans file found
        return None


def save_cost(locatorID, costID, **kwargs):
    if type(costID) != str and type(
            costID) != None:  ## TODO: figure out how to test for obj type, to simpify this if statement
        if costID not in locatorID.trip_plans:  # checks if obj not in trip list
            costID.edit_cost(**kwargs)
            locatorID.trip_plans.append(costID)
        else:
            costID.edit_cost(**kwargs)  # to overwrite existing ones
    elif type(costID) == str:  # to create new cost obj
        locatorID.add_reserved_cost(**kwargs)
    else:
        print('passing thru else statement line 209')  # maybe popup saying didnt work?
        pass
    locatorID.trip_plans = sort_costs_descending(locatorID.trip_plans)
    save_trip_list(vacations, filename)  # comment outwhile testing to prevent bad data saves
    return locatorID


def save_trip(locatorID, tripName, mon_date, day_date, year_date, end_mon, end_day, end_year, budget, note, controller=None):
    try:  # makes sure all data is proper then redirects; except catches errors and does popups
        if locatorID == None:  # to create a new trip obj
            trip = Trip()
            trip.update_trip_title(tripName, mon_date, day_date, year_date, end_mon, end_day, end_year,budget, note)
            locatorID = trip  # provides new locator ID to work with
        else:
            locatorID.update_trip_title(tripName, mon_date, day_date, year_date, end_mon, end_day, end_year, budget, note)

        create_vacaylist_for_save(vacations, locatorID)
        save_trip_list(vacations, filename)  # comment outwhile testing to prevent bad data saves
        return locatorID

    except TabError:  # include specific errors and trigger popups (TabError for test, delete later)
        pass


def delete_trip(triplist, locatorID):
    triplist.pop(triplist.index(locatorID))
    save_trip_list(triplist, filename)


def create_vacaylist_for_save(trip_list, locatorID):
    global vacations  # must declare it global to effect outside this function
    ###### this is for saving trip
    if trip_list == None:
        # ("creating new triplist")
        vacations = [locatorID, ]
    elif locatorID in trip_list:
        # dont need to rewrite list, obj already references whats been edited
        pass
    elif locatorID not in trip_list:
        vacations.append(locatorID)

    else:
        # ('Failure adding item to vacations list\n')
        ## TODO: popup telling user it failed
        return None  # to avoid breaking if this clause runs


def save_trip_list(trip_list, filename):
    '''
    to save trip obj data to be accessed at opening of program
    combine obj's into a list to be uploaded to file
    #I want all trips to be in one file, read/edited/saved to
    '''

    if trip_list == None:
        # No Data to save
        pass
    else:  # TODO: add a little notification at top of frame saying if successful
        try:
            with open(filename, 'wb') as output:  # Overwrites any existing file.
                pickle.dump(trip_list, output, -1)
                print("trip list saved")
        except UnboundLocalError:
            # ('Cannot Save Trip, Error')
            print('1')
            pass
        except:
            print('2')
            pass


############################# tkinter stuff ###################################
from tkinter import *


class DateEntry(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        detail_entry_config = {'font': ('arial', 14), 'fg': 'black', 'bd': 2, 'insertwidth': 2}
        self.mon_date = StringVar()
        self.day_date = StringVar()
        self.year_date = StringVar()
        limit_entry(self.mon_date, 3)
        limit_entry(self.day_date, 2)
        limit_entry(self.year_date, 2)

        self.mon_date_entry = Entry(self, width=3, textvariable=self.mon_date, **detail_entry_config)  # month
        self.date_slash_1 = Label(self, text='/')
        self.day_date_entry = Entry(self, width=2, textvariable=self.day_date, **detail_entry_config)  # day
        self.date_slash_2 = Label(self, text='/')
        self.year_date_entry = Entry(self, width=2, textvariable=self.year_date, **detail_entry_config)  # year

        self.mon_date_entry.pack(side=LEFT)
        self.date_slash_1.pack(side=LEFT)
        self.day_date_entry.pack(side=LEFT)
        self.date_slash_2.pack(side=LEFT)
        self.year_date_entry.pack(side=LEFT)


def limit_entry(str_var, length):
    def callback(str_var):
        c = str_var.get()[0:length]
        str_var.set(c)

    str_var.trace("w", lambda name, index, mode, str_var=str_var: callback(str_var))


def main():
    def popup_dlt_cost_conf(controller, vacations, locatorID, costID):
        popup = Tk()  # todo: fix so cant open more than one window a time
        popup.wm_title("!")
        popup.geometry('250x113+650+200')

        lbl_config = {'font': ('arial', 12), 'fg': '#326DA8', 'padx': 2, 'width': 25, 'height': 4}
        btn_config = {'width': 15, 'bg': '#145075', 'fg': '#D0E0EA'}

        label = Label(popup, text='Are you sure you want to delete this cost item?', **lbl_config, wraplength=200)
        label.grid(columnspan=2)
        del_btn = Button(popup, text="Confirm Delete",
                         command=lambda: [popup.destroy(), locatorID.remove_cost(vacations, costID),
                                          controller.refresh_show_frame(TripDetailsPage, locatorID)], **btn_config)
        del_btn.grid(row=1, column=1, padx=5, pady=5)
        cancl_btn = Button(popup, text="Cancel", command=popup.destroy, **btn_config)
        cancl_btn.grid(row=1, column=0, padx=5, pady=5)
        popup.mainloop()

    def popup_dlt_trip_conf(controller, vacations, locatorID):
        popup = Tk()
        popup.wm_title("!")
        popup.geometry('250x113+650+200')
        lbl_config = {'font': ('arial', 12), 'fg': '#326DA8', 'padx': 2, 'width': 25, 'height': 4}
        btn_config = {'width': 15, 'bg': '#145075', 'fg': '#D0E0EA'}

        label = Label(popup, text='Are you sure you want to delete this Entire Trip?', **lbl_config, wraplength=200)
        label.grid(columnspan=2)
        del_btn = Button(popup, text="Confirm Delete",
                         command=lambda: [popup.destroy(), delete_trip(vacations, locatorID),
                                          controller.refresh_show_frame(TripListPage)], **btn_config)
        del_btn.grid(row=1, column=1, padx=5, pady=5)
        cancl_btn = Button(popup, text="Cancel", command=popup.destroy, **btn_config)
        cancl_btn.grid(row=1, column=0, padx=5, pady=5)
        popup.mainloop()

    def popup_costtype(controller, msg, locatorID):
        popup = Tk()
        popup.geometry('250x115+650+200')
        popup.wm_title("Create a New Cost")
        lbl_config = {'font': ('arial', 13), 'fg': '#326DA8', 'padx': 2, 'width': 25, 'height': 2}
        btn_config = {'width': 15, 'bg': '#EBEDEE'}

        label = Label(popup, text='Please pick a cost type', **lbl_config)
        label.grid(columnspan=2)

        def act_btn(*args):
            if costtype_var.get() in list(choices):
                create_btn.config(state='active')

        costtype_var = StringVar(popup)

        choices = {'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'}
        costtype_var.set('choose cost')  # set the default option

        popupMenu = OptionMenu(popup, costtype_var, *choices)
        popupMenu.grid(columnspan=2, sticky='ew', padx=5)
        costtype_var.trace('w', act_btn)
        popupMenu.config(font=('arial', 12), bg='#EBEDEE', width=20)

        cancl_btn = Button(popup, text="Cancel", command=popup.destroy, **btn_config)
        cancl_btn.grid(row=3, padx=5, pady=5)
        create_btn = Button(popup, state='disabled', text="create cost", command=(
            lambda: [popup.destroy(), controller.refresh_show_frame(EditCostPage, locatorID,
                                                                    costtype_var.get())]), **btn_config)
        create_btn.grid(row=3, column=1, padx=5, pady=5)
        popup.mainloop()

    def popup_change_costtype(controller, locatorID, costID):
        def act_btn(*args):
            if costtype_var.get() in list(choices):
                confirm_btn.config(state='active')

        def reassign_cost_type():
            costID.type = costtype_var.get()

        popup = Tk()
        popup.geometry('250x165+650+200')
        popup.wm_title("Change Cost Type")
        lbl_config = {'font': ('arial', 13), 'fg': '#326DA8', 'padx': 2, 'width': 25, 'height': 2}
        btn_config = {'width': 15, 'bg': '#EBEDEE'}

        label = Label(popup, text='Please pick a new cost type', **lbl_config)
        label.grid(columnspan=2)

        # Dropdown menu
        choices = {'Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'}
        costtype_var = StringVar(popup)
        try:
            costtype_var.set(costID.type)  # set the default option
        except:
            costtype_var.set(costID)
        popupMenu = OptionMenu(popup, costtype_var, *choices)
        popupMenu.grid(columnspan=2, sticky='ew', padx=5)
        costtype_var.trace('w', act_btn)
        popupMenu.config(font=('arial', 12), bg='#EBEDEE', width=20)

        label2 = Label(popup, text='Are you sure? This will be permanent.', **lbl_config, wraplength=200)
        label2.grid(row=3, columnspan=2, pady=5)

        cancel_btn = Button(popup, text="Cancel", command=popup.destroy, **btn_config)
        cancel_btn.grid(row=4, padx=5, pady=5)

        confirm_btn = Button(popup, state='disabled', text="Confirm Cost Type", command=(
            lambda: [reassign_cost_type(), popup.destroy(), controller.refresh_show_frame(
                EditCostPage, locatorID, costID)]), **btn_config)
        confirm_btn.grid(row=4, column=1, padx=5, pady=5)

        popup.mainloop()

    class TravelApp(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            self.container = Frame(self)
            self.container.pack(side="top", fill="both", expand=True)
            self.container.grid_rowconfigure(0, weight=1)
            self.container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (EditTripPage, TripDetailsPage, EditCostPage, TripListPage):
                frame = F(self.container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(TripListPage)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

        def refresh_show_frame(self, cont, locatorID=None, costID=None):
            self.refresh_frame(cont, locatorID, costID)
            self.show_frame(cont)

        def refresh_frame(self, cont, locatorID, costID):
            frame = self.frames[cont]
            frame.destroy()

            frame = cont(self.container, self, locatorID, costID)
            self.frames[cont] = frame
            frame.grid(row=0, column=0, sticky="nsew")

    class TripListPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None):
            Frame.__init__(self, parent)
            self.canvas = Canvas(self, borderwidth=0, height=545)
            self.frame = Frame(self.canvas)
            self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.vsb.set)
            self.vsb.grid(row=1, column=1, sticky='ns')
            self.canvas.grid(row=1, column=0)
            self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")
            self.frame.bind("<Configure>", self.on_frame_config)
            self.frame.bind_all("<MouseWheel>", self.on_mousewheel)

            ######### trip Header ##########
            headcl = '#B1DEFA'
            self.headerf = Frame(self)
            self.headerf.grid(row=0, column=0)

            label = Label(self.headerf, text="Voyages", bg=headcl, height=1, width=42, font=('arial', 13))
            label.grid(row=0, column=0)

            #######  contents #########
            photo = PhotoImage(
                file=resource_path('Airplane_basicsm.png'))  # TODO: photo will be optional for user to customize
            button_config = {'image': photo, 'height': 50, 'width': 365, 'compound': 'left', 'bd': 6, 'justify': 'left',
                             'anchor': 'w'}
            try:
                for n, trip in enumerate(sort_trips_descending(vacations)):
                    trip.mon_color = trip.assign_color(trip.mon_date)  # for assigning colors, temp instant to populate
                    trip_button = Button(self.frame, text=trip.__str__(),
                                         command=lambda trip=trip: controller.refresh_show_frame(
                                             TripDetailsPage, locatorID=trip), bg=trip.mon_color, **button_config)
                    trip_button.image = photo
                    trip_button.grid(row=(n + 1))
            except TypeError:
                no_trips_label = Label(self.frame, text="You have no Voyages planned yet.\n "
                                                        "Click 'ADD' to plan a new one",
                                       font=('arial', '16'), padx=20, height=4)
                no_trips_label.grid()

            ###### Bottom Buttons #######
            self.directoryf = Frame(self, bg='#1A6493')
            self.directoryf.grid(row=3, column=0)

            add_btn_config = {'width': 10, 'bg': '#145075', 'fg': '#D0E0EA'}
            add_btn = Button(self.directoryf, text="ADD", command=lambda:
            controller.refresh_show_frame(EditTripPage), **add_btn_config)
            add_btn.grid(row=0, column=0, padx=151, pady=10)

        ######## Methods ##########
        def on_mousewheel(self, event):
            self.canvas.yview_scroll(-1 * int(event.delta / 60), "units")

        def on_frame_config(self, event):
            '''Reset the scroll region to encompass the inner frame'''
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    class EditTripPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None):
            Frame.__init__(self, parent)
            self.canvas = Canvas(self, borderwidth=0, height=545)
            self.frame = Frame(self.canvas)
            self.canvas.grid(row=1, column=0)
            self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")

            trip_name_var = StringVar()
            budget_var = StringVar()  # when intvar, breaks if char
            note_var = StringVar()

            trip_lbl_config = {'font': ('arial', 12), 'fg': '#326DA8', 'padx': 2, 'anchor': 'w', 'width': 25,
                               'height': 2}
            trip_entry_config = {'font': ('arial', 14), 'fg': 'black', 'bd': 2, 'width': 30, 'insertwidth': 2}
            if locatorID != None:
                prev_pg = TripDetailsPage
            else:
                prev_pg = TripListPage

            ######### trip Header ##########
            headcl = '#B1DEFA'
            self.headerf = Frame(self, )
            self.headerf.grid(row=0, column=0)

            label = Label(self.headerf, text="Create or Edit Trip Details Here", bg=headcl, height=1, width=42,
                          font=('arial',
                                13))  # todo: change width to a math func that checks frame size and fills in the diff from the text
            label.grid(row=0, column=0)

            ####################### entries################
            trip_name_label = Label(self.frame, text='Trip Destination:', **trip_lbl_config)
            trip_name_label.grid(row=0, sticky="W")
            trip_name_entry = Entry(self.frame, textvariable=trip_name_var, **trip_entry_config)
            trip_name_entry.bind('<Key>', lambda event, arg=trip_name_var: self.savebtn_active(event, arg), add='+', )
            trip_name_entry.bind('<Delete>', lambda event, arg=trip_name_var: self.savebtn_active(event, arg), add='+')
            trip_name_entry.grid(row=1, sticky="W")

            start_date_label = Label(self.frame, text='Start Date mmm/dd/yr:', **trip_lbl_config)
            start_date_label.grid(row=2, sticky="W")
            start_date_entry = DateEntry(self.frame)
            start_date_entry.grid(row=3, sticky="W")

            end_date_label = Label(self.frame, text='End Date mmm/dd/yr:', **trip_lbl_config)
            end_date_label.grid(row=4, sticky="W")
            end_date_entry = DateEntry(self.frame)
            end_date_entry.grid(row=5, sticky="W")

            budget_label = Label(self.frame, text='Budget Total:', **trip_lbl_config)
            budget_label.grid(row=6, sticky="W")
            budget_entry = Entry(self.frame, textvariable=budget_var, **trip_entry_config)
            budget_entry.grid(row=7, sticky="W")
            # budget_entry.insert(0,'$ ') ## TODO: displays $ disapears when typing, change to greyed out one that stays?

            misc_label = Label(self.frame, text='Trip Notes:', **trip_lbl_config)
            misc_label.grid(row=8, sticky="W")
            misc_entry = Text(self.frame, height=8, **trip_entry_config)
            misc_entry.grid(row=9, sticky="W")

            ###### bottom directory #######
            self.directoryf = Frame(self, bg='#1A6493')
            self.directoryf.grid(row=2, column=0)
            cost_btn_config = {'width': 10, 'bg': '#145075', 'fg': '#D0E0EA'}

            if locatorID != None:
                grid_config = {'padx': 27, 'pady': 10}
                button_del = Button(self.directoryf, text="DELETE",
                                    command=lambda: popup_dlt_trip_conf(controller, vacations, locatorID),
                                    **cost_btn_config)
                button_del.grid(row=0, column=2, **grid_config)
            else:
                grid_config = {'padx': 60, 'pady': 10}

            cancel_btn = Button(self.directoryf, text="CANCEL",
                                command=lambda: [controller.refresh_show_frame(prev_pg, locatorID)], **cost_btn_config)
            cancel_btn.grid(row=0, column=0, **grid_config)

            self.save_btn = Button(self.directoryf, text="SAVE", highlightbackground='red',
                                   command=lambda: controller.refresh_show_frame(TripDetailsPage,
                                                                                 save_trip(locatorID,
                                                                                           trip_name_var.get(),
                                                                                           start_date_entry.mon_date.get(),
                                                                                           start_date_entry.day_date.get(),
                                                                                           start_date_entry.year_date.get(),
                                                                                           end_date_entry.mon_date.get(),
                                                                                           end_date_entry.day_date.get(),
                                                                                           end_date_entry.year_date.get(),
                                                                                           budget_var.get(),
                                                                                           misc_entry.get("1.0",
                                                                                                          'end-1c'))),
                                   **cost_btn_config)
            self.save_btn.grid(row=0, column=1, **grid_config)

            if locatorID is None:
                self.save_btn.config(state='disabled')
            else:  # Populates any existing trip info for entry fields
                trip_name_entry.insert(0, locatorID.destination)
                try:
                    populate_trip_list = [start_date_entry.mon_date_entry.insert(0, locatorID.mon_date),
                                          start_date_entry.day_date_entry.insert(0, locatorID.day_date),
                                          start_date_entry.year_date_entry.insert(0, locatorID.year_date),
                                          end_date_entry.mon_date_entry.insert(0, locatorID.end_mon),
                                          end_date_entry.day_date_entry.insert(0, locatorID.end_day),
                                          end_date_entry.year_date_entry.insert(0, locatorID.end_year),
                                          budget_entry.insert(0, locatorID.budget),
                                          misc_entry.insert(END, locatorID.note)]
                    for pop in populate_trip_list:
                        try:
                            pop
                        except:
                            continue
                except:
                    pass

        def savebtn_active(self, event, trip_name_var):
            if event.keysym == 'BackSpace':  # reads count before button press, had to add this to count right
                length = len(trip_name_var.get()) - 1
            else:  # currently counting any button, including 'shift' as input len
                length = len(trip_name_var.get()) + 1
            if length < 2:  # set to 2 for things like 'AZ'
                self.save_btn.config(state='disabled')
            else:
                self.save_btn.config(state='active')  # doesnt hold color when activated, even if bg is plugged in here

    class TripDetailsPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None):
            Frame.__init__(self, parent)
            self.canvas = Canvas(self, borderwidth=0, height=440)
            self.frame = Frame(self.canvas)
            self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.vsb.set)
            self.vsb.grid(row=1, column=1, sticky='ns')
            self.canvas.grid(row=1, column=0)
            self.canvas.create_window((4, 4), window=self.frame, anchor="nw", tags="self.frame")
            self.frame.bind("<Configure>", self.on_frame_config)
            self.frame.bind_all("<MouseWheel>", self.on_mousewheel)


            cost_btn_config = {'height': 50, 'width': 365, 'compound': 'left', 'bd': 6,
                               'justify': 'left',
                               'anchor': 'w', 'bg': '#EEF7FB'}

            if locatorID != None:
                ######### trip Header ##########
                headcl = '#B1DEFA'
                self.headerf = Frame(self, bg=headcl)
                self.headerf.grid(row=0, column=0)
                dest_l = Label(self.headerf, text=locatorID.destination, bg=headcl, height=1, padx=20,
                               font=('arial', 22))
                dest_l.grid(row=0)
                date_l = Label(self.headerf, text='{} {}/{}'.format(locatorID.mon_date, locatorID.day_date, locatorID.year_date),
                               bg=headcl, width=50)
                date_l.grid(row=1)
                note_l = Label(self.headerf, text=locatorID.note, bg=headcl, height=3, width=50, wraplength=350)
                note_l.grid(row=2)

                budgetcl = '#F8AC39'
                self.budgetf = Frame(self.headerf, bg=budgetcl)
                self.budgetf.grid(row=3, sticky='ew')

                budget_l = Label(self.budgetf, text=('Budget: $ ' + str(locatorID.budget)), bg=budgetcl, width=17)
                budget_l.grid(row=0, column=0)

                total_l = Label(self.budgetf, text=('Total Cost: $ ' + str(locatorID.trip_total_price())), bg=budgetcl,
                                width=17)
                total_l.grid(row=0, column=1)

                compare_l = Label(self.budgetf, text=locatorID.within_budget_check(), bg=budgetcl, width=17)
                compare_l.grid(row=0, column=2)

            ######### cost buttons ##########
            if locatorID != None:
                try:  # labels by date, and lists buttons for each cost
                    first_date = (locatorID.trip_plans[0].start_date_month, locatorID.trip_plans[0].start_date_day)
                    date_config = {'fg': '#145075', 'anchor': 'w', 'width': '45', 'font': ('arial', 10)}

                    date_label = Label(self.frame, text=first_date[0]+'  '+first_date[1]+' --', **date_config)
                    date_label.grid()
                    for n, cost in enumerate(locatorID.trip_plans):
                        date = cost.start_date_month, cost.start_date_day
                        if date != first_date:
                            first_date = date
                            date_label = Label(self.frame, text=first_date[0]+'  '+first_date[1]+' --', **date_config)
                            date_label.grid()
                        try:
                            photo = PhotoImage(file=resource_path(cost.type_logo))
                        except:  # returns generic pc if trip logo cannot be called
                            photo = PhotoImage(file=resource_path('Airplane_basicsm.png'))
                        cost_button = Button(self.frame, text=cost.__str__(),
                                             command=lambda cost=cost: controller.refresh_show_frame(
                                                 EditCostPage, locatorID, cost), image=photo,  **cost_btn_config)
                        cost_button.image = photo
                        cost_button.grid()

                except IndexError:
                    no_costs_label = Label(self.frame, text="There are no costs yet for this trip.\n "
                                                            "Click 'add cost' to create a new one",
                                           font=('arial', '16'))
                    no_costs_label.grid()

            ###### Bottom Buttons #######
            self.directoryf = Frame(self, bg='#1A6493')
            self.directoryf.grid(row=3, column=0)

            cost_btn_config = {'width': 10, 'bg': '#145075', 'fg': '#D0E0EA'}

            back_btn = Button(self.directoryf, text="Back",
                              command=lambda: controller.refresh_show_frame(TripListPage), **cost_btn_config)
            back_btn.grid(row=0, column=0, padx=24, pady=10)
            edit_btn = Button(self.directoryf, text="EDIT",
                              command=lambda: controller.refresh_show_frame(EditTripPage, locatorID=locatorID),
                              **cost_btn_config)
            edit_btn.grid(row=0, column=2, padx=24, pady=10)
            add_btn = Button(self.directoryf, text="ADD COST",  # pop up asks what kind of cost
                             command=lambda: popup_costtype(controller, 'pick a cost', locatorID), **cost_btn_config)
            add_btn.grid(row=0, column=1, padx=24, pady=10)

        ######### functions #########
        def on_mousewheel(self, event):
            self.canvas.yview_scroll(-1 * int(event.delta / 60), "units")

        def on_frame_config(self, event):
            '''Reset the scroll region to encompass the inner frame'''
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    class EditCostPage(Frame):
        def __init__(self, parent, controller, locatorID=None, costID=None, conf=None):
            Frame.__init__(self, parent)
            self.canvas = Canvas(self, borderwidth=0, height=545)
            self.frame = Frame(self.canvas)
            self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
            self.canvas.configure(yscrollcommand=self.vsb.set)
            self.vsb.grid(row=1, column=1, sticky='ns')
            self.canvas.grid(row=1, column=0)
            self.canvas.create_window((10, 4), window=self.frame, anchor="nw", tags="self.frame")
            self.frame.bind("<Configure>", self.on_frame_config)
            self.frame.bind_all("<MouseWheel>", self.on_mousewheel)

            if costID in ('Transportation', 'Lodging', 'Event', 'Meal', 'Merchandise', 'Fee'):
                temp_obj = ReservedCost(type=costID)
                costID = temp_obj
            try:
                type = costID.type
            except AttributeError:
                type = costID

            ######### trip Header ##########
            headcl = '#B1DEFA'
            self.headerf = Frame(self)
            self.headerf.grid(row=0, column=0)

            label = Label(self.headerf, text="Edit cost information below", bg=headcl, height=1, width=42,
                          font=('arial',
                                13))  # todo: change width to a math func that checks frame size and fills in the diff from the text
            label.grid(row=0, column=0)

            # #######################labels and entry fields ################################
            med_font = ('arial', 14)
            detail_lbl_config = {'font': ('arial', 12), 'fg': '#326DA8', 'padx': 2, 'anchor': 'w', 'width': 36,
                                 'height': 2}
            detail_entry_config = {'font': ('arial', 14), 'fg': 'black', 'bd': 2, 'width': 30, 'insertwidth': 2}
            sub_type = StringVar()
            type = type
            price = StringVar()
            pay_method = StringVar()
            start_date = DateEntry(self.frame)  # todo: doesnt take focus when tabbing down page
            end_date = DateEntry(self.frame)
            company = StringVar()
            conf = StringVar()
            pointa = StringVar()
            pointb = StringVar()
            start_time = StringVar()
            end_time = StringVar()

            # if costID is not None:
            cost_types_dict = {  # CostType{Cost Detail:[label string, text variable]}
                    'Fee': {'type': ['Type', type, ''],
                            'sub_type': ['Fee Type', sub_type, ''],
                            'price': ['Price', price, ''],
                            'pay_method': ['Payment Method', pay_method, ''],
                            'start_date': ['Date', start_date, ''],
                            'end_date': [0, end_date, ''],
                            'company': ['Company', company, ''],
                            'conf_num': [0, conf, ''],
                            'point_a': [0, pointa, ''],
                            'point_b': [0, pointb, ''],
                            'start_time': [0, start_time, ''],
                            'end_time': [0, end_time, ''],
                            'misc': ['Note', '', '']
                            },
                    'Merchandise': {'type': ['Type', type, ''],
                                    'sub_type': ['Type of Merchandise', sub_type, ''],
                                    'price': ['Price', price, ''],
                                    'pay_method': ['Payment Method', pay_method, ''],
                                    'start_date': ['Date', start_date, ''],
                                    'end_date': [0, end_date, ''],
                                    'company': ['Store', company, ''],
                                    'conf_num': [0, conf, ''],
                                    'point_a': [0, pointa, ''],
                                    'point_b': [0, pointb, ''],
                                    'start_time': [0, start_time, ''],
                                    'end_time': [0, end_time, ''],
                                    'misc': ['Note', '', '']
                                    },
                    'Meal': {'type': ['Type', type, ''],
                             'sub_type': ['Meal Type', sub_type, ''],
                             'price': ['Price', price, ''],
                             'pay_method': ['Payment Method', pay_method, ''],
                             'start_date': ['Date', start_date, ''],
                             'end_date': [0, end_date, ''],
                             'company': ['Restaurant', company, ''],
                             'conf_num': [0, conf, ''],
                             'point_a': [0, pointa, ''],
                             'point_b': [0, pointb, ''],
                             'start_time': [0, start_time, ''],
                             'end_time': [0, end_time, ''],
                             'misc': ['Note', '', '']
                             },
                    'Transportation': {'type': ['Type', type, ''],
                                       'sub_type': ['Transport Type', sub_type, ''],
                                       'price': ['Cost', price, ''],
                                       'pay_method': ['Payment Method', pay_method, ''],
                                       'start_date': ['Departure Date', start_date, ''],
                                       'end_date': ['Arrival Date', end_date, ''],
                                       'company': ['Company', company, ''],
                                       'conf_num': ['Confirmation #', conf, ''],
                                       'point_a': ["Departure Location", pointa, ''],
                                       'point_b': ["Arrival Location", pointb, ''],
                                       'start_time': ["Departure Time", start_time, ''],
                                       'end_time': ["Arrival Time", end_time, ''],
                                       'misc': ['Notes', '', '']
                                       },
                    'Lodging': {'type': ['Type', type, ''],
                                'sub_type': ['Lodging Type', sub_type, ''],
                                'price': ['Cost', price, ''],
                                'pay_method': ['Payment Method', pay_method, ''],
                                'start_date': ['Check-in Date', start_date, ''],
                                'end_date': ['Check-out Date', end_date, ''],
                                'company': ['Company', company, ''],
                                'conf_num': ["Confirmation #", conf, ''],
                                'point_a': ["Location", pointa, ''],
                                'point_b': [0, pointb, ''],
                                'start_time': ["Check-in Time", start_time, ''],
                                'end_time': ['Check-out Time', end_time, ''],
                                'misc': ['Note', '', '']
                                },
                    'Event': {'type': ['Type', type, ''],
                              'sub_type': ['Event Type', sub_type, ''],
                              'price': ['Price', price, ''],
                              'pay_method': ['Payment Method', pay_method, ''],
                              'start_date': ['Date', start_date, ''],
                              'end_date': [0, end_date, ''],
                              'company': ['Company', company, ''],
                              'conf_num': ['Confirmation #', conf, ''],
                              'point_a': ['Location', pointa, ''],
                              'point_b': [0, pointb, ''],
                              'start_time': ["Start Time", start_time, ''],
                              'end_time': [0, end_time, ''],
                              'misc': ['Note', '', '']
                              }
                }

            for cost in cost_types_dict:  # selects cost detail dictionary by cost type
                if type == cost:
                    single_cost_dict = cost_types_dict[cost]
                else:
                    single_cost_dict = None

                if locatorID is not None:
                    try:  # provides data or blanks to be inserted on cost page or new page
                        entry_inserts_dict = {'type': costID.type,
                                              'sub_type': costID.sub_type,
                                              'price': costID.price,
                                              'pay_method': costID.pay_method,
                                              'start_date': (costID.start_date_month, costID.start_date_day, costID.start_date_year),
                                              'end_date': (costID.end_date_month, costID.end_date_day, costID.end_date_year),
                                              'company': costID.company,
                                              'conf_num': costID.conf,
                                              'point_a': costID.pointa,
                                              'point_b': costID.pointb,
                                              'start_time': costID.start_time,
                                              'end_time': costID.end_time,
                                              'misc': costID.misc
                                              }
                    except AttributeError:
                        entry_inserts_dict = {'type': '',
                                              'sub_type': '',
                                              'price': '',
                                              'pay_method': '',
                                              'start_date': (locatorID.mon_date, locatorID.day_date, locatorID.year_date),
                                              'end_date': ('','',''),
                                              'company': '',
                                              'conf_num': '',
                                              'point_a': '',
                                              'point_b': '',
                                              'start_time': '',
                                              'end_time': '',
                                              'misc': ''
                                              }


                if single_cost_dict is not None:  # assigns placement of entry fields
                    row = 2
                    for n, label_key in enumerate(single_cost_dict):
                        if single_cost_dict[label_key][0]:
                            if label_key == 'type':
                                label = Label(self.frame, text=type, **detail_lbl_config)
                                label.grid(row=row, sticky="E")
                                button = Button(self.frame, text="Change Cost Type",
                                                command=lambda: [costID.edit_cost(type=type,
                                                                                  price=price.get(),
                                                                                  pay_method=pay_method.get(),
                                                                                  pointa=pointa.get(),
                                                                                  start_date_month=start_date.mon_date.get(),
                                                                                  start_date_day=start_date.day_date.get(),
                                                                                  start_date_year=start_date.year_date.get(),
                                                                                  start_time=start_time.get(),
                                                                                  pointb=pointb.get(),
                                                                                  end_date_month=end_date.mon_date.get(),
                                                                                  end_date_day=end_date.day_date.get(),
                                                                                  end_date_year=end_date.year_date.get(),
                                                                                  end_time=end_time.get(),
                                                                                  sub_type=sub_type.get(),
                                                                                  conf=conf.get(),
                                                                                  company=company.get(),
                                                                                  misc=misc_entry.get("1.0", 'end-1c')),
                                                                 popup_change_costtype(controller, locatorID, costID)])
                                button.grid(row=row + 1, )
                            else:
                                label = Label(self.frame, text=single_cost_dict[label_key][0], **detail_lbl_config)
                                label.grid(row=row, sticky="E")

                                if label_key == 'start_date' or label_key == 'end_date':  # creates date field instead of text entry
                                    single_cost_dict[label_key][1].grid(row=row + 1, sticky="W")
                                    single_cost_dict[label_key][1].mon_date_entry.insert(0, entry_inserts_dict[label_key][0])
                                    single_cost_dict[label_key][1].day_date_entry.insert(0, entry_inserts_dict[label_key][1])
                                    single_cost_dict[label_key][1].year_date_entry.insert(0, entry_inserts_dict[label_key][2])

                                elif label_key == 'misc':
                                    misc_entry = Text(self.frame, height=8, **detail_entry_config)
                                    misc_entry.grid(row=row + 1)
                                    misc_entry.insert(END, str(entry_inserts_dict[label_key]))

                                else:  # creates basic text entry
                                    entry = Entry(self.frame, textvariable=single_cost_dict[label_key][1], **detail_entry_config)
                                    entry.grid(row=row + 1)
                                    if costID != None:  # populates entry fields with pre-existing data
                                        entry.insert(0, str(entry_inserts_dict[label_key]))

                        elif single_cost_dict[label_key][0] == 0:
                            # for erasing unused data if present, so when saved won't be hiding in the background.
                            entry_inserts_dict[label_key] = None
                        row += 2

            ###### Bottom Buttons #######
            self.directoryf = Frame(self, bg='#1A6493')
            self.directoryf.grid(row=2, column=0)

            cost_btn_config = {'width': 10, 'bg': '#145075', 'fg': '#D0E0EA'}

            cancel_btn = Button(self.directoryf, text="Cancel",
                                command=lambda: controller.refresh_show_frame(TripDetailsPage, locatorID=locatorID),
                                **cost_btn_config)
            cancel_btn.grid(row=0, column=0, padx=24, pady=10)

            edit_btn = Button(self.directoryf, text="Save",
                              command=lambda: controller.refresh_show_frame(TripDetailsPage,
                                                                            save_cost(locatorID, costID, type=type,
                                                                                      price=price.get(),
                                                                                      pay_method=pay_method.get(),
                                                                                      pointa=pointa.get(),
                                                                                      start_date_month=start_date.mon_date.get(),
                                                                                      start_date_day=start_date.day_date.get(),
                                                                                      start_date_year=start_date.year_date.get(),
                                                                                      start_time=start_time.get(),
                                                                                      pointb=pointb.get(),
                                                                                      end_date_month=end_date.mon_date.get(),
                                                                                      end_date_day=end_date.day_date.get(),
                                                                                      end_date_year=end_date.year_date.get(),
                                                                                      end_time=end_time.get(),
                                                                                      sub_type=sub_type.get(),
                                                                                      conf=conf.get(),
                                                                                      company=company.get(),
                                                                                      misc=misc_entry.get("1.0",
                                                                                                          'end-1c'))),
                              **cost_btn_config)
            edit_btn.grid(row=0, column=1, padx=24, pady=10)

            if locatorID != None:
                del_btn = Button(self.directoryf, text="DELETE COST",
                                 command=lambda: popup_dlt_cost_conf(controller, vacations, locatorID, costID),
                                 **cost_btn_config)
                del_btn.grid(row=0, column=2, padx=24, pady=10)

        def on_mousewheel(self, event):
            self.canvas.yview_scroll(-1 * int(event.delta / 60), "units")

        def on_frame_config(self, event):
            self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    global vacations  # only need because gui is inside main() and functions arent, can probably merge all later
    vacations = new_or_edit(filename)
    root = TravelApp()
    root.wm_title("Travel App")
    root.geometry('400x620+600+20')  # window size+ screen placement
    root.mainloop()


if __name__ == '__main__':
    main()
##############################################################################


# TODO: build tests to automate and check when i make changes
# TODO: possibly switch over to database not pkl file

# TODO:should be an add in field to add category to any charge... might be unnecessarily difficult. prob not do.
# TODO:have a add lodging to transportation button for things like cruises. just for future tracking
# TODO:add sort for cost by cost type, maybe add a buisinees/personal field,day

# todo: add end date for trip and logic for check if lodging covered
            # add a tracker for cost type per day
            # add like calendar that tells what is missing from each day. (hidden)
            # ?seperate screen or header bar that tells what is vital and missing when planning? like lodging

# todo: add in real time and hide past events under seperate tab.

### todo: add sort categories for pricing: costtype, personal/business, date, payment method

## commit:added icons for each charge category
