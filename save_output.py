from google import genai

client = genai.Client(api_key="AIzaSyC5L2k8ZflIpS--TY6IsA2R4Sxp5IGRxrY")

user_input = input("What report do you want? ")

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=f"Write a professional report about: {user_input}"
)

with open("report.txt", "w") as file:
    file.write(response.text)

print("Report saved to report.txt")    
