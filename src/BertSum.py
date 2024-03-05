from transformers import BartForConditionalGeneration, BartTokenizer
from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load BART model and tokenizer
bart_model = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

# Use the model and tokenizer for summarization
input_text = "The internet has become an integral part of our daily lives. From communication to entertainment, education to business, it has transformed the way we interact with the world. Social media platforms like Facebook, Twitter, and Instagram allow us to connect with friends and family, share our thoughts and experiences"


inputs = tokenizer([input_text], max_length=1024, return_tensors='pt', truncation=True)
summary_ids = bart_model.generate(inputs['input_ids'], num_beams=4, min_length=30, max_length=100)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary)
