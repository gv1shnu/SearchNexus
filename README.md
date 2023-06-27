# Search Nexus

Search Nexus is a flask-based application that allows users to perform searches across multiple search engines simultaneously and view the results in one place.

## Features

- Perform searches across multiple search engines simultaneously.
- View search results from various search engines in one consolidated view.
- Experimental in nature.

## Usage

- Download SearchNexus application directly from [here](https://drive.google.com/file/d/1fmbicfMMcl1JeaqiIOYOltmZAEz-CWah/view?usp=sharing).
- Enter your search query in the search box on the home page.
- Press Enter to initiate the search.
- Search results from multiple search engines will be displayed within seconds.

**Note**: Make sure Chrome is your default browser. It helps. 

## Screenshots

![Screenshot (1)](https://github.com/gv1shnu/SearchNexus/assets/121789146/98b0fee5-2b3f-4e04-b81f-2b9d08c4e101)

![Screenshot (1-1)](https://github.com/gv1shnu/SearchNexus/assets/121789146/3a5fa9a6-af2e-4574-904d-395ddcea1659)

![Screenshot (2)](https://github.com/gv1shnu/SearchNexus/assets/121789146/a86d71a9-a595-425f-8dc6-e8b49cae0c20)

![Screenshot (2-5)](https://github.com/gv1shnu/SearchNexus/assets/121789146/5e85b02a-aacf-4dd4-9e42-32c9b11dfdf6)

![Screenshot (17)](https://github.com/gv1shnu/SearchNexus/assets/121789146/c8669de2-864c-4ead-8473-bc34142ee18c)

![Screenshot (16)](https://github.com/gv1shnu/SearchNexus/assets/121789146/b8fc27dd-4e27-4147-a8c4-b1dd40ffe02d)

![Screenshot (18)](https://github.com/gv1shnu/SearchNexus/assets/121789146/ecc9d9fa-560b-4506-a91d-6d0a41761197)

![Screenshot (19)](https://github.com/gv1shnu/SearchNexus/assets/121789146/4a596a83-ac35-477e-a55a-f4345ed67965)


## Installation

Follow these steps to set up and run the Search Nexus Flask application:

1. Clone the repository:
	
   		git clone https://github.com/gv1shnu/SearchNexus.git


2. Navigate to the project directory:
	
   		cd SearchNexus


3. To run this project, make sure you have Python 3.11 and pip installed on your system. Install the required dependencies:
	
		pip install -r requirements.txt


4. Start the Flask development server:

		python app.py

## Technologies Used

- Flask: A micro web framework for Python programming language.
- HTML5: The markup language used for structuring the web pages.
- CSS3: The stylesheet language used for styling the web pages.

## Limitations

- The search results may not always be consistent across different search engines due to variations in algorithms and indexing.
- The application relies on the availability and performance of the search engines it queries.
- The application currently supports a predefined set of search engines and cannot dynamically add or remove search engines.

## Contributing

Contributions and code reviews are welcome! 

TODO
----
- [ ] Update the blurry icon
- [ ] Order rank-wise
- [x] Center the result-container div
- [x] Properly scrape for YouTube video description again
- [ ] Add more search engines
- [ ] Pagination
- [ ] Change the background of success.html
- [x] Organize displayed search results more comprehensively (card style)

## License

This project is licensed under the [MIT License](LICENSE).
