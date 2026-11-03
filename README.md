# Customer Support Ticket Analyzer

## Project Overview

The Customer Support Ticket Analyzer is a Python-based data analysis project that examines customer support ticket records to evaluate operational performance and customer satisfaction.

Using a dataset of 4,000 support tickets, the project explores response times, ticket distribution across support queues and priority levels, resolution timestamps, ticket reopening patterns, and customer satisfaction ratings.

The goal is to identify patterns in customer support operations, highlight areas that may require improvement, and demonstrate how Python can be used to extract meaningful insights from structured data.

## Project Objectives

- Analyze the distribution of support tickets across different queues and priority levels.
- Calculate average first-response times across ticket priorities.
- Examine the availability of resolution timestamps.
- Evaluate customer satisfaction ratings.
- Investigate ticket reopening patterns.
- Identify missing and invalid data values.

## Dataset Description

The project uses a customer support ticket dataset containing 4,000 records. Each record represents an individual support ticket.

The dataset includes the following fields:

| Column | Description |
|---|---|
| `ticket_id` | Unique ticket identifier |
| `opened_at` | Date and time the ticket was opened |
| `channel` | Channel through which the ticket was submitted |
| `queue` | Support team responsible for the ticket |
| `priority` | Assigned ticket priority |
| `subject` | Brief description of the customer's issue |
| `first_response_min` | Time taken to provide the first response, in minutes |
| `resolved_at` | Recorded resolution date and time |
| `reopened` | Indicates whether the ticket was reopened |
| `csat` | Customer satisfaction rating |

## Tools and Technologies

- **Python:** Used to analyze the dataset and calculate performance metrics.
- **CSV module:** Used to read and process structured CSV records.
- **Pathlib:** Used to manage file paths and locate the dataset.
- **Visual Studio Code:** Used as the development environment.

## Python Concepts Applied

- Variables and data types
- Lists and dictionaries
- Loops and conditional statements
- Functions and reusable code
- File handling
- Exception handling
- Data validation
- Basic statistical calculations

## Key Findings

### 1. Ticket Distribution

A total of 4,000 support tickets were analyzed across five support queues.

| Support Queue | Number of Tickets |
|---|---:|
| Technical | 1,282 |
| Billing | 960 |
| Account | 647 |
| Onboarding | 586 |
| Integrations | 525 |

The technical queue recorded the highest ticket volume, accounting for approximately 32% of all tickets.

### 2. First Response Time

Average first-response times varied across ticket priorities.

| Priority | Average Response Time |
|---|---:|
| Urgent | 25.11 minutes |
| High | 68.46 minutes |
| Normal | 149.50 minutes |
| Low | 302.62 minutes |

Urgent tickets received the fastest average first response, while low-priority tickets had the longest.

### 3. Customer Satisfaction

The overall average customer satisfaction score was **3.99 out of 5**, based on 1,226 recorded ratings.

Satisfaction varied across support queues:

- Integrations: 4.24/5
- Account: 4.08/5
- Onboarding: 4.01/5
- Billing: 3.95/5
- Technical: 3.85/5

The technical queue recorded the lowest average satisfaction score, suggesting an area worth investigating further.

### 4. Ticket Reopening

- Reopened tickets: 285
- Tickets not reopened: 3,715
- Reopening rate: 7.12%

### 5. Data Quality

The analysis identified missing values in several important fields:

| Field | Missing Records |
|---|---:|
| First response time | 149 |
| Resolution timestamp | 225 |
| Customer satisfaction rating | 2,774 |

All 1,226 recorded customer satisfaction ratings passed validation, falling within the expected range of 1–5.

## How to Run the Project

### Requirements

- Python 3 installed on your computer.
- The project files downloaded or cloned from this repository.

### Setup Instructions

1. Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

2. Navigate into the project folder:

```bash
cd customer-support-ticket-analyzer
```

3. Run the Python program:

```bash
python3 main.py
```

The program will load the CSV dataset and display the analysis results in the terminal.

## Project Limitations

- The analysis is based on the supplied dataset and may not represent the performance of an actual customer support organization.
- A large proportion of customer satisfaction ratings are missing, which limits the coverage of satisfaction analysis.
- Missing resolution timestamps do not necessarily confirm that tickets were unresolved.
- The project uses basic Python data processing and statistical calculations. More advanced visualizations and predictive analysis are outside its current scope.

## Future Improvements

- Add data visualizations to make findings easier to interpret.
- Explore additional performance indicators.
- Improve