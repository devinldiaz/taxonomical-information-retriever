<h3 align="center">ParaSite</h3>

<p align="center">
  Taxonomy and visualization tool for parasite phyla
</p>

---

## Overview  
Navigate parasite classes, view species lists, open modals with details, and fetch real-time taxonomy data from NCBI.

## Tech Stack  
**Framework:** Streamlit  
**Language:** Python  
**Data:** NCBI Entrez
**Other:** BioPython, Matplotlib

## Current Features  
- Multi-page Streamlit app with a clean, simple UI  
- Pages for different parasite classes (e.g., Cestoda, Trematoda, Nematoda, etc.)  
- Click a species → open a modal with taxonomic details  
- Fetches live NCBI data for classification & basic metadata  
- Modular project structure for adding new parasite groups easily  

## Planned Features  
- **Phylogeny Visualization:** Tree diagrams for evolutionary relationships  
- **Image Gallery:** Species-level reference images  
- **Filtering & Search:** By host organism, habitat, or morphology  

## Project Structure 
```
taxonomical-info-retriever/
├── main.py # Streamlit app entry point
├── pages/ # Individual class pages (Streamlit multipage)
│ ├── Cestoda.py
│ ├── Trematoda.py
│ ├── Nematoda.py
│ └── ...
├── data/ # Optional cached or static data
├── utils/ # NCBI fetchers, helpers, models
```

## Run Locally
### 1. Clone the repository  
```bash
git clone https://github.com/<your-username>/taxonomical-info-retriever.git
cd taxonomical-info-retriever
```
### 2. Install dependencies
``` bash
pip install -r requirements.txt
```
### 3. Run Streamlit app
```bash
streamlit run main.py
```
