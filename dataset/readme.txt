# StuDefects_java_ex是论文中的java语言的学生OJ数据集的一个题目的例子，这个数据集一个题目仅有一个学生代码
# my/main.py: 用于构建ch4
# ch4_0中的表示ch4章的代码整理后的最初版本，即学生代码命名没有采用true和false的版本
# ch4中的是目前整理的倒一true和倒二false代码,倒一是正确代码,倒二是最后一版错误代码, TODO:还需要找出Label行
# ch4_gold: 所有ch4中的代码, ch4_gold_true: 所有ch4中的正确代码, ch4_gold_false: 所有ch4中的错误代码
# val文件夹: 由techs的analysis将原始代码:analysis/code_filter/chapter4,划分为正确和逻辑错误代码,放在gold_false和gold_true文件夹中
# val/test.py: 用于将val/gold_false和val/gold_true中的代码进行对其(两两配对)

# ch4_labeled: 标注后的ch4数据集，且只有单行错误（不包含添加行的修改），由my/main_5_17.py生成
# ch4_labeled_dataset.xlsx: 标注后的ch4数据集的统计表
# dataset/my/main_5_17_1.py: 5.17最终分析结果，TODO：加入chatgpt的对比


analysis/code_filter/chapter4
=(dataset/my/main.py找出倒数两次的代码)=> dataset/val/val_
=(techs.analysis分类)=> dataset/val/gold_true和gold_false
=(dataset/val/test.py匹配val/gold_true和false两两配对)=> dataset/ch4_gold_true和false 
=(合并)=> dataset/ch4_gold
=(dataset/my/main.py构建成数据集结构)=> dataset/ch4
=(dataset/my/main_5_17.py打标签)=> dataset/ch4_labeld
