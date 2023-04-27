# Retry example

Web scraping and APIs are methods to obtain data from websites and servers. APIs are predefined routes for accessing data from a web server in a structured way, whereas web scraping refers to extracting data from a web page by parsing its HTML content.

When scraping websites, the process can be broken every time there is a connection problem, which can happen for several reasons, such as server maintenance or temporary network issues. To avoid this issue, we can use a retry function to attempt to obtain a valid response from the server.

The code above provides an example of how to use a retry function to scrape Google search results for a list of words using the Python requests and BeautifulSoup libraries. The function *get_result* fetches the HTML of the Google search results page for a given word. If a connection error occurs, the function will retry the request up to *MAX_RETRIES* times, waiting 45 seconds between each attempt.

The *for* loop at the bottom of the code calls *get_result* for each word in *LIST_OF_WORDS* and assigns the returned HTML to *results*. If all retry attempts fail, *result_html* is set to "Error", and the process continues with the next word in *LIST_OF_WORDS*.

In summary, using a retry function is a useful technique for web scraping when dealing with unreliable network connections. It allows us to make several attempts to obtain the desired data without breaking the scraping process, improving the reliability of our code.
