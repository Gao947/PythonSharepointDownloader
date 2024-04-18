import os
import sharepy

def download_files_from_urls_file(urls_file, save_directory):
    s = sharepy.connect("https://example.sharepoint.com")
    try:
        # Open the file containing the URLs
        with open(urls_file, 'r', encoding='UTF-8') as file:
            # Read each line (URL) from the file
            for url in file:
                # Remove leading/trailing whitespace and newlines
                url = url.strip()
                # Download the file
                try:
                    # Check if the request was successful (status code 200)
                    response = s.getfile(url, filename=f'downloaded_files\{url.split("/")[-1]}')
                    if response.status_code == 200:
                        print(f"Downloaded: {url}")
                    else:
                        print(f"Failed to download: {url}. Status code: {response.status_code}")
                except Exception as e:
                    print(f"An error occurred while downloading {url}: {e}")

    except Exception as e:
        print(f"An error occurred while reading URLs from {urls_file}: {e}")

# Path to the file containing the list of URLs
urls_file = "urls.txt"
# Directory where downloaded files will be saved
save_directory = "downloaded_files"

# Create the save directory if it doesn't exist
if not os.path.exists(save_directory):
    os.makedirs(save_directory)

# Call the function to download files from the URLs file
download_files_from_urls_file(urls_file, save_directory)