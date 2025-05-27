# Automatic-segmentation-model-of-pectoralis-major-muscle
<p>epoch路径：E:\APP\Anaconda3\envs\nnUNet\Lib\site-packages\nnunetv2\training\nnUNetTrainer\nnUNetTrainer.py</p>
<p>1验证：nnUNetv2_plan_and_preprocess -d 002 --verify_dataset_integrity  （CPU）</p>
<p>nnUNetv2_plan_and_preprocess -d 002 --verify_dataset_integrity -c 3d_fullres --device cuda </p>
<p>2预处理：nnUNetv2_plan_and_preprocess -d 002 -c 3d_fullres -np 8  (CPU)</p>
<p>3训练：nnUNetv2_train 002 3d_fullres 1</p>
<p>4推理：nnUNetv2_predict -i "G:\0424\Val" -o "G:\0424\Pre" -d 001 -c 3d_fullres -f 1 --save_probabilities</p>
