from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

# Set the seed, this will help reproduce results. Changing the seed will
# generate new results
from transformers import set_seed
set_seed(248602)

# We're using the version of Pegasus specifically trained for summarization
# using the CNN/DailyMail dataset
model_name = "google/pegasus-cnn_dailymail"

# If you're following along in Colab, switch your runtime to a
# T4 GPU or other CUDA-compliant device for a speedup
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the tokenizer
tokenizer = PegasusTokenizer.from_pretrained(model_name)

# Load the model
model = PegasusForConditionalGeneration.from_pretrained(model_name).to(device)





import textwrap

content = """Mozilla's "Trustworthy AI" Thinking Points:

PRIVACY: How is data collected, stored, and shared? Our personal data powers everything from traffic maps to targeted advertising. Trustworthy AI should enable people to decide how their data is used and what decisions are made with it.

FAIRNESS: We’ve seen time and again how bias shows up in computational models, data, and frameworks behind automated decision making. The values and goals of a system should be power aware and seek to minimize harm. Further, AI systems that depend on human workers should protect people from exploitation and overwork.

TRUST: People should have agency and control over their data and algorithmic outputs, especially considering the high stakes for individuals and societies. For instance, when online recommendation systems push people towards extreme, misleading content, potentially misinforming or radicalizing them.

SAFETY: AI systems can carry high risk for exploitation by bad actors. Developers need to implement strong measures to protect our data and personal security. Further, excessive energy consumption and extraction of natural resources for computing and machine learning accelerates the climate crisis.

TRANSPARENCY: Automated decisions can have huge personal impacts, yet the reasons for decisions are often opaque. We need to mandate transparency so that we can fully understand these systems and their potential for harm."""



# Tokenize the entire content
batch = tokenizer(content, padding="longest", return_tensors="pt").to(device)

# Generate the summary as tokens
summarized = model.generate(**batch)

# Decode the tokens back into text
summarized_decoded = tokenizer.batch_decode(summarized, skip_special_tokens=True)
summarized_text = summarized_decoded[0]

# Compare
def compare(original, summarized_text):
  print(f"Article text length: {len(original)}\n")
  print(textwrap.fill(summarized_text, 100))
  print()
  print(f"Summarized length: {len(summarized_text)}")

compare(content, summarized_text)



set_seed(860912)

# Generate the summary as tokens, with a max_new_tokens
summarized = model.generate(**batch, max_new_tokens=800)
summarized_decoded = tokenizer.batch_decode(summarized, skip_special_tokens=True)
summarized_text = summarized_decoded[0]

compare(content, summarized_text)
