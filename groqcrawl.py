import streamlit as st
import importlib    
import json
import sys
from pocketgroq import GroqProvider
from typing import List, Dict, Any

# Initialize GroqProvider
groq = GroqProvider()

def check_import(module_name):
    try:
        importlib.import_module(module_name)
        return None
    except ImportError as e:
        return str(e)

# Check for required modules
required_modules = ['pocketgroq', 'groq', 'langchain_groq', 'langchain', 'langchain_community']
import_errors = {module: check_import(module) for module in required_modules}

if any(import_errors.values()):
    st.error("Some required modules could not be imported:")
    for module, error in import_errors.items():
        if error:
            st.error(f"{module}: {error}")
    st.error("Please check your installation and requirements.txt file.")
    st.write("Python version:", sys.version)
    st.write("Python path:", sys.executable)
    st.write("sys.path:", sys.path)
else:
    # If all modules are present, import GroqProvider
    from pocketgroq import GroqProvider

    # Initialize GroqProvider
    try:
        groq = GroqProvider()
        st.success("GroqProvider initialized successfully.")
    except Exception as e:
        st.error(f"Error initializing GroqProvider: {str(e)}")

def scrape_url(url: str, formats: List[str] = ["markdown", "html"]) -> Dict[str, Any]:
    """
    Scrape a single URL using PocketGroq's enhanced_web_tool.
    """
    try:
        result = groq.enhanced_web_tool.scrape_page(url, formats)
        return result
    except Exception as e:
        return {"error": str(e)}

def crawl_website(url: str, max_depth: int, max_pages: int, formats: List[str] = ["markdown", "html"]) -> List[Dict[str, Any]]:
    """
    Crawl a website using PocketGroq's enhanced_web_tool.
    """
    try:
        groq.enhanced_web_tool.max_depth = max_depth
        groq.enhanced_web_tool.max_pages = max_pages
        results = groq.enhanced_web_tool.crawl(url, formats)
        return results
    except Exception as e:
        return [{"error": str(e)}]

def map_website(url: str) -> List[str]:
    """
    Map a website using PocketGroq's web_search method.
    """
    try:
        results = groq.web_search(f"site:{url}")
        return [result['url'] for result in results]
    except Exception as e:
        return [f"Error: {str(e)}"]

# Streamlit UI
st.title("GroqCrawl Interface")

# Select scraping type
scraping_type = st.radio("Select Scraping Type:", ["Single URL (/scrape)", "Crawl (/crawl)", "Map (/map)"])

# Input URL
url = st.text_input("URL:")

# Advanced Options
with st.expander("Options"):
    if scraping_type == "Crawl (/crawl)":
        max_depth = st.number_input("Max depth", min_value=1, value=3)
        max_pages = st.number_input("Max pages", min_value=1, value=10)
    
    formats = st.multiselect("Output formats", ["markdown", "html", "structured_data"], default=["markdown", "html"])
    
    exclude_paths = st.text_input("Exclude Paths (comma separated):", "blog/, /about/")
    include_paths = st.text_input("Include Only Paths (comma separated):", "articles/")
    ignore_sitemap = st.checkbox("Ignore sitemap")
    allow_backwards_links = st.checkbox("Allow backwards links")

# Run button
if st.button("Run"):
    if url:
        if scraping_type == "Single URL (/scrape)":
            result = scrape_url(url, formats)
            st.subheader("Scraped Result:")
            if "error" in result:
                st.error(result["error"])
            else:
                if "markdown" in formats:
                    st.markdown("### Markdown Content (Raw)")
                    st.text_area("Raw Markdown", result.get("markdown", ""), height=300)
                if "html" in formats:
                    st.markdown("### HTML Content")
                    st.code(result.get("html", ""), language="html")
                if "structured_data" in formats:
                    st.markdown("### Structured Data")
                    st.json(result.get("structured_data", {}))
                
                # Option to download result as JSON
                json_result = json.dumps(result, indent=4)
                st.download_button("Download JSON", json_result, "scraped_result.json", "application/json")
        
        elif scraping_type == "Crawl (/crawl)":
            results = crawl_website(url, max_depth, max_pages, formats)
            st.subheader("Crawl Results:")
            for i, result in enumerate(results, 1):
                st.write(f"Page {i}:")
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.write(f"URL: {result['url']}")
                    if "markdown" in formats:
                        st.markdown("#### Markdown Content (Raw)")
                        st.text_area(f"Raw Markdown (Page {i})", result.get("markdown", ""), height=200)
                    if "html" in formats:
                        st.markdown("#### HTML Content")
                        st.code(result.get("html", ""), language="html")
                    if "structured_data" in formats:
                        st.markdown("#### Structured Data")
                        st.json(result.get("structured_data", {}))
                st.markdown("---")
            
            # Option to download results as JSON
            json_result = json.dumps(results, indent=4)
            st.download_button("Download JSON", json_result, "crawl_results.json", "application/json")
        
        elif scraping_type == "Crawl (/crawl)":
            results = crawl_website(url, max_depth, max_pages, formats)
            st.subheader("Crawl Results:")
            for i, result in enumerate(results, 1):
                st.write(f"Page {i}:")
                if "error" in result:
                    st.error(result["error"])
                else:
                    st.write(f"URL: {result['url']}")
                    if "markdown" in formats:
                        st.markdown("#### Markdown Content")
                        st.markdown(result.get("markdown", ""))
                    if "html" in formats:
                        st.markdown("#### HTML Content")
                        st.code(result.get("html", ""), language="html")
                    if "structured_data" in formats:
                        st.markdown("#### Structured Data")
                        st.json(result.get("structured_data", {}))
                st.markdown("---")
            
            # Option to download results as JSON
            json_result = json.dumps(results, indent=4)
            st.download_button("Download JSON", json_result, "crawl_results.json", "application/json")
        
        elif scraping_type == "Map (/map)":
            results = map_website(url)
            st.subheader("Site Map:")
            for link in results:
                st.write(link)
            
            # Option to download results as JSON
            json_result = json.dumps(results, indent=4)
            st.download_button("Download JSON", json_result, "site_map.json", "application/json")
    
    else:
        st.error("Please enter a URL to process.")

# Display appropriate warnings
if scraping_type == "Crawl (/crawl)":
    st.warning("Crawling may take some time depending on the site size and depth.")
elif scraping_type == "Map (/map)":
    st.warning("Mapping uses a basic implementation. Results may not be comprehensive.")