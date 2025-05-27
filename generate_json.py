# 文件名改为 create_dataset_json.py
import json  # 现在会正确导入标准库的 json 模块

data = {
    "channel_names": {"0": "CT"},
    "labels": {"background": 0, "Pectoralis": 1},
    "numTraining": 20,
    "file_ending": ".nrrd",
    "overwrite_image_reader_writer": "SimpleITKIO"
}

with open("dataset.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)  # 现在可以正常调用 json.dump()