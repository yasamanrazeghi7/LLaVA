import json

def modify_jsonl(input_file_path, output_file_path, instruction=""):
    with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
        question_id = 1  # Initializing question ID counter
        
        for line in infile:
            # Load the JSON object from the line
            json_obj = json.loads(line)
            
            # Adding question ID
            json_obj['question_id'] = question_id
            question_id += 1  # Incrementing question ID counter
            
            # Modifying keys, you can customize this part
            if 'question' in json_obj:
                if instruction == "":
                    json_obj['text'] = json_obj.pop('question')
                else:
                    json_obj['text'] = json_obj.pop('question') + " " + instruction
            
            if 'figure_id' in json_obj:
                json_obj['image'] = json_obj.pop('figure_id')+".png"
            
            # Write the modified JSON object back to the new file
            outfile.write(json.dumps(json_obj) + '\n')

# Call the function with the paths of your input and output files
instruction = ""
modify_jsonl('/Users/yasaman/Documents/PhD/visualQA/LLAVA/LLaVA/playground/data/eval/visualQA/questions_sources_1.jsonl', '/Users/yasaman/Documents/PhD/visualQA/LLAVA/LLaVA/playground/data/eval/visualQA/transformed_questions_sources_1.jsonl', instruction=instruction)
