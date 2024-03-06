from transformers import PegasusForConditionalGeneration, PegasusTokenizer

# Load Pegasus model and tokenizer
pegasus_model = PegasusForConditionalGeneration.from_pretrained('google/pegasus-cnn_dailymail')
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-cnn_dailymail')

# Use the model and tokenizer for summarization
input_text = "The internet has become an integral part of \
    our daily lives. From communication to entertainment,\
    education to business, it has transformed the way\
    we interact with the world. Social media\
    platforms like Facebook, Twitter, and Instagram allow us\
    to connect with friends and family, share our thoughts\
    and experiences"

inputs = tokenizer([input_text], max_length=1024, return_tensors='pt', truncation=True)
summary_ids = pegasus_model.generate(inputs['input_ids'], num_beams=4, min_length=30, max_length=100)
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print(summary)
