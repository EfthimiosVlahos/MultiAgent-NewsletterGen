from crewai_tools import BaseTool
from exa_py import Exa
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv("/Users/Vlahonator/Downloads/exa-crewai-master/.env")
print("EXA_API_KEY:", os.getenv("EXA_API_KEY"))


class SearchAndContents(BaseTool):
    name: str = "Search and Contents Tool"
    description: str = (
        "Searches the web based on a search query for the latest results. Results are only from the last week. Uses the Exa API. This also returns the contents of the search results."
    )

    def _run(self, search_query: str) -> str:

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        search_results = exa.search_and_contents(
            query=search_query,
            use_autoprompt=True,
            start_published_date=date_cutoff,
            text={"include_html_tags": False, "max_characters": 8000},
        )

        return search_results


class FindSimilar(BaseTool):
    name: str = "Find Similar Tool"
    description: str = (
        "Searches for similar articles to a given article using the Exa API. Takes in a URL of the article"
    )

    def _run(self, article_url: str) -> str:

        one_week_ago = datetime.now() - timedelta(days=7)
        date_cutoff = one_week_ago.strftime("%Y-%m-%d")

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        search_results = exa.find_similar(
            url=article_url, start_published_date=date_cutoff
        )

        return search_results


class GetContents(BaseTool):
    name: str = "Get Contents Tool"
    description: str = "Gets the contents of a specific article using the Exa API. Takes in the ID of the article in a list, like this: ['https://www.cnbc.com/2024/04/18/my-news-story']."
    
    def _run(self, article_ids: str) -> str:

        exa = Exa(api_key=os.getenv("EXA_API_KEY"))

        contents = exa.get_contents(article_ids)
        return contents
    

if __name__ == "__main__":
    # search_and_contents=SearchAndContents()
    # search_results=search_and_contents.run(search_query="latest news on the USA stock market")
    # print(search_results)
    
    # find_similar=FindSimilar()
    # similar=find_similar.run(article_url="https://www.cnbc.com/2024/06/23/stock-market-today-live-updates.html?__source=newsletter%7Cmsapac")
    # print(similar)
    
    get_contents=GetContents()
    contents=get_contents.run(article_ids=["https://www.cnbc.com/2024/06/23/stock-market-today-live-updates.html?__source=newsletter%7Cmsapac"])
    print(contents)