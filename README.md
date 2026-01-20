<h3 align="center">ParaSite</h3>

<p align="center">
  Taxonomy and visualization tool for parasite phyla
</p>

---

## Overview  
Navigate parasite classes, view species lists, & fetch real-time taxonomy data from NCBI Taxonomy Database.
### Species Tab
<img width="500" height="500" alt="Screenshot 2026-01-20 at 8 54 55 AM" src="https://github.com/user-attachments/assets/433342c9-205a-4c81-9cd5-9adbaf351140" />

### Class overview tab
<img width="500" height="500" alt="Screenshot 2026-01-20 at 8 55 49 AM" src="https://github.com/user-attachments/assets/bb031455-c5f7-4232-904e-cbf4862403aa" />


## Tech Stack  
**Framework:** Streamlit  
**Language:** Python  
**Data:** NCBI Entrez  
**Other:** Biopython, Matplotlib

## Features  
- Multi-page Streamlit app with a clean, data-driven UI  
- Pages for different parasite classes with an overview & species list (e.g., Cestoda, Digenea, etc.)
- View taxonomic order metrics & host diversity among parasitic classes
- Click a species → open a modal with taxonomic details  
- Fetches live NCBI data for classification & basic metadata  
- Modular architecture for extending to new parasite groups easily  

## Project Structure 
```
taxonomical-information-retriever/
├── main.py # Streamlit app entry point
├── pages/ # Individual class pages (Streamlit multipage)
│ ├── cestoda.py
│ ├── digenea.py
│ ├── enoplea.py
│ └── ...
├── data/ # Optional cached or static data
├── utils/ # NCBI fetchers, helpers, models
```

## Run Locally
### 1. Clone the repository  
```bash
git clone https://github.com/devinldiaz/taxonomical-information-retriever.git
cd taxonomical-information-retriever
```
### 2. Install dependencies
``` bash
pip install -r requirements.txt
```
### 3. Run Streamlit app
```bash
streamlit run main.py
```
