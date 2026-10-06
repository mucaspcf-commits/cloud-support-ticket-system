# Project 5: Cloud Support Team
# The system separates regular users and support team members
# to represent a more realistic Service Desk environment.
# The authorised support team emails are: cloud.support@company.com and team.leader@company.com
# Imports datetime to track when tickets are created, updated, and closed.
# libraries modules
from datetime import datetime
#Stores all submitted tickets.
tickets = []
#Stores each user's email and registered name.
# dictionaries
registered_users = {}
#Records the number to be used for the next ticket.
next_ticket_number = 1
#Stores the list of supported cloud services.
service_types = ( "AWS", "Microsoft Azure", "Google Cloud", "Oracle Cloud", "IBM Cloud", "Salesforce Platform")
#Stores all supported cloud issue types.
issue_types = ( "Access", "Performance", "Deployment", "Availability", "Network", "Security", "Cloud Storage", "Database", "Backup and Recovery", "Configuration", "Disk and Memory Resources", "Billing and Cost")
#Keeps a list of email addresses with support access.
support_team_emails = ("cloud.support@company.com","team.leader@company.com")
#Shows the available options for a regular user.
def display_user_menu():
    print("\n" + "=" * 72) #Prints a separator line to organise the menu.
    print(" CLOUD SUPPORT TICKET SYSTEM - USER MENU".center(72))#Centres the user menu title within 72 characters.
    print("=" * 72) #Prints a separator line of 72 equals signs.
    print("1) Subimit a new ticket")
    print("2) View my tickets")
    print("3) Check one of my tickets")
    print("4) Log out ")
    print("5) Exit program")
    print("=" * 72) #Prints a separator line of 72 equals signs.
# Displays the support team menu.
def display_support_menu():
    print("\n" + "=" * 72) #Prints a separator line to organise the menu.
    print("CLOUD SUPPORT TICKET SYSTEM - SUPPORT MENU".center(72))
    print("=" * 72) #Prints a separator line of 72 equals signs.
    print("1) View all tickets")
    print("2) Check one ticket")
    print("3) Update ticket status")
    print("4) Display unresolved tickets")
    print("5) Count unresolved tickets by issue type")
    print("6) Add a support comment")
    print("7) Run recurring cloud maintenance")
    print("8) Log out")
    print("9) Exit program")
    print("=" * 72) #Prints a separator line of 72 equals signs.
# Asks for an email address and performs a simple format check.
def get_valid_email(message):
    while True:
        email = input(message).strip().lower()# Asks the user for an email, removes spaces, and converts it to lowercase
        at_position = email.find("@") # Finds the position of the "@" symbol in the email
        domain_parts = email[at_position + 1:].split(".")  # Splits the email domain into labels.
        if email.count("@") == 1 and at_position > 0 and not any(character.isspace() for character in email) and not email.startswith(".") and not email[:at_position].endswith(".") and ".." not in email[:at_position] and len(domain_parts) >= 2 and all(part and part.isascii() and all(character.isalnum() or character == "-" for character in part) and not part.startswith("-") and not part.endswith("-") for part in domain_parts):  # Checks the basic email format and rejects empty or invalid domain labels.
            return email
        print( "Invalid email address. " "Please enter a valid email address.")
# Checks the email to determine whether the user is support or a regular user.
#loop
def login():
    print("\n--- LOGIN ---")
    email = get_valid_email("Enter your email address: ") #Requests a valid email address from the user
    if email in support_team_emails:# Checks if the entered email belongs to the support team
        print("Support team access granted.")
        return email, "support"# Returns the email and identifies the user role as support
    print("User access granted.")
    return email, "user"# Returns the email and identifies the user role as USER
# Returns the email and assigns the support role.
def get_or_register_user_name(user_email):
    if user_email in registered_users:  # Checks whether the user's email is already registered.
        saved_name = registered_users[user_email]  # Stores the name associated with that email in saved_name.
        print( "Registered user name:",saved_name)
        return saved_name
    while True:
        user_name = input("Enter your name: ").strip()
        if user_name != "":  # Checks that the name is not empty.
            user_name = user_name.title()  # Converts the name to title case.
            registered_users[user_email] = user_name  # Stores the name under the user's email address.
            return user_name  # Returns the registered name.
        print("Your name cannot be empty." )
