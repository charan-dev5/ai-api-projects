from google import genai
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()

client = genai.Client(api_key=os.getenv("API_KEY"))

print("=== AI Data Analyzer ===\n")

filename = input("Enter CSV filename: ")

df = pd.read_csv(filename)

summary = f"""
Dataset Overview:
- Rows: {df.shape[0]}
- Columns: {df.shape[1]}
- Column names: {list(df.columns)}
- Basic statistics:
{df.describe().to_string()}
"""

prompt =f"""
You are a professional data analyst.
Analyze this dataset and provide:
1. Key insights and patterns
2. Interesting findings
3. Business recommendations
4. Any data quality issues

Dataset summary:
{summary}
"""

response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents=prompt
)

print("\n=== AI Analysis ===\n")
print(response.text)

with open("data_analysis_report.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
    
print("\nAnalysis saved to data_analysis_report.txt")   