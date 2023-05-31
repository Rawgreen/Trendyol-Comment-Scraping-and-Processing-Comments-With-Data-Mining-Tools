import re
import csv
import requests

# API URL for retrieving product reviews
API = "https://public-mdc.trendyol.com/discovery-web-socialgw-service/api/review/{id}?page={page}"

def main():
    # Prompt user for Trendyol product URL
    url = input("URL: ")

    # Retrieve comments using the provided URL
    comments = get_comments(url)

    # Write comments to a CSV file
    write_csv(comments["id"], comments["comments"])


def get_comments(url):
    # Extract product ID from the provided URL using regex
    regex = re.search("-p-(\\d+)", url)
    product_id = regex.group(1)

    # Create a session object for making HTTP requests
    session = requests.Session()

    # Initialize an empty list to store comments
    comments = []

    # Start from page 0 and retrieve comments until there are no more reviews
    page = 0
    while True:
        # Send a GET request to the Trendyol API to retrieve reviews
        response = session.get(API.format(id=product_id, page=page))
        json_data = response.json()

        # Extract the product reviews from the JSON response
        reviews_raw = json_data["result"]["productReviews"]

        # If there are no reviews, break out of the loop
        if reviews_raw is None:
            break

        # Extract comments and ratings from each review and add them to the list
        comments_raw = reviews_raw["content"]
        for comment in comments_raw:
            comments.append({"rate": comment["rate"], "comment": comment["comment"]})

        # Print progress message indicating the page number
        print("Page #{} done".format(page))

        # Move to the next page
        page += 1

    # Return a dictionary containing the product ID and the list of comments
    return {"id": product_id, "comments": comments}


def write_csv(product_id, comments):
    # Create a CSV file with the name as the product ID
    filename = '{}.csv'.format(product_id)

    # Open the file in write mode
    with open(filename, 'w', newline='', encoding="utf-8") as csvfile:
        # Define the field names for the CSV file
        fieldnames = ['rate', 'comment']

        # Create a CSV writer and write the header row
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        # Write each comment as a row in the CSV file
        for row in comments:
            writer.writerow(row)

    # Print a message indicating successful saving of comments to the CSV file
    print("Comments saved to '{}'".format(filename))


if __name__ == "__main__":
    main()
