#import ticketing.py where the classname is Tickets

from ticketing import Tickets
status="Open Ticket"                 # static variable(assigning outside the function but within the class)


def data_entry(): #fetching data to create tickets
    staff_id = input("Enter your staff Id ")
    ticket_creator = input("Enter the ticket creator's name: ")
    contact_email = input("Enter the contact email: ")
    desc_issue = input("Describe the issue: ")
    print("Ticket is submitted successfully!")
    ticket = Tickets(staff_id, ticket_creator, contact_email, desc_issue)
    ticket.display_data()  #display other ticket details except the inputs
    return ticket


def display_menu():
    print("Ticket System Menu:")
    print("1. Create Tickets")
    print("2. Generate password")
    print("3. Resolve Tickets")
    print("4. Reopen Tickets")
    print("5. Display Tickets")
    print("6. Display Ticket Statistics")
    print("7. Exit")


def generate_pwd(tickets):
    ticket_number = int(input("Enter the ticket number to perform action: "))
    for ticket in tickets:
        if ticket.ticket_no == ticket_number:
            result = ticket.issue_type_pwd()
            if result is not None: # accepts only if the description has "password change"(smaller case)
                print(f"The status of the ticket is: {ticket.ticket_status}")
                print(f"{ticket.response}")
            break


def resolve(tickets):
    ticket_number = int(input("Enter the ticket number to perform action: "))
    response = input("Enter IT team's response: ")
    for ticket in tickets:
        if ticket.ticket_no == ticket_number:
            ticket.ticket_status = "Closed"
            ticket.response = "Issue is resolved"
            print("Ticket has been resolved successfully!")
            Tickets.resolved_ticket += 1
            Tickets.opened_ticket -= 1
            break


def reopen(tickets):
    ticket_number = int(input("Enter the ticket number to perform action: "))
    for ticket in tickets:
        if ticket.ticket_no == ticket_number:
            ticket.ticket_status = "Reopened"
            print("Ticket has been reopened successfully!")
            Tickets.resolved_ticket -= 1
            Tickets.opened_ticket += 1
            return


def listing_tickets(tickets):
    for ticket in tickets:
        ticket.display_data()


def main():
    tickets = []
    print("Welcome to the Ticketing System!")
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            tickets.append(data_entry())
        elif choice == '2':
            generate_pwd(tickets)
        elif choice == '3':
            resolve(tickets)
        elif choice == '4':
            reopen(tickets)
        elif choice == '5':
            listing_tickets(tickets)
        elif choice == '6':
            Tickets.data_stats()
        elif choice == '7':
            exit()


if __name__ == "__main__":
    main()
