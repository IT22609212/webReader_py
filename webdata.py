# import requests

# # URL for the populate list API
# populate_url = "https://app.gulfood.com/search/populate_list_es/13 "

# # Headers and cookies for the POST request
# headers = {
#     "accept": "application/json, text/javascript, */*; q=0.01",
#     "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
#     "accept-encoding": "gzip, deflate, br",
#     "accept-language": "en-US,en;q=0.9",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
# }

# cookies = {
#     "AWSALB": "0vTLHWsqpt4ZyPMDxrVkShgnGuf0/LNc5k/Pb1Cdv1Bw/wZIwXintn3wnSDZzbCzYpOdFVX42043Lk/UQf1nQtkJGvGV3eAQzBiB1uU6c+AGoTX6vkZ4oT2xwTDt",
#     "AWSALBCORS": "0vTLHWsqpt4ZyPMDxrVkShgnGuf0/LNc5k/Pb1Cdv1Bw/wZIwXintn3wnSDZzbCzYpOdFVX42043Lk/UQf1nQtkJGvGV3eAQzBiB1uU6c+AGoTX6vkZ4oT2xwTDt",
#     "session": "a4ed55d69fc1b799_6791f19f.HArtLTdtfr9qfkSPrkpP1ySzxaY"
# }

# # Step 1: Fetch the list of document IDs
# response = requests.post(populate_url, headers=headers, cookies=cookies)

# if response.status_code == 200:
#     try:
#         # Parse JSON response
#         data = response.json().get("data", [])
#         # Extract id_object (document_id)
#         document_ids = [item.get("id_object") for item in data if item.get("id_object")]
#         print("Extracted document IDs:")
#         print(document_ids)
#     except Exception as e:
#         print(f"Error parsing JSON response: {e}")
# else:
#     print(f"Failed to fetch document IDs. Status Code: {response.status_code}")







import pandas as pd
import requests

# Base URL for the company profile API
base_url = "https://app.gulfood.com/profile/company/"

# List of company IDs
company_ids = [
"2ad042411b8b4c4fa8f0"
"d3fd258be5ed4ed7a333"
"fd126d916cc643f0859b"
"6d087cef889d4a6cb685"
"561dd77faa734a52b28f"
"627149bc667d4b30985e"
"20ef1a1ac57c4e168cbc"
"60b30916aecb4ff08e35"
"060732bd61a247eeb50e"
"2514a857afce42868f35"
"961700716b60416cbc47"
"cd4dbdb37fbe41d6a00a"
"a084819159f7472f871c"
"7b807675403b4118b734"
"fbcacf52c49442819e90"
"9c4d88171cd04a48b0f2"
"843a7e0917f34ed3b83f"
"db2734e968434c50a480"
"2652a73b26cd4d45b9b5"
"4f59f83afe71422d8750"
"9abbc0043cac46739e0f"
"208da4f7f92f47249881"
"05f32ca8a4ad469ca24b"
"0d6031bf4c42488fabe1"
"e6cc05165f2d4596a498"
"a94e77c856fe4844b331"
"512ef5021991451caed9"
"d51480f0948f43bf9753"
"75bba6218b194636b37a"
"5ea07df0e02e4ecd8397"
"019af5ea5e7a419a9770"
"13f6d568c476412b8768"
"e32ca98afb1949ef9543"
"c59effd63f2640a8bc21"
"27d8b26d8d4447bf9e31"
"2f2153b6b4f64568bba5"
"2ca282bc19274d559da9"
"342d17e87a654582a423"
"6f31ec527d5c4a7dad74"
"4f59f83afe71422d8750"
"9abbc0043cac46739e0f"
"208da4f7f92f47249881"
"05f32ca8a4ad469ca24b"
"0d6031bf4c42488fabe1"
"e6cc05165f2d4596a498"
"a94e77c856fe4844b331"
"512ef5021991451caed9"
"d51480f0948f43bf9753"
"75bba6218b194636b37a"
"2ca282bc19274d559da9"
"969b41cde25c49e7a188"
"7650a188a26e4809a960"
"a9e45c38f29842e2949b"
"570d7e1152c240149b30"
"36896cde857149e6be6f"
"38c0018f9cc54b498fc6"
"e0f4df2862d04e7a9cc5"
"759cd06d7fe14f738a0f"
"5b941d7b258347e6946f"
"6235dc3df83947989122"
"1e6847d112e148979357"
"7527f39f7bc64f37b1c6"
"07b0745c95424461b47a"
"006c74efa6b14f9c9a90"
"3aef566d25054792bcb3"
"2522682d2939498c9601"
"24e03130a11b4aa49164"
"e5fb614ae4ee4b03afe1"
"3f19ce2f9e0f44289f61"
"8bedafcce10a4be4afc5"
"b5d5a18ae6cb4a42b30a"
"d690ecf9710b4a86a367"
"f7f5d2e016604e99ae13"
"c27b72a41bbe4c338534"
"e05d7e6342024cf1bb2a"
"38889acdcc5c4543a59a"
"30c08af50a414b24a060"
"39abe6b6c0c04dc8871c"
"30f84594e3e24065a4ad"
"9d9f915d87a149cd8c31"
"0bc489fbf90c4603a23b"
"843f8e59172b4fe88c40"
"161d5368828c4f1b9a55"
"cf0298867e1140e89d5c"
"f9a0190ecff3497084dd"
"b743b5cc89a641db856a"
"30d5670106d34467a0c2"
"5b922f5c87ca4c0bb25b"
"694063f495b94943beb4"
"161d5368828c4f1b9a55"
"3e0d201fd6644bb8993e"
"f9164810befc45a48686"
"962d9cc27c824a8692ed"
"4ef725bd3645490d88bc"
"6fec4ca1583443b89c81"
"9819e20955db4ff4b4fa"
"38889acdcc5c4543a59a"
"30c08af50a414b24a060"
"68a5fa2aef9d4556b2dd"
"9f200321fac1483ab0ed"
"5620bebf57e940ecbd99"
"a943030451fd432ba9b3"
"3b2d72c7b8734f70900c"
"06a54138b4dd4580b5f0"
"7f6d99f85753465d9d53"
"1f5e4f2070d741048bc7"
"c2c101c8d4ea4ed892c0"
]