# Displays options stored in a tuple and returns the option selected by the user.
def select_from_tuple(title, items):
    while True:
        print("\n" + title)
        for position in range(len(items)):  # Loops through the index of each item.
            print(position + 1, ")",items[position])  # Displays each item with a number starting from 1.
        choice = input("Enter your choice: ").strip()  # Reads the choice and removes leading and trailing whitespace.
        if choice.isdecimal() and len(choice) <= 100:  # Checks whether the choice contains at most 100 decimal digits.
            choice_number = int(choice)  # Converts the choice to an integer.
            if (choice_number >= 1 and choice_number <= len(items)):  # Checks whether the number is within the available options.
                return items[choice_number - 1]  # Returns the selected item using its zero-based index.
        print("Invalid choice. Please try again.")
# Requests the cloud service related to the problem.
def select_service_type():
    return select_from_tuple("Select the cloud service:",service_types)
# Requests the type of cloud issue.
def select_issue_type():
    return select_from_tuple("Select the cloud issue type:",  issue_types)
# Requests the urgency of the ticket.
def select_priority():
    priorities = ("Low", "Medium", "High")
    return select_from_tuple("Select the ticket urgency:",priorities)
# Shortens long text so that it fits inside the ticket table.
def short_text(text, maximum_width):  # Defines a function that shortens text to fit the specified width.
    text = str(text)  # Converts the value to a string.
    if len(text) <= maximum_width:  # Checks whether the text fits within the maximum width.
        return text  # Returns the text unchanged if it already fits.
    return (text[:maximum_width - 3] + "...")
# Displays one or more tickets in an organised table.
def display_ticket_table(ticket_list,table_title):
    print("\n" + "=" * 72) #Prints a separator line to organise the menu.
    print(table_title.center(72))
    print("=" * 72) #Prints a separator line of 72 equals signs.
    if len(ticket_list) == 0:
        print( "No tickets are available.")
        return
    line = ("+--------------------+" "--------------------------------------------------+")
    row_format = ("| {:<18} | {:<48} |")
    for ticket in ticket_list:
        ticket_rows = (( "Ticket number", ticket["ticket_number"]), ("User name",ticket["user_name"]), ("User email",ticket["user_email"]), ("Cloud service",ticket["service_type"]), ("Issue type",ticket["issue_type"]), ("Description",ticket["description"]), ("Status",ticket["status"]), ("Priority",ticket["priority"]), ("Created at",ticket["created_at"]), ("Status updated at",ticket["status_updated_at"]), ("Closed at",ticket["closed_at"]), ("Support comment",ticket["support_comment"]))
        print(line)
        print(row_format.format("FIELD","VALUE"))
        print(line)
        for field_name, field_value in ticket_rows:
            print(row_format.format(field_name,short_text(field_value,48 )))
        print(line)
    print("Total tickets displayed:",len(ticket_list))
    print("=" * 72) #Prints a separator line of 72 equals signs.
# Creates a new cloud support ticket and stores it in the ticket list.
def submit_ticket(logged_user_email):
    global next_ticket_number
    print("\n--- SUBMIT A NEW TICKET ---")
    user_name = get_or_register_user_name(logged_user_email)
    service_type = select_service_type()
    issue_type = select_issue_type()
    while True:
        ticket_description = input("Describe the cloud issue: ").strip()
        if ticket_description != "":
            break
        print("The ticket description ""cannot be empty.")
    ticket_priority = select_priority()
    created_at = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    new_ticket = {"ticket_number":next_ticket_number, "user_name":user_name, "user_email":logged_user_email, "service_type":service_type, "issue_type":issue_type, "description":ticket_description, "status":"Open", "priority":ticket_priority, "created_at": created_at, "status_updated_at": "Not updated", "closed_at":"Not closed", "support_comment":"No comment"}
    tickets.append(new_ticket)
    print("\nTicket submitted successfully.")
    print("Your ticket number is:",next_ticket_number)
    print("Created at:",created_at)
    next_ticket_number += 1
# Searches for a ticket using its unique ticket number.
def find_ticket(search_number):
    for ticket in tickets:
        if (ticket["ticket_number"] == search_number ):
            return ticket
    return None
# Requests a ticket number and only accepts numeric input.
def get_ticket_number():
    while True:
        number_input = input("Enter the ticket number: ").strip()
        if number_input.isdecimal() and len(number_input) <= 100:
            return int(number_input)
        print("Invalid ticket number. " "Please enter numbers only.")
# Checks whether the logged-in person has permission to view a ticket.
def can_view_ticket(ticket,logged_user_email,user_role):
    if user_role == "support":
        return True
    return ( ticket["user_email"] == logged_user_email)
