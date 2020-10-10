import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
                                            or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
                                            or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington).
    # HINT: Use a while loop to handle invalid inputs
    city = input("Please specify a city to analyze: ")


    while(city.lower() not in CITY_DATA.keys()):

        for city_name in CITY_DATA.keys():
            if(city.lower().startswith(city_name[0])):
                answer=input("Did you mean "+city_name+": ")
                if(answer.lower().startswith('y')):
                    city=city_name
                    break

        if(city.lower() not in CITY_DATA.keys()):
            city = input("""Please, enter a correct city
                    (chicago, new york city, washington): """)


    allowed_months=["all", "january", "february",
                    "march", "april", "may", "june"]
    # get user input for month (all, january, february, ... , june)
    month = input("Please specify a month to analyze:")
    while(month.lower() not in allowed_months):
        for month_name in allowed_months:
            if(month.lower().startswith(month_name[0])):
                answer=input("Did you mean %s: "%month_name)
                if(answer.lower().startswith('y')):
                    month=month_name
                    break

        if(month.lower() not in allowed_months):
            month = input("""Please, enter a correct month
                (all, january, february, ... , june): """)

    # get user input for day of week (all, monday, tuesday, ... sunday)
    #allowed_days = map(str, range(8))
    # ("all":0, "monday":2, "tuesday","wednesday", "thursday",
    # "friday", "saturday", "sunday")

    allowed_days = ["all", "monday", "tuesday","wednesday", "thursday",
                                "friday", "saturday", "sunday"]

    day = input("Please specify a day to analyze: ")
    #print(allowed_days)
    while(day.lower() not in allowed_days):
        for day_name in allowed_days:
            if(day.lower().startswith(day_name[0])):
                answer=input("Did you mean %s: "%day_name)
                if(answer.lower().startswith('y')):
                    day=day_name
                    break

        if(day.lower() not in allowed_days):
            day = input("""Please specify a day to analyze,
                                    (all, saturday...): """)

    print('-'*40)
    return city.lower(), month.lower(), day.lower()


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by,
                                            or "all" to apply no month filter
        (str) day - name of the day of week to filter by,
                                            or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

	# To make sure that the inputs in lower case and type string
	# in case if the function is used in another program.

    if(type(city) != str):
        print("City should be the name of the city (String)")
        sys.exit()
    if(type(month) is not str):
    	print("Month should be the name of the month (String)")
    	sys.exit()
    if(type(day) is not str):
    	print("Day should be the name of the day (String)")
    	sys.exit()

    #print(type(city),type(month),type(day))
    city=city.lower()
    month=month.lower()
    day=day.lower()

    df=pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['year'] = df['Start Time'].dt.year
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day

    df['hour'] = df['Start Time'].dt.hour
    df['minute'] = df['Start Time'].dt.minute
    df['second'] = df['Start Time'].dt.second

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if(month!='all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month']==month]
    if(day!="all"):
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    #df['Start Time'] = pd.to_datetime(df['Start Time'])
    #print(type(pd.to_datetime(df['Start Time'])))

    # extract hour from the Start Time column to create an hour column

    print("The most common  month are:")
    # display the most common month
    print(df['month'].mode()[0])

    print("The most common day")
    # display the most common day of week
    print(df['day_of_week'].mode()[0])

    print("The most common hour")
    # display the most common start hour
    print(df['hour'].mode()[0],"Counts",df['hour'].value_counts().max())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station and how many counts
    print("The most common start station is:")
    print(df["Start Station"].mode()[0],"Count:",
                                    df["Start Station"].value_counts().max())

    # display most commonly used end station and how many counts
    print("The most common end station is:")
    print(df["End Station"].mode()[0],"Count:",
                                    df["End Station"].value_counts().max())

    # display most frequent combination of start station and end station trip

    print("The most common start and end station is:")
    d=df.copy()
    d=df.groupby("Start Station")
    print(d["End Station"].value_counts().idxmax(),"Count:",
                                    d["End Station"].value_counts().max())
    #most_freq_station_comb = df['Start Station'] + ' to ' + df['End Station']
    #print('The most frequnt combination of start station and end station trip was {}'.format(most_freq_station_comb.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("The total travel time is:")
    print(df["Trip Duration"].sum(),"Count:",df["Trip Duration"].count())

    # display mean travel time
    print("The average travel time is:")
    print(df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    try:
        print(df["User Type"].value_counts())
    except KeyError:
        print("No user type data to share")

    # Display counts of gender
    try:
        print(df["Gender"].value_counts())
    except KeyError:
        print("No gener data to share")

    # Display earliest, most recent, and most common year of birth
    try:
        print("The most common year Birth year is",
                df["Birth Year"].mode()[0],
                " and counted ",
                df["Birth Year"].value_counts().max())
        print("The oldest one who used the bike is",df["Birth Year"].min())
        print("The youngest one who used the bike is",df["Birth Year"].max())
    except KeyError:
        print("No birth year data to share")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ Display the raw data for the city"""

    raw_data = input("Would you like to see the raw data: ")
    # Copy data to not change the orignal
    d=df.copy()
    c=0
    while(raw_data.lower().startswith('y')):
        start=input("What is the row do you want to start with: ")
        while(not start.isnumeric()):
            start=input("Please, enter a number: ")
        start=int(start)

        how_many=input("How many row do you want to see: ")
        while(not how_many.isnumeric()):
            how_many=input("Please, enter a number: ")
        how_many=int(how_many)

        print(d[start:start+how_many])
        #print(d.head())
        raw_data = input("Would you like to see the next raw data: ")



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
