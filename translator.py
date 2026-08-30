from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


MODEL_NAME = "facebook/nllb-200-distilled-600M"


tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForSeq2SeqLM.from_pretrained(
    MODEL_NAME
)


def translate_to_telugu(text):

    tokenizer.src_lang = "eng_Latn"

    inputs = tokenizer(
        text,
        return_tensors="pt",
        padding=True,
        truncation=True
    )

    with torch.no_grad():

        output = model.generate(
            **inputs,
            forced_bos_token_id=tokenizer.convert_tokens_to_ids(
                "tel_Telu"
            ),
            max_length=256
        )

    translated = tokenizer.batch_decode(
        output,
        skip_special_tokens=True
    )

    return translated[0]