# Displays all information stored for one ticket.
def display_ticket_details(ticket):
    print("\n" + "-" * 72)
    print("Ticket number     :",ticket["ticket_number"])
    print("User name:",ticket["user_name"])
    print("User email:",ticket["user_email"])
    print("Cloud service:", ticket["service_type"])
    print("Issue type :",ticket["issue_type"])
    print("Description:",ticket["description"])
    print("Status:",ticket["status"])
    print("Priority:",ticket["priority"])
    print("Created at:",ticket["created_at"])
    print( "Status updated at :",ticket["status_updated_at"])
    print("Closed at:",ticket["closed_at"])
    print("Support comment:",ticket["support_comment"])
    print("-" * 72) #Prints a separator line of 72 hyphens.
# Displays all tickets for the support team.
def view_all_tickets():
    display_ticket_table(tickets,"ALL TICKETS")
# Displays only the tickets created by the logged-in user.
def view_my_tickets(logged_user_email):
    my_tickets = []
    for ticket in tickets:
        if (ticket["user_email"] == logged_user_email ):
            my_tickets.append( ticket )
    display_ticket_table(my_tickets,"MY TICKETS")
# Finds one ticket and displays it only if the user has permission.
def check_ticket_status(logged_user_email,user_role):
    print("\n--- CHECK TICKET STATUS ---")
    if len(tickets) == 0:
        print("No tickets are available.")
        return
    search_number = get_ticket_number()  # Gets the ticket number entered by the user.
    ticket = find_ticket(search_number)  # Finds the ticket with the specified number.
    if ticket is None:
        print("Ticket number not found.")
        return
    if not can_view_ticket(ticket,logged_user_email,user_role):
        print("Access denied. " "You can only view your own tickets.")
        return
    display_ticket_details(ticket)
# Allows the support team to change the status of a ticket.
def update_ticket_status():
    print("\n--- UPDATE TICKET STATUS ---")
    if len(tickets) == 0:
        print("No tickets are available.")
        return
    search_number = get_ticket_number()  # Gets the ticket number entered by the user.
    ticket = find_ticket(search_number)  # Finds the ticket with the specified number.
    if ticket is None:
        print("Ticket number not found.")
        return
    print("\nSelected ticket:")
    print('User name:', ticket['user_name'])
    print('Cloud service:', ticket['service_type'])
    print('Issue type:', ticket['issue_type'])
    print('Description:', ticket['description'])
    print('Current status:', ticket['status'])
    status_options = ( "Open", "In Progress", "Closed" )  # Lists the available ticket statuses.
    new_status = select_from_tuple( "Select the new ticket status:", status_options )  # Asks the user to select the new ticket status.
    status_change_time = ( datetime.now().strftime( "%d/%m/%Y %H:%M:%S" ) )  # Formats the current date and time for the status update.
    ticket["status"] = ( new_status )  # Saves the selected status in the ticket.
    ticket["status_updated_at"] = ( status_change_time )  # Records when the ticket status was updated.
    if new_status == "Closed":  # Checks whether the ticket is now closed.
        ticket["closed_at"] = ( status_change_time )  # Records the date and time the ticket was closed.
    else:  # Handles a status other than Closed.
        ticket["closed_at"] = ( "Not closed" )  # Marks the ticket as not closed.
    print('\nTicket status updated successfully.')
    print('New status:', ticket['status'])
    print('Status updated at:', ticket['status_updated_at'])
    print('Closed at:', ticket['closed_at'])
# Creates a list containing every ticket that is still unresolved.
def display_unresolved_tickets():
    unresolved_tickets = []
    for ticket in tickets:
        if ( ticket["status"] != "Closed" ):  # Checks whether the ticket is not closed.
            unresolved_tickets.append( ticket )  # Adds the ticket to the list of unresolved tickets.
    display_ticket_table( unresolved_tickets, "UNRESOLVED TICKETS" )  # Displays the unresolved tickets in a table.
# Counts unresolved tickets for every cloud issue category.
def count_unresolved_tickets_by_issue_type():
    print('\n--- UNRESOLVED TICKETS BY ISSUE TYPE ---')
    total_unresolved = 0
    for issue_type in issue_types:  # Loops through each issue type.
        matching_tickets = []  # Creates an empty list for unresolved tickets of this issue type.
        for ticket in tickets:  # Loops through each ticket.
            if ( ticket["issue_type"] == issue_type and ticket["status"] != "Closed" ):  # Checks whether the ticket matches this issue type and is not closed.
                matching_tickets.append( ticket )  # Adds the matching ticket to the list.
                total_unresolved += 1  # Increases the total number of unresolved tickets by one.
        print("-" * 72) #Prints a separator line of 72 hyphens.
        print(issue_type, ':', len(matching_tickets))
        if len(matching_tickets) > 0:
            for ticket in matching_tickets:
                print('- Ticket', ticket['ticket_number'], '|', ticket['user_name'], '|', ticket['service_type'])
                print('  Description:', ticket['description'])
    print("-" * 72) #Prints a separator line of 72 hyphens.
    print('Total unresolved tickets:', total_unresolved)
