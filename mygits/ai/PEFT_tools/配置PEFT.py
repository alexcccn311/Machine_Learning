from transformers import AutoModelForCausalLM
from peft import get_peft_model, LoraConfig, TaskType
model_name_or_path = r"D:\git\gitstorege\original_model\Llama3.1-8B-Chinese-Chat"
tokenizer_name_or_path = r"D:\git\gitstorege\original_model\Llama3.1-8B-Chinese-Chat"

peft_config = LoraConfig(
    task_type=TaskType.CAUSAL_LM, inference_mode=False, r=8, lora_alpha=32, lora_dropout=0.1
)

model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
model = get_peft_model(model, peft_config)
model.print_trainable_parameters()
