# Couplet
## 项目简介
人工智能对联项目
在网页对话框输入上联，自动生成下联 <br>
## 环境与工具
1.python 3.7 <br>
2.tensorflow 1.15.1 <br>
3.seq2seq <br>
## 实现原理
1.数据预处理：<br>
创建字典，将文本转化为模型可理解的数字<br>
2.模型构建：<br>
采用seq2seq模型，模型构建主要包括Encoder层与Decoder层。在Encoder层，我们首先需要对定义输入的tensor，同时要对字母进行Embedding，再输入到RNN层。<br>
3.训练模型：<br>
对构建的模型进行训练<br>
## 测试结果
   上联             下联
一腔热血             万里雄风
海上生明月           山中映碧云
花落无归处           花香有意时
春风袭来秋意浓       秋风吹落柳花香
事事如意大吉祥       人间有意乐新春
天时，地利           人富，国昌
## 项目负责人
[@LMB171004](https://github.com/LMB171004)  <br>
[@Lan10o0](https://github.com/Lan10o0)  <br>
[@aliu123aliu](https://github.com/aliu123aliu)  <br>
[@XUETING-LI](https://github.com/XUETING-LI)  <br>
