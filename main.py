import csv
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "support-tickets.csv"

with open(DATA_FILE, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    tickets = list(reader)


def show_summary(tickets): 
    print("CUSTOMER SUPPORT TICKET ANALYZER")
    print("---------------------------------")
    print("Total tickets:", len(tickets))
    print("Columns:", list(tickets[0].keys()) if tickets else "No data found")


# Count tickets by support queue

def count_tickets_by_queue(tickets):
    queue_counts = {}

    for ticket in tickets:
        queue = ticket["queue"]

        if queue in queue_counts:
            queue_counts[queue] += 1
        else:
            queue_counts[queue] = 1

    print("\nTickets by Queue:")

    for queue, count in queue_counts.items():
        print(queue, ":", count)



# Count tickets by priority

def count_tickets_by_priority(tickets):
    priority_counts = {}

    for ticket in tickets:
        priority = ticket["priority"]

        if priority in priority_counts:
            priority_counts[priority] += 1
        else:
            priority_counts[priority] = 1

    print("\nTickets by priority:")

    for priority, count in priority_counts.items():
        print(priority, ":", count)



def analyze_response_times(tickets):
    response_times = {}
    missing_response_times = 0

    for ticket in tickets:
        priority = ticket["priority"]
        response = ticket["first_response_min"].strip()

        if response == "":
            missing_response_times += 1
            continue

        response = float(response)

        if priority not in response_times:
            response_times[priority] = []

        response_times[priority].append(response)

    print("\nAverage First Response Time by Priority:")

    for priority, times in response_times.items():
        average = sum(times) / len(times)
        print(priority, ":", round(average, 2), "minutes")

    print("Tickets with missing response times:", missing_response_times)




def analyze_resolution(tickets):
    recorded_resolution_count = 0
    missing_resolution_count = 0

    for ticket in tickets:
        resolved_at = ticket["resolved_at"].strip()

        if resolved_at == "":
            missing_resolution_count += 1
        else:
            recorded_resolution_count += 1

    print("\nResolution Timestamp Analysis:")
    print("Tickets with recorded resolution timestamps:",
          recorded_resolution_count)
    print("Tickets without recorded resolution timestamps:",
          missing_resolution_count)

    if tickets:
        recorded_rate = (
            recorded_resolution_count / len(tickets)
        ) * 100

        print(
            "Percentage with recorded resolution timestamps:",
            round(recorded_rate, 2),
            "%"
        )



def analyze_customer_satisfaction(tickets):
    total_csat = 0
    csat_count = 0
    missing_csat = 0

    for ticket in tickets:
        rating = ticket["csat"].strip()

        if rating == "":
            missing_csat += 1
            continue

        total_csat += float(rating)
        csat_count += 1

    print("\nCustomer Satisfaction Analysis:")

    if csat_count > 0:
        average_csat = total_csat / csat_count
        print("Average satisfaction score:", round(average_csat, 2))
        print("Tickets with satisfaction ratings:", csat_count)
    else:
        print("No satisfaction ratings available.")

    print("Tickets with missing satisfaction ratings:", missing_csat)



def analyze_reopened_tickets(tickets):
    reopened_count = 0
    not_reopened_count = 0

    for ticket in tickets:
        reopened = ticket["reopened"].strip().lower()

        if reopened == "true":
            reopened_count += 1
        elif reopened == "false":
            not_reopened_count += 1

    print("\nTicket Reopening Analysis:")
    print("Reopened tickets:", reopened_count)
    print("Not reopened:", not_reopened_count)

    tickets_with_reopen_status = reopened_count + not_reopened_count

    if tickets_with_reopen_status > 0:
        reopen_rate = (
            reopened_count / tickets_with_reopen_status
        ) * 100

        print("Reopening rate:", round(reopen_rate, 2), "%")



def analyze_satisfaction_by_reopening(tickets):
    csat_by_reopened = {}

    for ticket in tickets:
        reopened = ticket["reopened"].strip().lower()
        rating = ticket["csat"].strip()

        if rating == "":
            continue

        if reopened not in csat_by_reopened:
            csat_by_reopened[reopened] = []

        csat_by_reopened[reopened].append(float(rating))

    print("\nSatisfaction by Reopening Status:")

    for reopened, ratings in csat_by_reopened.items():
        average = sum(ratings) / len(ratings)

        if reopened == "true":
            label = "Reopened"
        else:
            label = "Not Reopened"

        print(label, ":", round(average, 2), "/ 5")
        print("Rated tickets:", len(ratings))



def analyze_satisfaction_by_priority(tickets):
    csat_by_priority = {}

    for ticket in tickets:
        priority = ticket["priority"].strip().lower()
        rating = ticket["csat"].strip()

        if rating == "":
            continue

        if priority not in csat_by_priority:
            csat_by_priority[priority] = []

        csat_by_priority[priority].append(float(rating))

    print("\nSatisfaction by Priority:")

    for priority, ratings in csat_by_priority.items():
        average = sum(ratings) / len(ratings)

        print(priority.title(), ":", round(average, 2), "/ 5")
        print("Rated tickets:", len(ratings))



def analyze_satisfaction_by_queue(tickets):
    csat_by_queue = {}

    for ticket in tickets:
        queue = ticket["queue"].strip().lower()
        rating = ticket["csat"].strip()

        if rating == "":
            continue

        if queue not in csat_by_queue:
            csat_by_queue[queue] = []

        csat_by_queue[queue].append(float(rating))

    print("\nSatisfaction by Support Queue:")

    for queue, ratings in csat_by_queue.items():
        average = sum(ratings) / len(ratings)

        print(queue.title(), ":", round(average, 2), "/ 5")
        print("Rated tickets:", len(ratings))




def check_data_quality(tickets):
    print("\nDATA QUALITY CHECK")
    print("------------------")

    if not tickets:
        print("No ticket data available.")
        return

    for column in tickets[0].keys():
        missing_count = 0

        for ticket in tickets:
            if ticket[column].strip() == "":
                missing_count += 1

        print(column, ":", missing_count, "missing values")




def validate_csat(tickets):
    print("\nCSAT VALIDATION")
    print("---------------")

    invalid_csat = 0
    valid_csat = 0

    for ticket in tickets:
        rating = ticket["csat"].strip()

        if rating == "":
            continue

        try:
            rating = float(rating)

            if 1 <= rating <= 5:
                valid_csat += 1
            else:
                invalid_csat += 1

        except ValueError:
            invalid_csat += 1

    print("Valid CSAT ratings:", valid_csat)
    print("Invalid CSAT ratings:", invalid_csat)


def main():
    show_summary(tickets)
    count_tickets_by_queue(tickets)
    count_tickets_by_priority(tickets)
    analyze_response_times(tickets)
    analyze_resolution(tickets)
    analyze_customer_satisfaction(tickets)
    analyze_reopened_tickets(tickets)
    analyze_satisfaction_by_reopening(tickets)
    analyze_satisfaction_by_priority(tickets)
    analyze_satisfaction_by_queue(tickets)
    check_data_quality(tickets)
    validate_csat(tickets)


if __name__ == "__main__":
    main()

