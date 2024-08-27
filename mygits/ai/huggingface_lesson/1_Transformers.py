from transformers import pipeline
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'
unmasker = pipeline('fill-mask',device=device)
print(unmasker(
    '我好 <mask> 。',
    top_k=2,
))

"""
pipeline('预定义的任务类型',model='模型名',device=device)
transformers 库中预定义的任务类型:
    audio-classification - 音频分类
    automatic-speech-recognition - 自动语音识别
    depth-estimation - 深度估计
    document-question-answering - 文档问答
    feature-extraction - 特征提取
    fill-mask - 填充掩码（Masked Language Model）
    image-classification - 图像分类
    image-feature-extraction - 图像特征提取
    image-segmentation - 图像分割
    image-to-image - 图像到图像转换
    image-to-text - 图像到文本转换
    mask-generation - 掩码生成
    ner (Named Entity Recognition) - 命名实体识别
    object-detection - 目标检测
    question-answering - 问答
    sentiment-analysis - 情感分析
    summarization - 摘要生成
    table-question-answering - 表格问答
    text-classification - 文本分类
    text-generation - 文本生成
    text-to-audio - 文本到音频转换
    text-to-speech - 文本到语音转换
    text2text-generation - 文本到文本生成（如翻译或摘要）
    token-classification - 标记分类（如命名实体识别）
    translation - 翻译
    video-classification - 视频分类
    visual-question-answering - 视觉问答
    vqa (Visual Question Answering) - 视觉问答
    zero-shot-audio-classification - 零样本音频分类
    zero-shot-classification - 零样本分类
    zero-shot-image-classification - 零样本图像分类
    zero-shot-object-detection - 零样本目标检测
    translation_XX_to_YY - 从XX语言到YY语言的翻译
"""