# Headers and cookies for the request
headers = {
    "accept": "application/json, text/plain, */*",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
}

cookies = {
    "session": "e2114f8a48abbcf1_6791e38e.roZFTPlqYf42Le8sHKZVqsMZVTs",
    "AWSALB": "iRN23MEP9mqnEEJxgZgU8P/H2JUHSva0V4Ta7lYTDWgLYERFthbkKPhM9hh27RDqClTSoBu0/asFYjETFRCWNME7aHkLW2S5IDaAb4zPScsxEANOJSf43Rd5fEDk",
    "AWSALBCORS": "iRN23MEP9mqnEEJxgZgU8P/H2JUHSva0V4Ta7lYTDWgLYERFthbkKPhM9hh27RDqClTSoBu0/asFYjETFRCWNME7aHkLW2S5IDaAb4zPScsxEANOJSf43Rd5fEDk"
}

# Initialize an empty list to store all company data
all_data = []

# Iterate over each company ID
for company_id in company_ids:
    url = base_url + company_id
    response = requests.get(url, headers=headers, cookies=cookies)
    
    if response.status_code == 200:
        company_data = response.json()

        # Extract specific fields
        exhibitor_name = company_data.get("company_name", "N/A")
        
        
        
        # Extract attributes from my_preference_matches
        company_type = next((item["list"][0]["value"] for item in company_data["my_preference_matches"] if item["attribute"] == "Company Type"), "N/A")
        hall = next((item["list"][0]["value"] for item in company_data["my_preference_matches"] if item["attribute"] == "Hall Number"), "N/A")
        pavilion = next((item["list"][0]["value"] for item in company_data["my_preference_matches"] if item["attribute"] == "Pavilion"), "N/A")
        country = next((item["list"][0]["value"] for item in company_data["my_preference_matches"] if item["attribute"] == "Country"), "N/A")
        
        # Company URL and logo (added to the dataset)
        company_url = company_data.get("company_url", "N/A")
        

        # Append data to the list
        all_data.append({
            "Exhibitor Name": exhibitor_name,
            "Hall": hall,
            "Pavilion": pavilion,
            "Country": country,
            "Company URL": company_url,
            "Company Type": company_type
            
        })
    else:
        print(f"Failed to fetch data for Company ID: {company_id} (Status Code: {response.status_code})")

# Create a DataFrame and save all data to Excel
df = pd.DataFrame(all_data)
df.to_excel("reseller_distributer.xlsx", index=False)
print("All data saved to reseller_distributer.xlsx")
