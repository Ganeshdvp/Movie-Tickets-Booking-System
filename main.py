movies_list = ['Varanasi', 'Raaka', 'Spirit', 'fauzi', 'kaaka']
show_timings = [
    ['8:30am', '11:00am', '2:30pm', '5:30pm','8:30pm'], 
    ['8:30am', '2:30pm', '5:30pm','8:30pm'],
    ['8:30am', '11:00am', '5:30pm','8:30pm'],
    ['8:30am', '11:00am', '2:30pm', '5:30pm'],
    ['11:00am', '2:30pm', '5:30pm','8:30pm'],
]
tickets = [
    [60,60,60,60,60],
    [30,20,10,20],
    [0,10,5,4],
    [55,50,35,25],
    [55,50,58,30],
]
admin_menu = ['Add Movie', 'Remove Movie', 'Update Movie', 'Add Shows', 'Remove Shows', 'Update Show', 'Add Tickets', 'View Bookings', 'Exit']
bookings = [10,5,12,44]


while True:
    user_type = input('Enter what you are (Owner/Custumer) : ')

# Customer
    if user_type == 'Customer':

        # Showing all movies
        print('Currently running movies are : ')
        for i in range(0, len(movies_list)):
            print(i, '-', movies_list[i])

        while True:
            # Selecting movie
            selected_movie = int(input('Select your Movie: '))

            # Cover edge-case
            if len(movies_list) <= selected_movie:
                print('Your Movie is on Jupiter planet, So please select valid movie!')
            else:
                break
            
        # Showing the show times
        show_timing = show_timings[selected_movie]
        print('Available Show Times are : ')
        for i in range(0, len(show_timing)):
            print(i, '-', show_timing[i])

        while True:
            # Selecting Show time
            selected_show_time = int(input('Select your Show time: '))

            # Cover edge-case
            if len(tickets[selected_movie]) <= selected_show_time:
                print('I didnt do any degree to understand your show time So, Please select valid above show time! ')
            else:
                break

        # Showing tickets
        available_tickets = tickets[selected_movie][selected_show_time]
        print('-' * 30)
        print('Available tickets are : ', available_tickets)
        print('-' * 30)

        while True:
            # Want to book ticket
            status = input('Want to book a ticket? (Yes/No) : ')
    
            # Booking Tickets
            if status == 'Yes':
                while True:
                    booked_tickets = int(input('How many tickets want to book? : '))
                    if booked_tickets <= available_tickets:
                        tickets[selected_movie][selected_show_time] = available_tickets - booked_tickets
                        print('Congratulations! You have successfully booked ',booked_tickets, 'tickets')
                        bookings.append(booked_tickets)
                        print('=' * 30)
                        print(movies_list[selected_movie], ' ', show_timings[selected_movie][selected_show_time], ' ', booked_tickets, 'tickets')
                        print('=' * 30)
                        print('ENJOY PANDAGOOOOW...')
                        break
                    else:
                        print('Sorry Rich Burroh! Out of Stock!')
                        print('Your not a PM/CM so, try again later!')
                break
            elif status == 'No':
                print('Really? dont you want to buy a ticket then why do you came here IDIOT?...')
                break
            else:
                print('Read properly and Enter valid answer YOU LITTLE BRAT! ')
        
        break

# Owner
    elif user_type == 'Owner':

        print('--Menu--')
        for i in range(len(admin_menu)):
            print(i, '-', admin_menu[i])

        while True:
            status = int(input('Select One Admin Bruooh :' ))
            
            # exit logic
            if status == 8:
                print('Thanks for visiting...')
                break
    
            # Add Movie logic
            elif status == 0:
                movie = input('Enter new movie: ')
                movies_list.append(movie)
                print('Yaahoo! successfully added to movies list!')
                break
    
            # Remove Movie logic
            elif status == 1:
                print('---', 'Running Movies are :')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    remove_movie = int(input('Select Movie to remove : '))
                    if remove_movie < len(movies_list):
                        movies_list.pop(remove_movie)
                        print('Yaahoo! Successfully removed! ')
                        break
                    else:
                        print('Invalid Movie dude!')                    
                break
    
            # Update Movie logic
            elif status == 2:
                print('---', 'Running Movies are :')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    update_index = int(input('Select Movie to Update : '))
                    if update_index < len(movies_list):
                        updated_movie = input('Enter your movie : ')
                        movies_list[update_index] = updated_movie
                        print('Yaahoo! successfully updated movie! ')
                        break
                    else:
                        print('Invalid movie to update!')
                break
    
            # Add Show time logic
            elif status == 3:
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('Existing Show Times are : ')
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        add_show_time = input('Add Show Time : ')
                        show_timings[select_movie].append(add_show_time)
                        print('Yaahoo! Successfully added new Show Time')
                        break
                    else:
                        print('Invalid Movie! ')
                break
    
            # Remove Show Time logic
            elif status == 4:
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        while True:
                            remove_show_time = int(input('Select Show Time to remove : '))
                            if remove_show_time < len(show_timings[select_movie]):
                                show_timings[select_movie].pop(remove_show_time)
                                print('Yaahoo! Successfully removed! ')
                                break
                            else:
                                print('Invalid Show time! ')
                        break
                    else:
                        print('Invalid Movie! Select Proper Movie! ')
                break
    
            # Update Show Time logic
            elif status == 5:
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        while True:
                            update_show_time_index = int(input('Select Show Time to update : '))
                            if update_show_time_index < len(show_timings[select_movie]):
                                update_show_time = input('Enter your new Show Time : ')
                                show_timings[select_movie][update_show_time_index] = update_show_time
                                print('Yaahoo! Successfully updated! ')
                                break
                            else:
                                print('Invalid Show time!')
                        break
                    else:
                        print('Invalid Movie!')
                break
    
            # Add Tickets logic
            elif status == 6:
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        while True:
                            update_show_time = int(input('Select Show Time : '))
                            if update_show_time < len(show_timings[select_movie]):
                                print('Available tickets are : ', tickets[select_movie][update_show_time])
                                add_tickets = int(input('How many tickets want to add? : '))
                                tickets[select_movie][update_show_time] += add_tickets
                                print('Yaahoo! Successfully added tickets! ')
                                break
                            else:
                                print('Invalid Show Time')
                        break
                    else:
                        print('Invalid Movie!')
                break
    
            # View Booking logic
            elif status == 7:
                total_tickets_booked = 0
                for i in range(len(bookings)):
                    print(bookings[i],'tickets are booked! ')
                    total_tickets_booked += bookings[i]
                print('-' * 15)
                print('Total tickets booked : ', total_tickets_booked)
                print('-' * 15)
                break
    
            # invalid entry
            else:
                print('Invalid! Please enter valid one! ')
        break
    else:
        print('Enter valid user type dude!')