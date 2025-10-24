# Solution Code - Web Scraping to JSON

<details>
<summary> Step 1 Solution - Import Python Dependencies</summary>
Python - main.py

```python
# main.py

# Standard library imports
import os     # for working with file paths
import json   # for saving Python data as JSON

# Third-party imports (install with pip if missing)
from bs4 import BeautifulSoup  # for parsing HTML
```
    


</details>

<details>
<summary>Step 2 Solution – Write get_html(source) to Load HTML from a File</summary>
Python - main.py

```python
# STEP 2 — helper to load HTML from a local file
def get_html(source):
    """
    Open the sample HTML file and return its contents as text.
    """
    # The open() function is part of Python's standard library.
    # It lets you read files saved on your computer.
    with open(source, "r", encoding="utf-8") as f:
        html_text = f.read()

    # Simple check: print out how many characters were loaded
    print("Loaded HTML with", len(html_text), "characters")
    return html_text

# Example usage after defining HTML_FILE:
# html_text = get_html(HTML_FILE)
```


</details>  
<details>
<summary>Step 3 Solution – Create a Template for Each Item</summary>
Python - main.py

```python
def make_item(title, price, url):
	return {"title": title, "price":price, "url":url}
```

</details>   

<details>
<summary> Step 4A Solution – TKTK</summary>
Python - main.py

```python
# ---------------------------------------------------
# STEP 4A: Parse HTML and locate repeated blocks 
# ---------------------------------------------------
soup = BeautifulSoup(html_text, "html.parser")
blocks = soup.select(ITEM_SELECTOR)

print("[STEP 4A] Found", len(blocks), "blocks")
```
</details>   



<details>
<summary> Step 4B Solution – Use BeautifulSoup to Search the HTML</summary>
Python - main.py

```python

# ---------------------------------------------------
# STEP 4B: Extract fields from each block and build result dicts
# ---------------------------------------------------

results = []  # list to hold one dict per product

for block in blocks:
    # Find the child elements inside each product block
    title_el = block.select_one(TITLE_SELECTOR)   # e.g., "h2"
    price_el = block.select_one(PRICE_SELECTOR)   # e.g., ".price"
    link_el  = block.select_one(LINK_SELECTOR)    # e.g., "a"

    # Get the text values and clean up any stray whitespace 
    title = title_el.get_text(strip=True)
    price = price_el.get_text(strip=True)
    url   = link_el.get("href")

    # Build a consistent dict and store it
    item = make_item(title, price, url)
    results.append(item)

# Confirm results
print("[STEP 4B] Extracted", len(results), "items")
if results:
    print("[STEP 4B] First item preview:", results[0])

```
</details>   



<details>
<summary> Step 5 Solution – Extract Content from Each HTML Block</summary>
Python - main.py

```python
# STEP 5 — Save your cleaned results to a JSON file

OUTPUT_FILE = "data.json"  # define this at the top of your file

# Write the results list to a JSON file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("[STEP 5] Saved", len(results), "items to", OUTPUT_FILE)

```

</details>   


<details>
<summary>Step 6 - Save Your Cleaned results to a JSON File (Optional/Stretch)</summary>
Python - main.py

```python
# ---------------------------------------------------
# STEP 6 (Stretch) — Switch to a live URL
# ---------------------------------------------------
print("Step 6: (Stretch) Refactor get_html to fetch live URLs...")

# TODO: Add requests logic to support both files and URLs

def get_html(source):
    if source.startswith("http"):
        response = requests.get(source)
        return response.text
    else:
        with open(source, "r", encoding="utf-8") as f:
            return f.read()


```
</details>


<details>
<summary> Final Solution</summary>
Python - main.py

```python
# main.py

# ================== IMPORTS ==================
# Standard library
import os     # for file paths
import json   # for saving Python data as JSON

# Third-party libraries
from bs4 import BeautifulSoup  # uncomment in Step 1 after installing
# =============================================

# ================== SETTINGS =================
HTML_FILE = "sample_page.html"   # local file you’ll start with
OUTPUT_FILE = "data.json"        # output file

# CSS selectors for sample_page.html
ITEM_SELECTOR = ".card"
TITLE_SELECTOR = "h2"
PRICE_SELECTOR = ".price"
LINK_SELECTOR = "a"
# =============================================

# ---------------------------------------------------
# STEP 1 — Import libraries and verify scaffold
# ---------------------------------------------------
print("Step 1: Starter loaded. Review settings above and confirm they match your HTML.")

# ---------------------------------------------------
# STEP 2 — Load HTML from local file
# ---------------------------------------------------
print("Step 2: Load HTML from local file...")

# TODO: Define get_html(source) here
def get_html(source):
    with open(source, "r", encoding="utf-8") as f:
        html_text = f.read()
    print('Loaded HTML with', len(html_text), 'characters')
    return html_text

html_text = get_html(HTML_FILE)

# ---------------------------------------------------
# STEP 3 — Define your JSON schema
# ---------------------------------------------------
print("Step 3: Define your schema with make_item...")

# TODO: Define make_item(title, price, url) here
def make_item(title, price, url):
    return {"title": title, "price": price, "url": url}

example_item = make_item("EXAMPLE", "$0.00", "https://example.com")
print("[STEP 3] Schema preview:", json.dumps([example_item], indent=2))

# ---------------------------------------------------
# STEP 4A — Parse HTML and locate repeated blocks
# ---------------------------------------------------
print("Step 4A: Locate repeated blocks with ITEM_SELECTOR...")

# TODO: Create a BeautifulSoup object and select ITEM_SELECTOR
soup = BeautifulSoup(html_text, "html.parser")
blocks = soup.select(ITEM_SELECTOR)
print("[STEP 4A] Found", len(blocks), "blocks")

# ---------------------------------------------------
# STEP 4B — Extract fields from each block
# ---------------------------------------------------
print("Step 4B: Extract fields (title, price, url) from each block...")

# TODO: Loop over blocks and extract title, price, and link
results = []
for block in blocks:
    title_el = block.select_one(TITLE_SELECTOR)
    price_el = block.select_one(PRICE_SELECTOR)
    link_el = block.select_one(LINK_SELECTOR)

    title = title_el.get_text(strip=True)
    price = price_el.get_text(strip=True)
    url = link_el.get("href")

    item = make_item(title, price, url)
    results.append(item)

print("[STEP 4B] Extracted", len(results), "items")
if results:
    print("[STEP 4B] First item preview:", results[0])

# ---------------------------------------------------
# STEP 5 — Save results to JSON
# ---------------------------------------------------
print("Step 5: Save your cleaned results to a JSON file...")

# TODO: Save results to OUTPUT_FILE with json.dump()
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2)

print("[STEP 5] Saved", len(results), "items to", OUTPUT_FILE)

```
</details>   



