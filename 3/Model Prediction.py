from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import pandas as pd

model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
sa= pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)

dataFrame = pd.read_excel("MarkedPreprocessedData.xlsx")
columnName = "Preprocessed Text"

guessed = []
for comment in dataFrame[columnName]:
    p = sa(comment)
    if p[0]["label"] == "positive":
        guessed.append(1)
    if p[0]["label"] == "negative":
        guessed.append(0)


write_col_name = "Guessed"
dataFrame[write_col_name] = guessed
dataFrame.to_excel("MarkedPreprocessedData.xlsx", index=False)
print("done")

