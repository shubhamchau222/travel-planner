from pydantic import BaseModel, Field
from typing import Type
from crewai.tools import BaseTool
import requests
import json
from dotenv import load_dotenv
import os

load_dotenv()
serper_api= os.getenv("SERPER_API_KEY")

class SearchQuery(BaseModel):
    query: str = Field(..., description="Search query to find relevant information")

class SearperTool(BaseTool):
    name: str= "Search the internet"
    description: str = """A tool to search the internet for relevant information. The input should be a search query, 
                            e.g. 'latest news on AI' or 'Python programming tutorials'"""
    args_schema: Type[BaseModel] = SearchQuery

    def _run(self, query:str) -> str:
        try:
            url= "https://google.serper.dev/search"
            payload= json.dumps({"q": query})
            #TODO: Add your own API key here (make it dynamic)
            headers = {
                        'X-API-KEY': serper_api,
                        'Content-Type': 'application/json'
                        }
            
            top_results_toselect= 5

            response = requests.request("POST", url, headers=headers, data=payload)

            if response.status_code !=200:
                return f"Error: Search API request failed. Status code: {response.status_code}"
            
            data = response.json()

            if 'organic' not in data:
                return "No results found or API error occurred."

            results = data['organic']
            string = []
            for result in results[ : top_results_toselect]:
                try:
                    title = result.get('title', 'No title')
                    link = result.get('link', 'No link')
                    snippet = result.get('snippet', 'No snippet')
                    string.append(f"Title: {title}\nLink: {link}\nSnippet: {snippet}\n\n")
                except KeyError:
                    continue
            return "\n".join(string) if string else "No valid results found."

        except Exception as e:
            raise(e)



## Tool tesing
# if __name__ == "__main__":
#     a= SearperTool()
#     print(a._run("Krabi Thailand"))

## demo results
# (tripplanner) D:\crew_ai\Travel-planner-using-crewai>python tools/searper.py
# Title: Krabi - The official website of Tourism Authority of Thailand
# Snippet: Krabi is famous for its scenic view and breathtaking beaches and islands. Its cor


# Title: Crappy in Krabi - How We Didn't Enjoy The Thai Paradise                            
# Link: https://www.tuljak.com/blog/crappy-in-krabi-how-we-didnt-enjoy-the-thai-paradise
# Snippet: Ao Nang is the main tourist hub of Krabi Province. It is the main jump-off point
# to many of the most popular islands in the area. We could score ...


# Title: Krabi Town, Thailand: All You Must Know Before You Go (2025)                       
# Link: https://www.tripadvisor.com/Tourism-g297927-Krabi_Town_Krabi_Province-Vacations.html
# Snippet: Krabi Town is known for some of its popular attractions, which include: Tiger Cav
# e Temple (Wat Tham Suea) · Hong Island · Phi Phi Islands · Krabi Weekend Night ...


# Title: Krabi - Wikipedia                                                                  
# Link: https://en.wikipedia.org/wiki/Krabi
# Snippet: Krabi is the capital of and main town in Krabi Province (thesaban mueang), on the
#  west coast of southern Thailand, where the Krabi River flows into Phang ...


# Title: Tailor-Made Vacations To Krabi | Places To Go | Audley Travel US                   
# Link: https://www.audleytravel.com/us/thailand/places-to-go/krabi
# Snippet: The province stretches along Thailand's southeast coast, graduating from a thick
# jungle interior to blonde beaches that taper gently into bathwater-warm water.
