#!/usr/bin/env python
# coding: utf-8

# In[2]:


import time
import pandas as pd
import numpy as np

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
    
    citylist = ['chicago', 'new york city', 'washington']
    while True:
        city =  input("Which city would you like to get data for? \n Chicago, New York City or Washington?: ").lower() # get and process input for a list of names
        print(city)
        if city not in citylist:
            print('{} not available, please use  Chicago, New York City or Washington'.format(city))
            continue
        else:
            print('You choose to look on the data for {}'.format(city))
            break 
        
    
    # TO DO: get user input for month (all, january, february, ... , june)
    monthlist = ['january','february','march','april','may','june','all']
    while True:
        month =  input("Name one of the month from January to June you want to filter by, or all to apply no month filter: ").lower() # get and process input for a list of the number of assignments
        if month not in monthlist:
            print(' {} Your choosen month is not available, please use different month between January and June'.format(city))
        else:
            break 
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    daylist = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday",'all']
    while True:
    
        day =  input("name of the day of week to filter by, or all to apply no day filter: ").lower() # get and process input for a list of grades
        if day not in daylist:
            print('Your choosen day is not available, please use a day between monday and sunday')
        else:
            break 
    

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
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    p_month = df['month'].mode()[0]
    
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    p_day = df['day'].mode()[0]
       # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    p_hour = df['hour'].mode()[0]
        
    #print(df)   
    print('Most common month: {} \nMost common day: {} \nMost common starting hour: {} '.format(p_month,p_day,p_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    mc_start = df['Start Station'].mode()[0]    

    # TO DO: display most commonly used end station
    mc_end = df['End Station'].mode()[0]

    # TO DO: display most frequent combination of start station and end station trip
    combi = df.groupby(['Start Station','End Station']).size().nlargest(1)
    
    print('Most commen start: {} \nMost common end: {} \nMost frequent combination: {} \n'.format(mc_start,mc_end,combi))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    ttt = df['Trip Duration'].sum()

    # TO DO: display mean travel time
    tmt = df['Trip Duration'].mean()
    
    print('Total Trip Duration: {} \nMean of travel time: {} '.format(ttt,tmt))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        user_gender(df)
      
  
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        user_birth(df)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_gender(df):

    gender_counts = df.groupby(['Gender']).size()
    print(gender_counts)
    
def user_birth(df):
    birth_year = df['Birth Year']
    birth_min = df['Birth Year'].min()
    birth_max = df['Birth Year'].max()
    birth_common = df['Birth Year'].mode()[0]
    print('Most recent birthyear {} \nEarliest birth year: {} \nMost common: {} \n'.format(birth_max,birth_min,birth_common))

    
def raw_data(df):
 
    anfangs_loc = 0
    List = ['yes','no']
    
    while True:
        anzeigen = input('Great!\nDo you want to see the raw data? please input yes or no?').lower()
        if anzeigen not in List:
            print('Sorry, not sure what {} means, please enter only yes or no'.format(anzeigen))
            continue
        elif anzeigen == 'yes':
            print(df.iloc[anfangs_loc:anfangs_loc+5])
            anfangs_loc += 5
        else:
            break
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks for analyzing data, have nice day')
            break


if __name__ == "__main__":
	main()

