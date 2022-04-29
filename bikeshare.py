import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv',"new york":'new_york_city.csv',
              'nyc': 'new_york_city.csv',"chi":'chicago.csv',"wa":'washington.csv'}
# to improve the case insensitivity by adding all probable typos and inputs from the user and add the abbreviations of this cities too !
#I preferred to to use global scope to avoid any reptations and errors
months = ['january', 'february', 'march', 'april', 'may', 'june']


days=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
filter_choices=["day","month","none","both"]
user_answer_list=["yes","no"]   

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        
            city=input("Would you like to see data for Chicago(chi), New York(nyc), or Washington(wa)?").lower()  #I used lower() to to improve the case insensitivity
            if city not in CITY_DATA  :
                print("please choose a valid city and make sure that you type them correctly")
            else:
                break 
        
    
    #applying time filter regard to month or day or both of them or none of them       
    while True :
        time_filter=input("Would you like to filter the data by month, day, or both or none?").lower()  #I used lower() to to improve the case insensitivity
        if time_filter not in filter_choices :
            print("please type word from that list: (day,month,none,both) ")
        else:
            break    
             
        
            
    if time_filter=="month" or time_filter=="both":
     while True:
            month=input("please enter a month in range(january-june) :").lower()  #I used lower() to to improve the case insensitivity
            if  month not in months :
                print("please enter a valid month ")
            else:
                break  
    else:
        month="all"            
      
   
        
    if time_filter=="both" or time_filter=="day":   
     while True:
            day=input("please enter the day name :").title()  #I used title() to to improve the case insensitivity
            if day not in days:
                print("please enter a valid day name")
            else:
                 break    
    else:
        day="all"       
           

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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])    #converting to datetime

    #creating month column
    df["month"]=df["Start Time"].dt.month
    
    
    #creating day column
    df["day"]=df["Start Time"].dt.day_name()   #I am using a recent version of panda so I used day_name() if It didn't work use dt.weekday_name 
    #creating hour colume 
    df["hour"]=df["Start Time"].dt.hour
    #creating most common trips column 
    df["most common trips "]= df["Start Station"]+ " to "+df["End Station"]

    if month != 'all':
        # use the index of the months list to get the corresponding int
        
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day name if applicable
    if day != 'all':
        # filter by day name to create the new dataframe
        df = df[df['day'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    

    # display the most common month
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_common_month=df["month"].value_counts().idxmax() 
    print(" the most common month is:",most_common_month)

    # display the most common day of week
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_common_day=df["day"].value_counts().idxmax()
    print(" the most common day is:",most_common_day)
    
    # display the most common start hour
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_common_start_hour=df["hour"].value_counts().idxmax()
    print("the most common start hour is:",most_common_start_hour)
       




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_commonly_used_start_station=df["Start Station"].value_counts().idxmax()
    print("most commonly used start station:",most_commonly_used_start_station)


    # display most commonly used end station
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_commonly_used_end_station=df["End Station"].value_counts().idxmax()

    print("most commonly used end station:",most_commonly_used_end_station)


    # display most frequent combination of start station and end station trip
    #I used value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
    most_common_trip=df["most common trips "].value_counts().idxmax()
    print("most frequent combination of start station and end station trip is:", most_common_trip )
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df["Trip Duration"].sum() 
    total_travel_time_in_hours=total_travel_time/3600  #convert from seconds to hours
    print("total_travel_time_in_ :",total_travel_time_in_hours," hour")



    # display mean travel time
    mean_travel_time=df["Trip Duration"].mean()
    mean_travel_time_in_hours=mean_travel_time/3600 #convert from seconds to hours
    print("mean_travel_time :", mean_travel_time_in_hours," hour")  


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types=df["User Type"].value_counts()
    print("the counts of user types:",counts_of_user_types)

    if  "Gender" not in df and "Birth Year" not in df:
        print("there is no Birth Year or gender column in washington")
    else: 
        # Display counts of gender
        counts_of_gender=df["Gender"].value_counts()
        print("the counts of gender is :",counts_of_gender )
        # Display earliest, most recent, and most common year of birth
        #since the earliest year is the minimum number I used min()
        earliest_year=int(df["Birth Year"].min()) #the result without int() is float (e.g.1899.0) so I have to use int to prevent that
        print("the earliest year is of birth:",earliest_year)
        #since the most recent year is largest number I use max()
        most_recent_year=int(df["Birth Year"].max())        
        print("the most recent year of birth :",most_recent_year)
        #I will use value_counts().idxmax() to determine the most common years but I could use mode()][0] too !
        the_most_common_year=int(df["Birth Year"].value_counts().idxmax())
        print("the most common year is: ",the_most_common_year)
    
         

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#I define a new function to irritate 5 rows in each time respectivelydef user_data(df):
def user_data(df):
   x=5
   while True :
        
            user_answer=input("would you like to display user trips data ?").lower() #I used lower() to to improve the case insensitivity
            if user_answer not in user_answer_list :
                print("please answer with (yes) or (no) only") 
            elif user_answer== "yes":
                print(df.head(x))
                x+=5
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
        user_data(df)
        
        
        
                

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