# Allows the support team to add a short comment to a ticket.
def add_support_comment():
    print('\n--- ADD A SUPPORT COMMENT ---')
    if len(tickets) == 0:
        print('No tickets are available.')
        return
    search_number = get_ticket_number()  # Gets the ticket number entered by the user.
    ticket = find_ticket( search_number )  # Finds the ticket with the specified number.
    if ticket is None:
        print('Ticket number not found.')
        return
    print('\nSelected ticket:')
    print('User name:', ticket['user_name'])
    print('Cloud service:', ticket['service_type'])
    print('Issue type:', ticket['issue_type'])
    print('Description:', ticket['description'])
    print('Status:', ticket['status'])
    print('Current support comment:', ticket['support_comment'])
    while True:
        support_comment = input( "Enter a brief support comment " "(maximum 100 characters): " ).strip()  # Reads the support comment and removes leading and trailing whitespace.
        if support_comment == "":  # Checks whether the comment is empty.
            print('The support comment cannot be empty.')  # Displays an error message for an empty comment.
        elif len(support_comment) > 100:  # Checks whether the comment exceeds 100 characters.
            print('The support comment cannot exceed 100 characters.')  # Displays an error message when the comment is too long.
        else:  # Handles a non-empty comment of at most 100 characters.
            ticket["support_comment"] = ( support_comment )  # Saves the valid support comment in the ticket.
            break
    print('\nSupport comment added successfully.')
    print('Comment:', ticket['support_comment'])
# Repeats cloud maintenance checks and counts tickets by service,
# status, and priority.
def run_recurring_maintenance():
    print('\n--- RECURRING CLOUD MAINTENANCE ---')
    while True:
        cycles_input = input( "Enter the number of maintenance cycles: " ).strip()  # Reads the number of maintenance cycles and removes leading and trailing whitespace.
        if cycles_input.isdecimal() and len(cycles_input) <= 100:  # Checks whether the input contains at most 100 decimal digits.
            cycles = int( cycles_input )  # Converts the input to an integer.
            if cycles > 0:  # Checks whether the number of cycles is positive.
                break  # Exits the input loop once a positive number is entered.
        print('Please enter a positive whole number.')
    for cycle in range( 1, cycles + 1 ):
        maintenance_title = ( "MAINTENANCE CYCLE " + str(cycle) )
        print("\n" + "=" * 72) #Prints a separator line to organise the menu.
        print(maintenance_title.center(72))
        print("=" * 72) #Prints a separator line of 72 equals signs.
        for service in service_types:  # Loops through each supported cloud service.
            open_low = 0  # Resets the count of open tickets with low priority.
            open_medium = 0  # Resets the count of open tickets with medium priority.
            open_high = 0  # Resets the count of open tickets with high priority.
            progress_low = 0  # Resets the count of in-progress tickets with low priority.
            progress_medium = 0  # Resets the count of in-progress tickets with medium priority.
            progress_high = 0  # Resets the count of in-progress tickets with high priority.
            closed_count = 0  # Resets the count of closed tickets.
            for ticket in tickets:  # Loops through each ticket.
                if ( ticket["service_type"] == service ):  # Checks whether the ticket belongs to the current service.
                    if ( ticket["status"] == "Closed" ):  # Checks whether the ticket is closed.
                        closed_count += 1  # Increases the closed ticket count by one.
                    elif ( ticket["status"] == "Open" ):  # Checks whether the ticket is open.
                        if ( ticket["priority"] == "Low" ):  # Checks whether the ticket has low priority.
                            open_low += 1  # Increases the count of open tickets with low priority by one.
                        elif ( ticket["priority"] == "Medium" ):  # Checks whether the ticket has medium priority.
                            open_medium += 1  # Increases the count of open tickets with medium priority by one.
                        elif ( ticket["priority"] == "High" ):  # Checks whether the ticket has high priority.
                            open_high += 1  # Increases the count of open tickets with high priority by one.
                    elif ( ticket["status"] == "In Progress" ):  # Checks whether the ticket is in progress.
                        if ( ticket["priority"] == "Low" ):  # Checks whether the ticket has low priority.
                            progress_low += 1  # Increases the count of in-progress tickets with low priority by one.
                        elif ( ticket["priority"] == "Medium" ):  # Checks whether the ticket has medium priority.
                            progress_medium += 1  # Increases the count of in-progress tickets with medium priority by one.
                        elif ( ticket["priority"] == "High" ):  # Checks whether the ticket has high priority.
                            progress_high += 1  # Increases the count of in-progress tickets with high priority by one.
            print('\n' + service)  # Prints a blank line followed by the service name.
            print("-" * 40)  # Prints a separator line of 40 hyphens.
            print("Open")  # Displays the heading for open tickets.
            print('1) Low    :', open_low)  # Displays the count of open tickets with low priority.
            print('2) Medium :', open_medium)  # Displays the count of open tickets with medium priority.
            print('3) High   :', open_high)  # Displays the count of open tickets with high priority.
            print('\nIn Progress')  # Prints a blank line followed by the heading for in-progress tickets.
            print('1) Low    :', progress_low)  # Displays the count of in-progress tickets with low priority.
            print('2) Medium :', progress_medium)  # Displays the count of in-progress tickets with medium priority.
            print('3) High   :', progress_high)  # Displays the count of in-progress tickets with high priority.
            print('\nClosed:', closed_count)  # Prints a blank line followed by the closed ticket count.
    print('\nRecurring cloud maintenance completed.')
