import time
import pandas as pd
import numpy as np
import datetime
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    
    while city is None :
        incity = input("Enter city name (chicago, new york city, washington): ").lower()
        if incity.lower() in ['chicago', 'new york city', 'washington'] :
                       city = incity

    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
                       
    while month is None:
       inmonth=input("Enter month  (all, january, february, ... , december): ").lower()     
       if inmonth.lower() in ['all','january', 'february','march','april','may','june','july','august','september','october','november','december']:
                     month=inmonth
                       

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=None
    while day is None:
        inday=input("Enter day of week (all, monday, tuesday, ... sunday): ").lower()
        if inday in ['all', 'monday', 'tuesday','wednesday','thursday','friday','saturday','sunday']:
            day=inday
        
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(city.replace(' ','_')+'.csv')
        
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    filter =  [month == 'all' or tt.strftime('%b').lower() == month[:3] for tt in df['Start Time']]
    df['mn'] = filter    
    
    df['dt'] = [day == 'all' or  calendar.day_name[ tt.weekday()].lower() == day.lower() for tt in df['Start Time']]  
    
    dfmn = df[df['mn'] == True ]
    
    dfdt = dfmn[dfmn['dt']==True]
    
    return dfdt

def max_from_dict(dt):
    """Returns key with max value"""
    maxValue = None
    
    
    cnts = list(dt.values())
    cnts.sort(reverse=True)
    max = cnts[0]
    
    for k,v in dt.items():
        if v == max:
            maxValue = k
    
    return maxValue
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if len(df) == 0:
        print("=====> Recheck filter, no records found...")
    else:
        # TO DO: display the most common month
        mths=dict()

        wdays = dict()
        shr = dict()
        

        for lbl, i in df.iterrows():
            tt =i[1]
            mtname = tt.strftime('%b')
            mths[mtname] = mths.get(mtname,0) +1   
            wod = calendar.day_name[ tt.weekday()]
            wdays[wod] = wdays.get(wod,0)+1
            hr = str(tt.hour)
            shr[hr] = shr.get(hr,0)+1
        
        print("\nMost common month is : {}\n".format(max_from_dict(mths)))

        # TO DO: display the most common day of week

        print("\nMost common day of week is : {}\n".format(max_from_dict(wdays)))

        # TO DO: display the most common start hour
        print("\nMost common start hour is : {}\n".format(max_from_dict(shr)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    if len(df) == 0:
        print("=====> Recheck filter, no records found...")
    else:

        ss = dict()
        es = dict()
        ses = dict()

        for lbl, i in df.iterrows():
            #print(i[4])
            start_station = i[4]
            ss[start_station] = ss.get(start_station,0) + 1
            end_station=i[5]
            es[end_station] = es.get(end_station,0) +1
            start_end_station = i[4] + i[5]
            ses[start_end_station] = ses.get(start_end_station,0)+1

        # TO DO: display most commonly used start station

        print("\nMost commonly used start station is : {}\n".format(max_from_dict(ss)))

        # TO DO: display most commonly used end station
        print("\nMost commonly used end station is : {}\n".format(max_from_dict(es)))

        # TO DO: display most frequent combination of start station and end station trip
        print("\nMost frequent combination of start station and end station trip is : {}\n".format(max_from_dict(ses)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""   
    
    
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    if len(df) == 0:
        print("=====> Recheck filter, no records found...")
    else:
    
    
        tt=datetime.timedelta(0)

        # TO DO: display total travel time
        for lbl, i in df.iterrows():
            st = i[1]
            et = i[2]        
            tt+=et-st

        print("\nTotal travel time is: {}".format(tt))

        # TO DO: display mean travel time
        print("\nMean travel time is : {}\n".format(datetime.timedelta(df.mean()[1])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    if len(df) == 0:
        print("=====> Recheck filter, no records found...")
    else:

        # TO DO: Display counts of user types

        ut = dict()
        gd=dict()
        byd=dict()
        for lbl, i in df.iterrows():
            typ = i[6]
            ut[typ] = ut.get(typ,0)+1
            gd[i[7]] = gd.get(i[7],0)+1
            bd = str(i[8])
            if bd != str(float('nan')) :
                byd[bd] = byd.get(bd,0)+1

        print("Counts for user types are as follows:")
        for k,v in ut.items():
            print("{} : {}".format(k,v))

        # TO DO: Display counts of gender
        print("\nCounts for gender types are as follows:")
        for k,v in gd.items():
            print("{} : {}".format(k,v))

        # TO DO: Display earliest, most recent, and most common year of birth
        print("\nEarliest year of birth is: {}".format(df['Birth Year'].min()))
        print("\nMost recent year of birth is: {}".format(df['Birth Year'].max()))
        print("\nMost common year of birth is: {}".format(max_from_dict(byd)))
   
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
    
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
