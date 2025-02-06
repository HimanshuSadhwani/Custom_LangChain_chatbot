from langchain.document_loaders import UnstructuredURLLoader

def extract_course_data():
    urls = ["https://brainlox.com/courses/category/technical"]
    loader = UnstructuredURLLoader(urls=urls)
    documents = loader.load()
    return documents

if __name__ == "__main__":
    data = extract_course_data()
    print("Extracted Data:", data[:2])  # Show a preview
