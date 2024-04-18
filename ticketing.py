class Tickets:
    ticket_no = 2000
    #counter value is 2000
    submitted_ticket=0 # Number of tickets created
    resolved_ticket=0 # Closed tickets
    opened_ticket=0 # Number of tickets to solve

#initialise the inputs
    def __init__(self, staff_id, ticket_creator, contact_email, desc_issue):
        Tickets.ticket_no +=1
        self.staff_id = staff_id
        self.ticket_creator = ticket_creator
        self.contact_email = contact_email
        self.desc_issue = desc_issue
        self.ticket_no= Tickets.ticket_no
        self.ticket_status = "Open Ticket"
        self.response= "Not yet provided"           #default response is set
        Tickets.submitted_ticket +=1

    def issue_type_pwd(self):
        issue = self.desc_issue.split()
        if "password" in issue and "change" in issue:         #if description has password change
            new_pwd = self.staff_id[:2] + self.ticket_creator[:3]
            self.ticket_status = "Closed"
            Tickets.resolved_ticket += 1
            Tickets.opened_ticket -= 1
            self.response = "Response: New password: " + new_pwd  # Response is the new password
            return new_pwd
        else:
            print("The issue description does not contain 'Password' and 'change'.")
            return None

    def display_data(self):
        print("\nTicket Details:\n")
        print(f"Ticket Number: {self.ticket_no}")
        print(f"Ticket Creator: {self.ticket_creator}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Email Address: {self.contact_email}")
        print(f"Description: {self.desc_issue}")
        print(f"Ticket Status: {self.ticket_status}")
        print(f"Response from IT team: {self.response}\n")

    @staticmethod
    def data_stats():            #data_stats may be static and so static method is declared
        print("Displaying Ticket Statistics:")
        print("Total tickets:", Tickets.submitted_ticket)
        print("Closed Tickets:", Tickets.resolved_ticket)
        solve= (Tickets.submitted_ticket - Tickets.resolved_ticket)
        print("Open Tickets:", solve)



