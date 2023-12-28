from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import build_pipeline, add_example_data, print_answers

# We are model agnostic :) Here, you can choose from: "anthropic", "cohere", "huggingface", and "openai".
provider = "openai"
API_KEY = "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"

document_store = InMemoryDocumentStore(use_bm25=True)

add_example_data(document_store, "data/Antonio")

pipeline = build_pipeline(provider, API_KEY, document_store)

# Ask a question on the data you just added.
result = pipeline.run(query="What is the difference between Antonio and Luigi? If I have to choose one of them to work as a developer for my site, whom do you suggest?")

print_answers(result, details="medium")
