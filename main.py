# main.py

# imports go here


# ============== SETTINGS ==============
HTML_FILE = ""              
OUTPUT_FILE = ""

# Simple CSS selectors that should match sample_page.html - these will be used in <steps x>
ITEM_SELECTOR = ".card"                      # each repeated item container
TITLE_SELECTOR = "h2"                        # inside each card
PRICE_SELECTOR = ".price"                    # inside each card
LINK_SELECTOR  = "a"                         # inside each card
# ===================================================

# ---------------------------------------------------
# STEP 1: Import libraries, configured settings and verify environment 
# ---------------------------------------------------
print("Step 1: Starter loaded. Review settings above and confirm they match your HTML.")



# ---------------------------------------------------
# STEP 2: Load HTML from local file 
# ---------------------------------------------------
print("Step 2: Load HTML from local file...")



# ---------------------------------------------------
# STEP 3: Define your JSON schema 
# ---------------------------------------------------
print("Step 3: Define your schema with make_item...")



# ---------------------------------------------------
# STEP 4A: Parse HTML and locate repeated blocks 
# ---------------------------------------------------
print("Step 4A: Locate repeated blocks with ITEM_SELECTOR...")
# TODO: Create a BeautifulSoup object from html_text, then select with ITEM_SELECTOR.



# ---------------------------------------------------
# STEP 4B: Extract fields from each block and build result dicts 
# ---------------------------------------------------
print("Step 4B: Extract fields (title, price, url) from each block...")
# TODO: For each element in `blocks`, select TITLE_SELECTOR / PRICE_SELECTOR / LINK_SELECTOR,
#       get text/attributes, and append dicts with identical keys.



# ---------------------------------------------------
# STEP 5 — Save results to JSON
# ---------------------------------------------------
print("Step 5: Save your cleaned results to a JSON file...")

# TODO: Save results to OUTPUT_FILE with json.dump()



# ---------------------------------------------------
# STEP 6 (Stretch) — Switch to a live URL
# ---------------------------------------------------
print("Step 6: (Stretch) Refactor get_html to fetch live URLs...")
# TODO: Add requests logic to support both files and URLs



# ---------------------------------------------------
# Scaffold complete
# ---------------------------------------------------
print("Scaffold complete. Add code at each TODO to implement the steps.")
