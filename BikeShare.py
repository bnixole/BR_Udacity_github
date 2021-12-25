import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def Pull_location():
    """
    Asks user to specify a city
    Returns:
        (str) city - name of the city to analyze
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower not in ['new york', 'chicago', 'washington']:
            city = input('Which city data would you like to explore, New York, Chicago or Washington? \n')
            if city.lower() == 'new york':
                return 'new york city'
            elif city.lower() == 'chicago':
                return 'chicago'
            elif city.lower() == 'washington':
                return 'washington'
            else:
                print('Maybe you made a typo. Please enter try again\n')
    return city
    
def get_filter():

    """Prompt filter type
    Returns:
        (str) filter - prefered method to filter by 
    """
    filter = ''
    while filter.lower() not in ['day', 'month', 'none']:
        filter = input('Would you like to filter the data by month, day, or not at all? Type \'none\' for no filter\n')
        if filter.lower() not in ['day', 'month', 'none']:
            print('Maybe you made a typo. Please try again\n')
    return filter
    
def get_month():

    """
    Asks users who want to filter by month the enter a month 
    Returns:
        (str) month
    """
    # Get user input for month (none, january, february, ... , june)
    month = ""
    month_dict = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
    while month.lower() not in month_dict.keys():
        month = input('\nWhich months data are you interested in seeing - January, February, March, April, May, or June?\n')
        if month.lower() not in month_dict.keys():
            print('Maybe you made a typo. Try again\n')
    month = month_dict[month.lower()]
    return month

def get_day():
    """
    Asks users who want to filter by month the enter a month 
    Returns:
        (str) day
    """
    #get user input for day of week (none,monday,tuesday....sunday)
    day = ""
    day_dict = {'m': 'Monday', 't': 'Tuesday', 'w': 'Wednesday', 'th': 'Thursday', 'f': 'Friday', 'sa': 'Saturday', 's': 'Sunday'}
    while day.lower() not in day_dict.keys():
        day = input('Which day would you like to see - M, T, W, Th, F, Sa, S\n')
        if day.lower() not in day_dict.keys():
            print('It seems there may be a typo. Please try again\n')
    day = day_dict[day.lower()]
    return day
   

 
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month in the data set
    
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    value = int(df['Start Time'].dt.month.mode())
    p_month = months[value - 1]
    print('\nThe most popular month for traveling is {}'.format(p_month))


    # Display the most common day of week
    day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    value = int(df['Start Time'].dt.dayofweek.mode())
    p_day = day[value]
    print('\nThe most popular day for traveling is {}'.format(p_day))

    #display the most common start hour
    value = int(df['Start Time'].dt.hour.mode())
    print('\nThe most popular hour to begin traveling (in 24-hour format) is {}'.format(value))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    value_start = df['Start Station'].mode().to_string(index = False)
    print('\nThe most commonly used start station is {}'.format(value_start))

    # display most commonly used return station
    value_end = df['End Station'].mode().to_string(index = False)
    print('\nThe most commonly used end station is {}'.format(value_end))

    # Display most frequent combination of start station and end station trip
    #create a value to match start/stops
    df['trip'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    value = df['trip'].mode().to_string(index = False)
    print('\nThe most frequent combination of start station and end station is {}'.format(value))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)   
    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_time = df['Trip Duration'].sum()
    mins, sec = divmod(total_time, 60)
    hour, mins = divmod(mins, 60)
    print('The total travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))

    #  display mean travel time
    avg_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(avg_time, 60)
    #if mins > 60:
    hour, mins = divmod(mins, 60)
    print('The mean travel time is {} hours {} minutes and {} seconds'.format(hour, mins, sec))
 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #  Display counts of user types
    sub = (df['User Type'] == 'Subscriber').sum()
    cust = (df['User Type'] == 'Customer').sum()
    print('\nThe count of subscriber is {} and Customer is {}'.format(sub, cust))

    us = df['User Type'].value_counts()
    print(us)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def year_stats(df):
    start_time = time.time()
    # display counts of gender
    male = (df['Gender'] == 'Male').sum()
    female = (df['Gender'] == 'Female').sum()
    print('\nThe count of males is {} and females is {}'.format(male, female))


    # Display earliest, most recent, and most common year of birth
    dob_early = int(df['Birth Year'].min())
    dob_recent = int(df['Birth Year'].max())
    dob_common = int(df['Birth Year'].mode())
    print('\nThe earliest year of birth is {}'.format(dob_early))
    print('\nThe most recent year of birth is {}'.format(dob_recent))
    print('\nThe most common year of birth is {}'.format(dob_common))
   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    '''Prompt user regarding raw data
       Return 5 lines of data at a time
    '''
    start=0
    end=5
    while True:
        reply=['yes','no']
        choice= input("\nWould you like to view individual trip data? Type 'yes' or 'no'")
        if choice.lower() in reply:
            if choice=='yes':
                data = df.iloc[start:end]
                print(data)
            break     
        else:
            print("Please chose yes or no")
    if  choice == 'yes':       
            while True:
                moredata= input("\nDo you want to view more trip data? Type 'yes' or 'no'")
                if moredata.lower() in reply:
                    if moredata=='yes':
                        start+=5
                        end+=5
                        data = df.iloc[start:end]
                        print(data)
                    else:    
                        break  
                else:
                    print("Please chose yes or no")              


    
    
    
def main():
    while True:
        city = Pull_location()
        df = pd.read_csv(CITY_DATA[city], parse_dates = ['Start Time', 'End Time'])

        df['Start Time'] = pd.to_datetime(df['Start Time'])

        filters = get_filter()
        
        if filters == 'month':
            month = get_month()
            df['month'] = df['Start Time'].dt.month
            df = df[df['month'] == month]
        elif filters == 'day':
            day = get_day()
            df['day'] = df['Start Time'].dt.weekday_name
            df = df[df['day'] == day]

     
        if filters == 'none':
            time_stats(df)


        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        if city == 'chicago' or city == 'new york':
            year_stats(df)
        
        if city == 'washington':
            print('\nNo data available')
            
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()