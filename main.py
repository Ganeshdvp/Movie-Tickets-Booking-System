movies_list = ['Varanasi', 'Raaka', 'Spirit', 'fauzi', 'kaaka']
show_timings = [
    ['8:30am', '11:00am', '2:30pm', '5:30pm','8:30pm'], 
    ['8:30am', '2:30pm', '5:30pm','8:30pm'],
    ['8:30am', '11:00am', '5:30pm','8:30pm'],
    ['8:30am', '11:00am', '2:30pm', '5:30pm'],
    ['11:00am', '2:30pm', '5:30pm','8:30pm'],
]
tickets = [
    [
        [[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,0,0,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    ],
    [
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    ],
    [
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    ],
    [
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    ],
    [
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
        [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]],
    ]
]

admin_menu = ['Add Movie', 'Remove Movie', 'Update Movie', 'Add Shows', 'Remove Shows', 'Update Show', 'Add Tickets', 'Remove Seats', 'Update Seats', 'View Bookings', 'Exit']
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
        total_available_tickets = 0
        for i in range(len(tickets[selected_movie][selected_show_time])):
            for j in tickets[selected_movie][selected_show_time][i]:
                if j != 0:
                    total_available_tickets+=1
        print('-' * 30)
        print('Available tickets are : ', total_available_tickets)
        print('-' * 30)

        while True:
            # Want to book ticket
            status = input('Want to book a ticket? (Yes/No) : ')
    
            # Booking Tickets
            if status == 'Yes':
                while True:
                    booked_tickets = int(input('How many tickets want to book? : '))
                    if booked_tickets <= total_available_tickets:
                        for i in range(0,len(tickets[selected_movie][selected_show_time])+1):
                            print('   ', i, end='',sep='')
                        print()
                        for i in range(len(tickets[selected_movie][selected_show_time])):
                            print(i, '-', sep='', end='')
                            for j in tickets[selected_movie][selected_show_time][i]:
                                print('|', ' ', '|','-', sep='',end='')
                            print()
                        bookings.append(booked_tickets)
                        i=1
                        while i<=booked_tickets:
                            while True:
                                row = int(input('select row: '))
                                if row < len(tickets[selected_movie][selected_show_time]):
                                    while True:
                                        col = int(input('select col: '))
                                        if col < len(tickets[selected_movie][selected_show_time][row]):
                                            if tickets[selected_movie][selected_show_time][row][col] != 0:
                                                tickets[selected_movie][selected_show_time][row][col] = 0
                                                i+=1
                                            else:
                                                print('Already Booked Dude! Try other!')
                                            break
                                        else:
                                            print('Invalid Column!')
                                    break
                                else:
                                    print('Invalid row!')

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
            status = int(input('Select One of the menu list?  :' ))
            
            # exit logic
            if status == 10:
                print('Thanks for visiting! Come again later...')
                break
    
            # Add Movie logic
            elif status == 0:
                movie = input('Enter new movie to add : ')
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
                print('---Running movies are : ')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('--- Existing Show Times are : ')
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
                print('---Running movies are : ')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('---Existing Show times are : ')
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
                print('---Running movies are : ')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('--- Existing Show times are : ')
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
                print('---Running movies are : ')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('--- Running Show times are : ')
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        while True:
                            update_show_time = int(input('Select Show Time : '))
                            if update_show_time < len(show_timings[select_movie]):
                                total_available_tickets = 0
                                for i in range(len(tickets[select_movie][update_show_time])):
                                    for j in tickets[select_movie][update_show_time][i]:
                                        if j != 0:
                                            total_available_tickets+=1
                                print('Available tickets are : ', total_available_tickets)
                                add_tickets = int(input('How many tickets want to add? : '))
                                i = 1
                                seat = []
                                while i<=add_tickets:
                                    seat.append(1)
                                    i+=1
                                tickets[select_movie][update_show_time].append(seat)
                                for i in range(len(tickets[select_movie][update_show_time])):
                                    print(i, '-', sep='', end='')
                                    for j in tickets[select_movie][update_show_time][i]:
                                        print('|', ' ', '|','-', sep='',end='')
                                    print()
                                print('Yaahoo! Successfully added tickets! ')
                                break
                            else:
                                print('Invalid Show Time')
                        break
                    else:
                        print('Invalid Movie!')
                break

            # Remove seats/tickets logic
            elif status == 7:
                print('---Running movies are : ')
                for i in range(len(movies_list)):
                    print(i, '-', movies_list[i])
                while True:
                    select_movie = int(input('Select Movie :'))
                    if select_movie < len(movies_list):
                        print('---Running Show times are : ')
                        for i in range(len(show_timings[select_movie])):
                            print(i, '-', show_timings[select_movie][i])
                        while True:
                            select_show_time = int(input('Select Show Time : '))
                            if select_show_time < len(show_timings[select_movie]):
                                total_available_seats = 0
                                for i in range(len(tickets[select_movie][select_show_time])):
                                    for j in tickets[select_movie][select_show_time][i]:
                                        if j != 0:
                                            total_available_seats+=1
                                print('Available seats are : ', total_available_seats)
                                remove_seats = int(input('How many seats want to remove? : '))
                                i = 1
                                while i<=remove_seats:
                                    last = len(tickets[select_movie][select_show_time])-1
                                    tickets[select_movie][select_show_time][last].pop()
                                    i+=1
                                
                                for i in range(len(tickets[select_movie][select_show_time])):
                                    print(i, '-', sep='', end='')
                                    for j in tickets[select_movie][select_show_time][i]:
                                        print('|', ' ', '|','-', sep='',end='')
                                    print()
                                print('Yaahoo! Successfully removed seats! ')
                                break
                            else:
                                print('Invalid Show Time')
                        break
                    else:
                        print('Invalid Movie!')
                break

            # View Booking logic
            elif status == 9:
                print('--- Booking ---')
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