# Auteur : Pelpav
# Date : 06/07/24
# Description : Main file of my Python project

# Import necessary modules
from database import DatabaseManager  # Manages the database connection
from models import Citation  # Data model for a quote
from utils import CitationGenerator
import tkinter as tk

# Define the main function
def main():
    # Create an instance of DatabaseManager with your database connection parameters
    db_manager = DatabaseManager('localhost', 'root', '', 'citations')

    # Create an instance of CitationGenerator with your DatabaseManager
    citation_generator = CitationGenerator(db_manager)

    # Create a new Tkinter window
    window = tk.Tk()
    window.geometry("900x200")  # Set a fixed size for the window

    # Create a frame to contain the quote and author labels
    frame = tk.Frame(window)
    window.title("QuoteGenerator-Pelpav")
    frame.pack()

    # Create a label to display the quote
    quote_label = tk.Label(frame, font=("Helvetica", 16))
    quote_label.pack()

    # Create a label to display the author and source
    author_label = tk.Label(frame, font=("Helvetica", 14, "italic"), anchor="w")
    author_label.pack(fill="both")

    # Create a button that will generate a quote when clicked
    button = tk.Button(window, text="Générer une citation", command=lambda: generate_citation(citation_generator, quote_label, author_label))

    # Add the button to the window at the bottom
    button.pack(side=tk.BOTTOM)

    # Add the button to the window
    button.pack()

    # Start the Tkinter event loop
    window.mainloop()

    # Don't forget to close the database connection when you're done
    db_manager.close_connection()
def generate_citation(citation_generator, quote_label, author_label):
    # Generate a quote
    citation = citation_generator.generate_citation()

    # Display the quote and author in the labels
    if citation is not None:
        quote_label.config(text=citation.citation)  # assuming the Citation class has a 'quote' attribute
        author_label.config(text=f"{citation.auteur}, {citation.theme}")  # assuming the Citation class has 'author' and 'source' attributes
    else:
        quote_label.config(text="No quote could be generated.")
        author_label.config(text="")

# If this script is run directly, call the main function
if __name__ == "__main__":
    main()
