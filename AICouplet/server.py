from flask import Flask, jsonify, request, render_template, url_for  # 把模板渲染出来
import os
import tensorflow as tf
import numpy as np
from read_utils import TextConverter
from model import Model,Config

app = Flask(__name__)
app.debug=True

@app.route('/couplet')
def hello():
    return render_template("index.html")

@app.route('/success/?<string:output>')
def success(output):
    return 'couplet is %s'%output

@app.route('/test',methods=['POST','GRT'])
def test():
    if request.method == 'POST':
        user_couplet = request.values.get("mycouplet")
        mycouplet = user_couplet;
        user_couplet = ' '.join(user_couplet)
        user_couplet = user_couplet.split()
        en_arr, arr_len = converter.text_en_to_arr(user_couplet)
        test_g = [np.array([en_arr,]), np.array([arr_len,])]
        output_ids = model.test(test_g, model_path, converter)
        output_couplet = converter.arr_to_text(output_ids)
        return render_template("index.html", user_couplet=mycouplet, output_couplet=output_couplet)

if __name__ == '__main__':

    model_path = os.path.join('models', Config.file_name)
    converter = TextConverter(vocab_dir='data/vocabs', max_vocab=Config.vocab_size, seq_length = Config.seq_length)
    print('vocab lens:',converter.vocab_size)
    # 加载上一次保存的模型
    model = Model(Config)
    checkpoint_path = tf.train.latest_checkpoint(model_path)
    if checkpoint_path:
        model.load(checkpoint_path)
    # app.run()
    app.jinja_env.auto_reload = True  #debug模式，使css的修改不用重启服务器也能生效
    app.run(debug=True)
