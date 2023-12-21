from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import build_pipeline, add_example_data, print_answers

# We are model agnostic :) Here, you can choose from: "anthropic", "cohere", "huggingface", and "openai".
provider = "openai"
API_KEY = "xxx"

document_store = InMemoryDocumentStore(use_bm25=True)

add_example_data(document_store, "data/GoT_getting_started")

pipeline = build_pipeline(provider, API_KEY, document_store)

# Ask a question on the data you just added.
result = pipeline.run(query="Who is the father of Arya Stark?")

print_answers(result, details="medium")
