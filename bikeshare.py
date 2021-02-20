import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    """
    print("Hello let's explore US bike share data ")
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    selected_city = input("Choose one of the following cities : Chicago, New York city, or Washington  \n").lower()
    # To make sure the entries are correct
    while (selected_city != "chicago" and selected_city != "new york city" and selected_city != "washington"):
        selected_city = input(
            "please agin enter one of the following cities :Chicago, New York city, or Washington  \n").lower()

        # TO DO: get user input for month (all, january, february, ... , june)
    selected_month = input("choose any month you want : January, February, March, April, May, June, or all?\n").lower()
    # To make sure the entries are correct
    while (
            selected_month != 'all' and selected_month != 'january' and selected_month != 'february' and selected_month != 'march' and selected_month != 'april' and selected_month != 'may' and selected_month != 'june'):
        selected_month = input(
            "please agin enter any month you want : January, February, March, April, May, June, or all?\n").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    selected_day = input(
        "choose any day of the week you want : Monday, Tuesday,Wednesday, Thursday ,Friday ,Saturday or Sunday \n").lower()
    #  TO make sure the entries are correct  
    while (
            selected_day != 'all' and selected_day != 'monday' and selected_day != 'tuesday' and selected_day != 'wednesday' and selected_day != 'thursday' and selected_day != 'friday' and selected_day != 'saturday' and selected_day != 'sunday'):
        selected_day = input(
            "please agin enter any day you want :Monday, Tuesday,Wednesday, Thursday ,Friday ,Saturday , Sunday or all?\n").lower()

    print('-' * 40)
    return selected_city, selected_month, selected_day


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
    # convert the start date time to  date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month
        df = df[df['month'] == month]

    # filter by day 
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("Most Popular Month: " + str(popular_month))

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("Most Popular day: " + popular_day)

    # TO DO: display the most common start hour
    popular_common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', popular_common_start_hour)

    print("\n This took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most End Station:', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    popularCombination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('\nThe most frequent combination of start station and end station trip: ', popularCombination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\n Calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time from the given filtered data is: " + str(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time from the given fitered data is: " + str(mean_travel_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('User Type Stats:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # TO DO: Display counts of gender
        print('Gender Stats:')
        print(df['Gender'].value_counts())

        # TO DO: Display earliest, most recent, and most common year of birth
        print('Birth Year Stats:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year:', most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year:', most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year:', earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw(df):
    # request user to display numbers of row  data
    print(df.head())
    next_row = 0
    while True:
        view_row = input("\nWould you like to view next five row of raw data? Enter yes or no.\n")
        if view_row.lower() != "yes":
            return
            next_row = next_row + 5
        print(df.iloc[next_row:next_row + 5])


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        user_stats(df, city)
        while True:
            viewRow = input('\nWould you like to view first five row of raw data? Enter yes or no.\n')
            if viewRow.lower() != 'yes':
                break
            display_raw(df)
            break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
