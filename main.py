import requests
import json

def search_searxng(query="elon musk", categories="news", time_range="day"):
    """
    Search SearxNG instance for news articles

    Args:
        query (str): Search query
        categories (str): Search categories (e.g., 'news', 'general')
        time_range (str): Time range filter (e.g., 'day', 'week', 'month')

    Returns:
        dict: JSON response from SearxNG API
    """

    # Base URL for the SearxNG instance
    base_url = "https://searxng-railway-production-65a7.up.railway.app/search"

    # Parameters for the API request
    params = {
        'q': query,
        'format': 'json',
        'categories': categories,
        'time_range': time_range,
        'engines':["startpage news"]
    }

    try:
        # Make the HTTP GET request
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse JSON response
        data = response.json()
        return data

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON response: {e}")
        return None

def main():
    # Execute the search
    results = search_searxng()

    if results:
        print("Search Results:")
        print(json.dumps(results, indent=2))

        # Extract and display just the results if available
        if 'results' in results:
            print(f"\nFound {len(results['results'])} results:")
            for i, result in enumerate(results['results'][:5], 1):  # Show first 5 results
                print(f"\n{i}. {result.get('title', 'No title')}")
                print(f"   URL: {result.get('url', 'No URL')}")
                print(f"   Content: {result.get('content', 'No content')[:100]}...")
    else:
        print("Failed to retrieve search results")

if __name__ == "__main__":
    main()
