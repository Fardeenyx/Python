from google import genai

client = genai.Client(api_key="AIzaSyAyp05N2brxmJb_L0-09o215ZcfHSzQGNQ")

i= 0

while i < 1: 
     
    query = input("Enter your query: ")

    response = client.models.generate_content(
        model="gemini-3-flash-preview", contents=query,
    )
    print(response.text)