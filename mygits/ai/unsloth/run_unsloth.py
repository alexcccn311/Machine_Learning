from unsloth import FastLanguageModel
from unsloth import is_bfloat16_supported
import torch
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import load_dataset

max_seq_length = 2048 # Supports RoPE Scaling internally, so choose any!

# 使用本地数据集
local_dataset_path = r"D:\git\gitstorege\json\llama3\danmu.json"
dataset = load_dataset("json", data_files={"train": local_dataset_path}, split="train")

# 加载本地模型
local_model_path = r"D:\git\gitstorege\original_model\Llama3.1-8B-Chinese-Chat"
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name=local_model_path,
    max_seq_length=max_seq_length,
    dtype=None,
    load_in_4bit=True,
)

# Do model patching and add fast LoRA weights
model = FastLanguageModel.get_peft_model(
    model,
    r=16,
    target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                    "gate_proj", "up_proj", "down_proj"],
    lora_alpha=16,
    lora_dropout=0, # Supports any, but = 0 is optimized
    bias="none",    # Supports any, but = "none" is optimized
    # [NEW] "unsloth" uses 30% less VRAM, fits 2x larger batch sizes!
    use_gradient_checkpointing="unsloth", # True or "unsloth" for very long context
    random_state=3407,
    max_seq_length=max_seq_length,
    use_rslora=False,  # We support rank stabilized LoRA
    loftq_config=None, # And LoftQ
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    dataset_text_field="text",
    max_seq_length=max_seq_length,
    tokenizer=tokenizer,
    args=TrainingArguments(
        per_device_train_batch_size=2,
        gradient_accumulation_steps=4,
        warmup_steps=10,
        max_steps=60,
        fp16=not is_bfloat16_supported(),
        bf16=is_bfloat16_supported(),
        logging_steps=1,
        output_dir=r"D:\git\gitstorege\original_model\outputs",
        optim="adamw_8bit",
        seed=3407,
    ),
)
trainer.train()