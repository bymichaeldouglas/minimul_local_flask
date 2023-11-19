This is the starter flask app that can manipulate local information and uses the browser to seamlessly interact with other stuff


the minimum is 

requirements.txt
app.py (heart of the app)
index.html (web page info in a folder named Templates)

running the app.py file will start a flask app that displays your html file in your browser


you can style it by adding this directly under </scripts>

<style>
        body {
            text-align: center; /* Center align elements */
            padding-top: 50px; /* Add some space at the top */
        }
        #overlayImage {
            max-width: 80%; /* Limit image width to 80% of its parent */
            height: auto; /* Keep image aspect ratio */
            margin-bottom: 30px; /* Space between image and form */
        }
        .container {
            width: 80%;
            margin: auto; /* Center align the container */
        }
</style>

here are the changes to alter the parts colors


<style>
body {
    text-align: center; /* Center align elements */
    padding-top: 50px; /* Add some space at the top */
    background-color: #121212; /* Dark background for dark mode */
    color: #ffffff; /* Light text color for contrast */
}

#overlayImage {
    max-width: 80%; /* Limit image width to 80% of its parent */
    height: auto; /* Keep image aspect ratio */
    margin-bottom: 30px; /* Space between image and form */
}

.container {
    width: 80%;
    margin: auto; /* Center align the container */
    background-color: #1e1e1e; /* Slightly lighter background for the container */
    padding: 20px; /* Padding inside the container */
    border-radius: 10px; /* Rounded corners for the container */
}
</style>
