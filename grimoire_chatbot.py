import os
from flask import Flask, request, jsonify
import markdown2

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    user_query = data.get('query')

    if 'hello' in user_query.lower():
        return jsonify({
            "response": "Hello! Would you like an introduction? You can also access Grimoire.md, commands, Readme.md, or upload a picture."
        })

    response = process_query(user_query)
    return jsonify({"response": response})

def process_query(query):
    response = ""
    if query.startswith("P "):
        response = read_grimoire_file(query[2:])
    elif query.startswith("K "):
        response = display_hotkeys()
    elif query.startswith("R "):
        response = read_readme_file()
    elif query.startswith("upload"):
        response = "Please upload a picture."
    else:
        response = "I am Grimoire, your Code Wizard. How can I assist you with your coding needs today?"

    return response

def read_grimoire_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return markdown2.markdown(content)
    except FileNotFoundError:
        return f"File {filename} not found."

def display_hotkeys():
    return """
    ### Hotkeys & Actions

    **Navigation & Iteration**
    - **W:** Yes, Continue – Confirm, advance, proceed.
    - **A:** Alt – Provide 2-3 alternative approaches, compare & rank.
    - **S:** Explain – Explain each line of code step by step with comments.
    - **D:** Iterate, Improve, Evolve – Identify three critiques or edge cases, propose improvements.

    **Planning & Debugging**
    - **Q:** Question – Help build intuition about a concept.
    - **E:** Expand – Break down the implementation into smaller steps.
    - **SS:** Explain Simply – Simplify explanation for beginners.
    - **SOS:** Generate search queries – Provide Google, Stack Overflow, and Perplexity queries for deeper learning.
    - **T:** Test Cases – List ten test cases and step through them.
    - **F:** Fix – Debug the code systematically.
    - **H:** Help Debug – Add print/debugging lines.
    - **J:** Run Code – Execute in a Jupyter notebook.
    - **B:** Search – Use the web tool to fetch updated information.

    **Exporting & Deployment**
    - **Z:** Write completed code to files, zip them for download.
    - **G:** Stash sandbox – Save files for later retrieval.
    - **REPL:** Replit Auto Deploy – Instantly export to Replit for live testing.
    - **N:** Netlify Auto Deploy – Instantly deploy a static site.
    - **ND:** Netlify Drop – Manually deploy by dragging and dropping a ZIP file.
    - **C:** Code Mode – Write code only, no explanations.
    - **V:** Split Code – Break into smaller code blocks for easier copying.
    - **VV:** Divide into Sub-functions – Organize code into well-defined functions.
    - **PDF:** Generate a PDF file for download.
    - **L:** Tweet – Generate a formatted tweet link.

    **Advanced Features & Special Modes**
    - **X:** Side Quest – Explore tangentially related topics.
    - **PN:** Display Patch Notes.
    - **KT:** Visit GPTavern.md – Display all links & URLs.
    - **KY:** Display Recommended Tools.
    """

def read_readme_file():
    try:
        with open('Readme.md', 'r') as file:
            content = file.read()
        return markdown2.markdown(content)
    except FileNotFoundError:
        return "Readme.md file not found."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)