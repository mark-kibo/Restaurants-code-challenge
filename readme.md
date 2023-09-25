# Yelp-Style Domain Assignment

In this assignment, we will work with a Yelp-style domain consisting of three models:

1. `Restaurant`
2. `Customer`
3. `Review`

## Model Relationships

- A `Restaurant` has many `Reviews`.
- A `Customer` has many `Reviews`.
- A `Review` belongs to both a `Customer` and a `Restaurant`.

The relationship between `Restaurant` and `Customer` forms a many-to-many relationship.

## Deliverables

You are required to implement the following methods in the respective classes. Feel free to create additional helper methods if needed.

### Customer

- `Customer __init__(self, given_name, family_name)`
  - Initializes a customer with a given name and family name, both as strings (e.g., first and last name, like "George Washington").

- `Customer given_name(self, new_given_name=None)`
  - Returns the customer's given name.
  - Allows for changing the given name if `new_given_name` is provided.

- `Customer family_name(self, new_family_name=None)`
  - Returns the customer's family name.
  - Allows for changing the family name if `new_family_name` is provided.

- `Customer full_name(self)`
  - Returns the full name of the customer, with the given name and family name concatenated in Western style.

- `Customer all()`
  - Returns a list of all customer instances.

### Restaurant

- `Restaurant __init__(self, name)`
  - Initializes a restaurant with a name as a string.

- `Restaurant name(self)`
  - Returns the restaurant's name.
  - The name cannot be changed after the restaurant is created.

### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Initializes a review with a customer, a restaurant, and a rating (a number).

- `Review rating(self)`
  - Returns the rating for the review.

- `Review all()`
  - Returns a list of all reviews.

### Object Relationship Methods

#### Review

- `Review customer(self)`
  - Returns the customer object associated with the review.
  - Once a review is created, the customer cannot be changed.

- `Review restaurant(self)`
  - Returns the restaurant object associated with the review.
  - Once a review is created, the restaurant cannot be changed.

#### Restaurant

- `Restaurant reviews(self)`
  - Returns a list of all reviews for that restaurant.

- `Restaurant customers(self)`
  - Returns a unique list of all customers who have reviewed the restaurant.

#### Customer

- `Customer restaurants(self)`
  - Returns a unique list of all restaurants that the customer has reviewed.

- `Customer add_review(self, restaurant, rating)`
  - Given a restaurant object and a star rating (as an integer), creates a new review and associates it with that customer and restaurant.

### Aggregate and Association Methods

#### Customer

- `Customer num_reviews(self)`
  - Returns the total number of reviews that a customer has authored.

- `Customer find_by_name(cls, name)`
  - Given a string representing a full name, returns the first customer whose full name matches.

- `Customer find_all_by_given_name(cls, name)`
  - Given a string representing a given name, returns a list containing all customers with that given name.

#### Restaurant

- `Restaurant average_star_rating(self)`
  - Returns the average star rating for the restaurant based on its reviews.
  - The average is calculated by summing all ratings and dividing by the number of ratings.

