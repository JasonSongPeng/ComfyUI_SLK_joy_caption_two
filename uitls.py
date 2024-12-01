import gc
import json
import os
import folder_paths

from comfy.model_management import unload_all_models, soft_empty_cache

# 下载hg 模型到本地
def download_hg_model(model_id:str, exDir:str=''):
    # 获取本地模型路径
    model_checkpoint = os.path.join(folder_paths.models_dir, exDir, os.path.basename(model_id))
    
    # 检查目录是否存在且不为空
    if os.path.exists(model_checkpoint) and any(os.scandir(model_checkpoint)):
        print(f"使用本地模型: {model_checkpoint}")
        return model_checkpoint
        
    # 如果目录不存在或为空，则报错
    raise ValueError(f"模型目录 {model_checkpoint} 不存在或为空。请确保已正确下载模型文件。")

def clear_cache():
    gc.collect()
    unload_all_models()
    soft_empty_cache()

def modify_json_value(file_path, key_to_modify, new_value):
  """
  读取 JSON 文件，修改指定 key 的 value 值，并保存修改后的文件。

  Args:
    file_path: JSON 文件路径。
    key_to_modify: 需要修改的 key。
    new_value:  新的 value 值。
  """
  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)

    # 查找并修改 key 的 value
    if key_to_modify in data:
      data[key_to_modify] = new_value
    else:
      print(f"Warning: Key '{key_to_modify}' not found in JSON file.")

    # 保存修改后的 JSON 文件
    with open(file_path, 'w', encoding='utf-8') as f:
      json.dump(data, f, indent=4)  # 使用 indent 参数格式化输出

    print(f"Successfully modified '{key_to_modify}' value in '{file_path}'.")

  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in '{file_path}'.")

def read_json_file(file_path):
  """读取 JSON 文件并转换为 Python 字典。"""
  try:
    with open(file_path, 'r', encoding='utf-8') as f:
      data = json.load(f)
    return data
  except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    return None
  except json.JSONDecodeError:
    print(f"Error: Invalid JSON format in '{file_path}'.")
    return None