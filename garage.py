class Garage:

    def __init__(self, avail_tickets, used_tickets, total_spaces):
        self.avail_tickets = avail_tickets
        self.used_tickets = used_tickets
        self.total_spaces = total_spaces

    def takeTicket(self):
        if self.avail_tickets == []:
            print('The parking lot is full. Please come again soon.')
        
        else:
            print(f'Your ticket number is #{self.avail_tickets[0]}')
            self.used_tickets[self.avail_tickets.pop(0)] = False
            
    def payTicket(self):
        ticket = int(input('What is your ticket #:'))
        
        if ticket in self.used_tickets:
            input('Input amount to pay for ticket:')
            self.used_tickets[ticket] = True
            print('Your ticket has been paid for.\n Proceed to the exit gate.')
        
        else:
            print("That ticket # is invalid. Try again.")

    # A debug just to find out if ticket has been paid for.        
    def ticketStatus(self):
        ticket = int(input('What is your ticket #:'))
        print(self.used_tickets[ticket])

    def leaveGarage(self):
        pass





# Sami,
# Just some things:
# When you use leave garage the value of self.used_ticket[whatever ticket number here]
# Should equal True before leave garage adds the ticket back to the avail_tickets list
# Slack me if you have any questions. I'll see you at 2est tomorrow

def run():
    slcgarage = Garage([1,2,3,4,5,6,7,8,9,10], {}, 10)