# Controls login sessions, menus, and the complete program.
def main():
    program_running = True
    while program_running:
        logged_user_email, user_role = login()  # Logs in and stores the user email and role.
        session_running = True  # Starts the login session.
        while session_running:  # Repeats the menu while the session is active.
            if user_role == "support":  # Checks whether the user has the support role.
                display_support_menu()  # Displays the support menu.
                menu_choice = input("Select an option (1-9): ").strip()  # Reads the menu choice and removes leading and trailing whitespace.
                if menu_choice == "1":  # Checks whether option 1 was selected.
                    view_all_tickets()  # Displays all tickets.
                elif menu_choice == "2":  # Checks whether option 2 was selected.
                    check_ticket_status(logged_user_email,user_role)  # Displays the selected ticket if the user has permission to view it.
                elif menu_choice == "3":update_ticket_status()  # Updates the ticket status when option 3 is selected.
                elif menu_choice == "4":  # Checks whether option 4 was selected.
                    display_unresolved_tickets()  # Displays tickets that are not closed.
                elif menu_choice == "5":  # Checks whether option 5 was selected.
                    count_unresolved_tickets_by_issue_type()  # Counts unresolved tickets for each issue type.
                elif menu_choice == "6":  # Checks whether option 6 was selected.
                    add_support_comment()  # Allows a support comment to be added to a ticket.
                elif menu_choice == "7":  # Checks whether option 7 was selected.
                    run_recurring_maintenance()  # Runs the recurring cloud maintenance checks.
                elif menu_choice == "8":  # Checks whether option 8 was selected.
                    session_running = False  # Ends the current session.
                    print("\nYou have logged out successfully.")  # Displays a logout confirmation message.
                elif menu_choice == "9":  # Checks whether option 9 was selected.
                    session_running = False  # Ends the current session.
                    program_running = False  # Stops the main program loop.
                else:  # Handles an invalid support menu choice.
                    print("Invalid option. ""Please enter a number from 1 to 9.")  # Displays the valid range of support menu options.
            else:  # Handles a regular user session.
                display_user_menu()  # Displays the user menu.
                menu_choice = input("Select an option (1-5): ").strip()  # Reads the menu choice and removes leading and trailing whitespace.
                if menu_choice == "1":  # Checks whether option 1 was selected.
                    submit_ticket(logged_user_email)  # Creates a ticket for the logged-in user.
                elif menu_choice == "2":view_my_tickets(logged_user_email)  # Displays the logged-in user tickets when option 2 is selected.
                elif menu_choice == "3":  # Checks whether option 3 was selected.
                    check_ticket_status(logged_user_email,user_role)  # Displays the selected ticket if the user has permission to view it.
                elif menu_choice == "4":  # Checks whether option 4 was selected.
                    session_running = False  # Ends the current session.
                    print("\nYou have logged out successfully.")  # Displays a logout confirmation message.
                elif menu_choice == "5":  # Checks whether option 5 was selected.
                    session_running = False  # Ends the current session.
                    program_running = False  # Stops the main program loop.
                else:
                    print("Invalid option. " "Please enter a number from 1 to 5.")
    print("\nThe Cloud Support Ticket System ""has been closed.")
# Starts the main program.
main()