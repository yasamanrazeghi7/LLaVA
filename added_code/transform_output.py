import json
# need to find the keys, 
def check_queality(dict_1, dict_2, instruction=""):
    if instruction != "":
        if dict_1['question'] + " " + instruction  != dict_2['text']:
            return False
    figure_id1 = dict_1['figure_id']
    figure_id2 = dict_2['image']
    if ".png" not in figure_id1:
        figure_id1 = figure_id1 + ".png"
    if ".png" not in figure_id2:
        figure_id2 = figure_id2 + ".png"
    if figure_id1 != figure_id2:
        return False
    # for k_key in ["figure_id"]:
    #     if dict_1[k_key] != dict_2[k_key]:
    #         return False
    return True

def read_json_file(file_path):
    return_dict_list = []
    with open(file_path, 'r') as infile:
        all_lines = infile.readlines()
    for line in all_lines:
        return_dict_list.append(json.loads(line))
    return return_dict_list

def read_json_into_dict(file_path):
    return_dict = {}
    with open(file_path, 'r') as infile:
        all_lines = infile.readlines()
    for line in all_lines:
        json_obj = json.loads(line)
        return_dict[json_obj['question_id']] = json_obj
    return return_dict

def write_json_file(file_path, answer_list):
    with open(file_path, 'w') as outfile:
        for line in answer_list:
            outfile.write(json.dumps(line) + '\n')


original_input_file = "/Users/yasaman/Documents/PhD/visualQA/LLAVA/LLaVA/playground/data/eval/visualQA/questions_sources_1.jsonl"
transformed_input_file = "/Users/yasaman/Documents/PhD/visualQA/LLAVA/LLaVA/playground/data/eval/visualQA/transformed_questions_sources_1.jsonl"
merged_answers = "/Users/yasaman/Documents/PhD/figure_understanding/LLAVA/LLaVA/playground/data/eval/visualQA/answers/transformed_questions_sources_1/llava-v1.5-7b/merge.jsonl"
answer_output_file = "/Users/yasaman/Documents/PhD/figure_understanding/LLAVA/LLaVA/playground/data/eval/visualQA/answers/transformed_questions_sources_1/llava-v1.5-7b/public_models_questions_with_answers.jsonl"
model_size = "7B"
model_name = "LLAVA-1-5"
instruction = ""

orginal_input_dict_list = read_json_file(original_input_file)
transformed_input_dict = read_json_into_dict(transformed_input_file)
merged_answers_dict = read_json_into_dict(merged_answers)
answer_list = []

for i, input_dict in enumerate(orginal_input_dict_list):
    if check_queality(input_dict, transformed_input_dict[i+1]):
        tmp_dict = input_dict.copy()
        tmp_dict['model_output'] = merged_answers_dict[i+1]['text'] #check this
        tmp_dict['model_size'] = model_size
        tmp_dict['model_name'] = model_name
        tmp_dict['model_input'] = transformed_input_dict[i+1]['text']
        answer_list.append(tmp_dict)
    else:
        print("Error: the input files are not aligned")

if len(answer_list) == len(orginal_input_dict_list):
    write_json_file(answer_output_file, answer_list)



