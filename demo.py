from haystack.document_stores import InMemoryDocumentStore
from haystack.utils import build_pipeline, add_example_data, print_answers
from config import API_KEY


# can choose from: "anthropic", "cohere", "huggingface", and "openai".
provider = "openai"

document_store = InMemoryDocumentStore(use_bm25=True)

add_example_data(document_store, "data/People")

pipeline = build_pipeline(provider, API_KEY, document_store)

result = pipeline.run(query="What is the difference between Marco and Luigi?")

print_answers(result, details="medium")
