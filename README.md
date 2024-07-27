# API test TCB

This is the project that solve the test below:

Deliverable:

- Write a REST API with two POST endpoints

- First POST endpoint receives a JSON in the form of a document with two fields: a pool-id (numeric) and a pool-values (array of values) and is meant to append (if pool already exists) or insert (new pool) the values to the appropriate pool (as per the id):

  e.g.

        {
           "poolId": 123546,
           "poolValues": [1, 7, 2, 6]
        }

- Second POST is meant to query a pool, the two fields are pool-id (numeric) identifying the queried pool, and a quantile (in percentile form)

e.g.

        {
           "poolId": 123546,
           "percentile":99.5
        }

- The response from the append is a status field confirming "appended" or "inserted".

- The response from the query has two fields: the calculated quantile and the total count of elements in the pool

- Please do not use a library for the quantile calculation if a pool contains less than 100 values.

- Focus on high performance if possible (time permitting) and resiliency

- Reasoning about high-availability and scalability is a nice-to-have

- No database; no connection to anything needed. Keep it simple.

- Your preferred language. The programming language does not need to be a systems language (that performs by definition), so no C/C++/Rust needed (unless this is your preference), really up to you (Python, Go, Java, Scala, ...).

- Build it from scratch, please don’t copy, do it by yourself

### General guidelines
- Keep it very simple, clean [architecture and code], don’t forget about testing, documentation, instructions, focus on a full deliverable and strictly on what matters, nothing more nothing less; you will be evaluated on these.

- Don’t spend more than 3-4 hours. Deadline is 4-5 days after receiving the homework, we are considerate of the fact that you have a full-time job and a life. If you can finish earlier even better.

## Execution Plan

1. Requirements
- Build REST API with two POST endpoints
- There are two API with two specific task:
    + **Append or Insert a pool of value**: Form of a document with two fields: a pool-id (numeric) and a pool-values (array of values) and is meant to append (if pool already exists) or insert (new pool) the values to the appropriate pool (as per the id)
    + **Query a pool**: Result returns two fields are pool-id (numeric) identifying the queried pool, and a quantile (in percentile form)
        * ***Quantile definition**: A quantile defines a particular part of a data set, i.e., a quantile determines how many values in a distribution are above or below a certain limit. General quantiles include the median (50th percentile), quartiles (25th, 50th, and 75th percentiles), and percentiles (values ranging from 0 to 100).*

2. Definition of Done (DoD)
* For Append and Insert API, the application needs to temporarily store the data and return the state of API result, which is confirming "appended" or "inserted".
* For query API, the application needs to calculate the quantile and return the result, including calculated quantile and the total count of elements in the pool.

3. Executtion plan
    **a. API implementation:**
    * We will use Flask route method to create the API and host the application in localhost at port 5000 (default port)
    * There are two routes to the API, which are two APIs for task on previous description:
        * localhost:5000/append: This api will append/insert pool in body payload into "In-memory database" (which is dictionary).
        * localhost:5000/query: This api will access the pool id from "In-memory database" and calculate the quantile of the pool, then return the result.

    **b. Calculate quantile:**
    **The steps for calculating the quantiles involved:**
    * Sorting the Data: Arrange the dataset in increasing order.
    * Determine the Position: Calculate the position of the desired quantile based on the given formula: \(position = \frac{\text{percentile} \times (n + 1)}{100}\)
        - n: total number of observations.
    * Interpolation (if needed): Interpolate between two adjacent values to find the quantile if the position is not an integer.

    **Detail calculation steps:**
    - Step 1: Sorting the list: using sorted() method
    - Step 2: Calculate Position and Quantile value
    + If the position is interger:
        + \(\text{position} = \frac{\text{percentile} \times (n + 1)}{100}\)
        + Quantile = Value at position in list
    + If the position is not an integer, calculate in interpolation way involved more few steps below:
        + Identify floor and ceil values of position
        + Calculate the fractional part, where \( fraction = position - floor\)
        + Calculate \(\text{Quantile} = \text{Value at floor position} + (\text{Value at ceiling position} - \text{Value at floor position}) \times \text{Fractional Part}\)

## Running and testing
1. Setting the environment: All packages are listed in the requirements.txt file, all you need is to create a python virtual environment and run pip install -r requirements.txt.
2. Setting the application: The app can be run with simple command in bash:
python3 api.py
3. Testing the application: After running the app, you can use Postman or any API platform for building and using APIs to use the api, including:
    * [localhost:5000/append](http://localhost:5000/append): This api will append/insert pool in body payload has two keys name: "poolID" and "percentile"
    * [localhost:5000/query](http://127.0.0.1:5000/query): This api will access the pool id from "In-memory database" and calculate the quantile of the pool, then return the result. The body is dictionary with two keys: "poolID" and "percentile"