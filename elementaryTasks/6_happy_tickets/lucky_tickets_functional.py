def easy_way_determine_lucky_tickets(ticket: str) -> bool:
    """Determines if the ticket is lucky if the sum of the first three digits
    is equal to the sum of the last three.
    :return bool result. True if ticket is lucky, False if not."""
    first_part_ticket = sum(map(int, ticket[:3]))
    second_part_ticket = sum(map(int, ticket[3:]))
    return first_part_ticket == second_part_ticket


def hard_way_determine_lucky_tickets(ticket: str) -> bool:
    """Determines if the ticket is lucky if the sum of the even numbers of the ticket
    is equal to the sum of the odd numbers of the ticket.
    :return bool result. True if ticket is lucky, False if not."""
    even_numb_sum = 0
    odd_numb_sum = 0
    for numb in ticket:
        if int(numb) % 2 == 0:
            even_numb_sum += int(numb)
        else:
            odd_numb_sum += int(numb)
    return even_numb_sum == odd_numb_sum


def comparison_calculation_methods(min_ticket: str, max_ticket: str):
    """Compare easy and hard ways to determine if ticket is lucky. Prints result of comparing."""
    lucky_tickets_easy_way = 0
    lucky_tickets_hard_way = 0
    if int(min_ticket) < int(max_ticket):
        for ticket in range(int(min_ticket), int(max_ticket)):
            if easy_way_determine_lucky_tickets(str(ticket)):
                lucky_tickets_easy_way += 1
            if hard_way_determine_lucky_tickets(str(ticket)):
                lucky_tickets_hard_way += 1

    if lucky_tickets_easy_way > lucky_tickets_hard_way:
        print(f"Easy way for counting lucky tickets gives {lucky_tickets_easy_way} lucky tickets, "
              f"hard way gives {lucky_tickets_hard_way}")
    elif lucky_tickets_easy_way < lucky_tickets_hard_way:
        print(f"Hard way for counting lucky tickets gives {lucky_tickets_easy_way} lucky tickets, "
              f"easy way gives {lucky_tickets_hard_way}")


if __name__ == '__main__':
    continue_ = True
    while continue_:
        try:
            min_ticket_numb = input("Enter min ticket number: ")
            max_ticket_numb = input("Enter max ticket number: ")
            if len(min_ticket_numb) == 6 and len(max_ticket_numb) == 6 and min_ticket_numb < max_ticket_numb:
                comparison_calculation_methods(min_ticket_numb, max_ticket_numb)
            else:
                raise ValueError
        except ValueError:
            print("Please enter a positive value consisting of 6 numbers. "
                  "Min ticket number should be less than max ticket number.")

        continue_ = input("Do you want check another tickets (y / n): ").lower() == "y"
