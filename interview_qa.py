from transformers import pipeline
import os
import time
import dask
import dask.bag as db
from dask.distributed import Client


# reading text
count = 8
text = ''

for i in range(count):
    with open(f'distributed_files/output/part_{i + 1}.txt', 'r', encoding='utf-8') as f:
        text += f.read() + '\n'


# QA
questions = [
    'не возражаешь, если я спрошу?',
    'не могли бы вы рассказать мне о вашей любимой книге и почему она вам так нравится?',
    'о каком месте путешествия вы мечтаете, и что вас в нем привлекает?',
    'если бы вы могли обладать какой-либо сверхспособностью, какой бы она была и как бы вы ее использовали?',
    'какое самое запоминающееся приключение или путешествие, в котором вы побывали?',
    'если бы вы могли поужинать с какой-либо исторической личностью, кто бы это был и о чем бы вы их спросили?'
]

def question_answering(text, question):
    model_name = "ruselkomp/sbert_large_nlu_ru-finetuned-squad"
    nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
    QA_input = {
        'question': question,
        'context': text
    }

    res = nlp(QA_input)
    print(f'ANSWER: {res["score"]:.4f}: {res["answer"]}')

client = Client('tcp://10.128.0.36:8786')
question_bag = db.from_sequence(questions)
delayed_results = [dask.delayed(question_answering)(text, question) for question in question_bag]

start = time.time()
dask.compute(*delayed_results, scheduler='distributed')
end = time.time()
print(f'Overall time: {end - start} sec')

# Close the Dask client
client.close()
