# Gutendex API

## Running the service

Use docker compose to run the service. <br>

`docker compose up`

## Using the endpoints

<br>

### Searching a book by name

`curl --location --request GET 'http://localhost:5000/api/v1/books?title=A Treatise Concerning'`

<br>



### Create a review about some book

`curl --location --request POST 'http://localhost:5000/api/v1/books/84/review' \
--header 'Content-Type: application/json' \
--data-raw '{
    "bookId": 84,
    "rating": 5,
    "description": "Very good book"
}'`

<br>

### Get book details

`curl --location --request GET 'http://localhost:5000/api/v1/books/84'`

<br>

## Tests

Run tests using pytest. The docker containers should be UP before you start running the tests. You also should export the following env variable in your current environment (outside the container).

- DATABASE_URL=postgresql://postgres:leotarla@localhost:5432/postgres <br>

Now, run the tests: <br>

`pytest tests/`


## Scalable architecture diagram

A high-level scalable architecture diagram can be found [here](https://drive.google.com/file/d/1-ly-Ofqt8kf211gNSKqfTKwr8LWPPaTh/view?usp=share_link).