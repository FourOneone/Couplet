import os
import tensorflow as tf
import numpy as np
from read_utils import TextConverter, batch_generator
from model import Model,Config
from flask import Flask, jsonify, request,render_template
from flask_cors import CORS, cross_origin
from gevent.pywsgi import WSGIServer
import logging
# from model_attention import Model,Config

app = Flask(__name__)
CORS(app)


model_path = os.path.join('models', Config.file_name)
     #TextConverter类编码所有的内容为数据单元对应数字，然后使用batch_generator函数将编码好的数字分批返回
converter = TextConverter(vocab_dir='data/vocabs', max_vocab=Config.vocab_size, seq_length = Config.seq_length)
print('vocab lens:',converter.vocab_size)


    # 加载上一次保存的模型
model = Model(Config)
checkpoint_path = tf.train.latest_checkpoint(model_path)
if checkpoint_path:
    model.load(checkpoint_path)

@app.route('/success/<nam>')
def success(nam):
    return '%s' % nam

@app.route('/chat/couplet/<in_str>')
def chat_couplet(in_str):
     if len(in_str) == 0 or len(in_str) > 50:
        output = u'您的输入太长了'
     else:

        in_str = ' '.join(in_str)
        in_str = in_str.split()
        en_arr, arr_len = converter.text_en_to_arr(in_str)
        test_g = [np.array([en_arr, ]), np.array([arr_len, ])]  # 序列
        output_ids = model.test(test_g, model_path, converter)  # 对输出文字id
        output = ' '.join(in_str)
        output = converter.arr_to_text(output_ids)  # 下联

        output = ''.join(output.split(' '))
        print('上联：%s；下联：%s' % (in_str, output))
        return jsonify({'output': output})

@app.route('/test', methods=['POST', 'GET'])
def test():
    if request.method == 'POST':
        # user = request.values.get("mycouplet")
        user = request.form.get('mycouplet')
        print(user)

        big= ' '.join(user)
        big= big.split()

        en_arr, arr_len = converter.text_en_to_arr(big)

        test_g = [np.array([en_arr, ]), np.array([arr_len, ])]  # 序列
        output_ids = model.test(test_g, model_path, converter)  # 对输出文字id
        output = converter.arr_to_text(output_ids)  # 下联

        print('上联：%s；下联：%s' % (user, output))
        return render_template("one.html", user=user, output=output)
'''
    while True:

        english_speek = input("上联:")
        english_speek = ' '.join(english_speek)
        english_speek = english_speek.split()
        en_arr, arr_len = converter.text_en_to_arr(english_speek)

        test_g = [np.array([en_arr,]), np.array([arr_len,])]#序列
        output_ids = model.test(test_g, model_path, converter)#对输出文字id
        strs = converter.arr_to_text(output_ids)#下联
        print('下联:',strs)
        '''
http_server = WSGIServer(('', 8000), app)
# http_server = WSGIServer(('', 63342),app)
http_server.serve_forever()

if __name__ == '__main__':
    tf.app.run()
    app.run()