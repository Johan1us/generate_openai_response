# Readme for generate_openai_response function
## Prerequisite

This function is hosted on Google Cloud Platform and requires a few prerequisite steps before deployment. These include:

- A Google Cloud Platform account and project setup.
- Access to Firestore to store the settings and prompt for the OpenAI api call.
- An OpenAI API key.

## Workflow

The generate_openai_response function takes an HTTP request as input and returns an HTTP response with the generated response from the OpenAI api call. Here are the steps in the workflow:

- Extract the tag and user message from the request. 
- Use the tag to retrieve the Firestore document containing the settings and prompt for the OpenAI api call. 
- Replace the << QUERY >> placeholder in the prompt with the user message.
- Make an api call to OpenAI with the settings and prompt.
- Return the generated response in the HTTP response.

## Setup cloud functions

To deploy this function on Google Cloud Functions, follow these steps:

- Create a new function in the Google Cloud Console.
- Set the trigger type to HTTP and provide the name of the function.
- Copy the code into the inline editor or upload the code as a zip file.
- Set the function to use Python 3.7 runtime.
- Add the following environment variable OPENAI_API_KEY with your OpenAI API key.
- Save and deploy the function.

## Setup local

To run this function locally, follow these steps:

- Install the required dependencies listed in requirements.txt.
- Set the OPENAI_API_KEY environment variable with your OpenAI API key.
- Run the command functions-framework --target generate_openai_response --debug.

## Local testing with Pycharm

- Open main.py file in Pycharm.
- Install the required dependencies listed in requirements.txt.
- Set the OPENAI_API_KEY environment variable with your OpenAI API key.
- Run the generate_openai_response function with test inputs.
- The output will be displayed in the console.

## Files

- main.py: Contains the generate_openai_response function.
- requirements.txt: Contains the list of required Python packages.
- test.http: Contains sample HTTP request and response for testing.

## Dependencies

- firebase-admin
- openai 
- functions-framework

## Keys

This function requires the following environment variables:

- OPENAI_API_KEY: Your OpenAI API key.

## Usage

The generate_openai_response function is triggered by an HTTP request and returns an HTTP response with the generated response from the OpenAI api call. The HTTP request should have the following JSON payload:

json

    {
    "fulfillmentInfo": {
        "tag": "collection - document"
    },
    "text": "User message"
    }

- tag: The tag used to retrieve the settings and prompt from Firestore.
- text: The user message to be used as input to the OpenAI api call.

## Deployment

To deploy this function on Google Cloud Functions, see the "Setup cloud functions" section above.
