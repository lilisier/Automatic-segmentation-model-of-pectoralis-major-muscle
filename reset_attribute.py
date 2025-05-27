import SimpleITK as sitk

# 1. 读取图像和标签
image = sitk.ReadImage("F:/work/nnUNet/nnUNet_raw/Dataset001_Pectoralis/imagesTr/Case025_0000.nrrd")
label = sitk.ReadImage("F:/work/nnUNet/nnUNet_raw/Dataset001_Pectoralis/labelsTr/Case025.nrrd")

# 2. 打印原始几何属性（调试用）
print("原始图像image Size:", image.GetSize(), "Spacing:", image.GetSpacing(), "Origin:", image.GetOrigin())
print("原始标签label Size:", label.GetSize(), "Spacing:", label.GetSpacing(), "Origin:", label.GetOrigin())

# 3. 强制设置图像的几何属性与标签一致
image.SetSpacing(label.GetSpacing())
image.SetOrigin(label.GetOrigin())

# 4. 重采样标签以匹配标签尺寸
resampler = sitk.ResampleImageFilter()
resampler.SetReferenceImage(label)  # 以label为参考基准
resampler.SetOutputSpacing(label.GetSpacing())  # 显式设置输出Spacing（避免意外覆盖）
resampler.SetOutputOrigin(label.GetOrigin())    # 显式设置输出Origin
resampler.SetSize(label.GetSize())              # 关键！强制输出Size与标签一致
resampler.SetInterpolator(sitk.sitkNearestNeighbor)  # 标签需用最近邻插值
resampler.SetOutputPixelType(sitk.sitkUInt8)    # 确保输出类型为UInt8（适用于分割标签）
resampled_image = resampler.Execute(image)

# 5. 验证输出尺寸是否一致
print("重采样后图像image Size:", resampled_image.GetSize())  # 应与标签Size相同

# 6. 保存修正后的标签
sitk.WriteImage(resampled_image, "F:/work/nnUNet/nnUNet_raw/Dataset001_Pectoralis/imagesTr/Case025_0000.nrrd")
print("保存成功")