from ace import ACE
from utils import initialize_clients

# Initialize API clients
api_provider = "sambanova" # or "together", "openai"

print("Step 1")

# Initialize ACE system
ace_system = ACE(
    api_provider=api_provider,
    generator_model="DeepSeek-V3.1",
    reflector_model="DeepSeek-V3.1",
    curator_model="DeepSeek-V3.1",
    max_tokens=4096
)

print("Step 2")

# Prepare configuration
config = {
    'num_epochs': 1,
    'max_num_rounds': 3,
    'curator_frequency': 1,
    'eval_steps': 100,
    'online_eval_frequency': 15,
    'save_steps': 50,
    'playbook_token_budget': 80000,
    'task_name': 'your_task',
    'json_mode': False,
    'no_ground_truth': False,
    'save_dir': './results',
    'test_workers': 20,
    'use_bulletpoint_analyzer': False,
    'api_provider': api_provider

}

print("Step 3")

# Offline adaptation
results = ace_system.run(
    mode='offline',
    train_samples=train_data,
    val_samples=val_data,
    test_samples=test_data,  # Optional
    data_processor=processor,
    config=config
)

print("Step 4")

# Online adaptation
results = ace_system.run(
    mode='online',
    test_samples=test_data,
    data_processor=processor,
    config=config
)

# Evaluation only
results = ace_system.run(
    mode='eval_only',
    test_samples=test_data,
    data_processor=processor,
    config=config
)