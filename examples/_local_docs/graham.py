from gpt_index import GPTSimpleVectorIndex, SimpleDirectoryReader
from IPython.display import Markdown, display
import argparse

# Load the data from the 'data' directory using the SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()

# Create an index using the GPTSimpleVectorIndex class and the loaded data
index = GPTSimpleVectorIndex(documents)

#### Query the index with the given string and store the response in the 'response' variable
# response = index.query("Give a brief summary of the author. Provide 1 paragraph summary and 3 main bullet points?")

# Print the response
# print(response)


# Create an ArgumentParser object and add an argument for the query string
parser = argparse.ArgumentParser()
parser.add_argument('query', type=str, help='The query to be passed to the index.query function')

# Parse the command-line arguments
args = parser.parse_args()

# Query the index with the given string and store the response in the 'response' variable
response = index.query(args.query)

# Print the response
print(response)
