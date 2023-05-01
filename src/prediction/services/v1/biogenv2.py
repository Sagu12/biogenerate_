from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import pandas as pd
import random
import itertools

class BioGen:
    def __init__(self):
        if torch.cuda.is_available():
            self.device = "cuda"
        else:
            self.device = "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base")
        self.model = AutoModelForSeq2SeqLM.from_pretrained("humarin/chatgpt_paraphraser_on_T5_base").to(self.device)
        self.df = pd.read_csv(r"src/prediction/models/bios_net.csv", usecols=["keywords", "bios"])
        self.keywords_list = self.df.keywords.values.tolist()

    async def paraphrase(self,
                         input_sentence,
                         num_return_sequences=1,
                         repetition_penalty=10.0,
                         no_repeat_ngram_size=2,
                         temperature=0.9,
                         max_length=128):
        input_ids = self.tokenizer(
            f'paraphrase: {input_sentence}',
            return_tensors="pt", padding="longest",
            max_length=max_length,
            truncation=True,
        ).input_ids

        with torch.no_grad():
            outputs = self.model.generate(
                input_ids, temperature=temperature, repetition_penalty=repetition_penalty,
                num_return_sequences=num_return_sequences, no_repeat_ngram_size=no_repeat_ngram_size,
                max_length=max_length, do_sample=True
            )

        paraphrased_sentences = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return paraphrased_sentences
    
    async def main(self, keywords: str) -> None:
        lowered_keywords = keywords.lower()
        split_keywords = lowered_keywords.split(",")
        if len(split_keywords) < 2 or len(split_keywords) > 3:
            return {"error": "Invalid input keywords."}
        else:
            lowered_keywords = keywords.lower()
            lowered_keywords_split = lowered_keywords.split(',')
            lowered_keywords_split = [keyword.strip() for keyword in lowered_keywords_split]
            new_keywords = ", ".join(lowered_keywords_split)
            combinations = itertools.combinations(lowered_keywords_split, 2)
            combinations_list = []
            for combination in combinations:
                combinations_list.append(", ".join(combination))

            bios_df = self.df.copy(deep=True)
            bios_df["keywords"]= bios_df["keywords"].str.lower()

            matching_bios = bios_df[bios_df["keywords"].isin(combinations_list)]["bios"].values.tolist()
            target_bios = bios_df[bios_df["keywords"]==new_keywords]["bios"].values.tolist()
            target_bios_isin = bios_df[bios_df["keywords"].str.contains(new_keywords)]["bios"].values.tolist()

            if len(target_bios)==0 and len(target_bios_isin)==0:
                bios_to_paraphrase = matching_bios
            else:
                bios_to_paraphrase = matching_bios + target_bios + target_bios_isin

            bios_to_paraphrase = list(set(bios_to_paraphrase))
            bios_to_paraphrase= [str(i) for i in bios_to_paraphrase]
            try:
                bios_to_paraphrase.remove("[]")
            except:
                bios_to_paraphrase= bios_to_paraphrase
            bios_to_paraphrase = random.sample(bios_to_paraphrase, 3)

            paraphrased_bios = []
            for sentence in bios_to_paraphrase:
                with torch.no_grad():
                    paraphrased_sentences = await self.paraphrase(sentence)
                paraphrased_bios.append(paraphrased_sentences)
            paraphrased_bios_flat = [item for sublist in paraphrased_bios for item in sublist]
            output_bios = paraphrased_bios_flat
            return {"bios": output_bios}