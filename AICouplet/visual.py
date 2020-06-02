import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate


log_file = "/home/cyd/Seq2seq_couplet/numlayers2-hiddendim128-drop0.8-lr0.01-batchsize32-log.txt"
draw_step = 100
f = open(log_file,"r")
lines = f.readlines()
f.close()

loss_list = []
step_list = []

max_loss = 100
for i in range(len(lines)):
    if i % 1 == 0:
        each_line = lines[i]
        each_line = each_line.strip()
        loss = each_line.split(",")[1].split(":")[1].strip()
        step = each_line.split(",")[0].split(":")[1].split("/")[0].strip()
        loss = float(loss)
        step = int(step)
        if loss < max_loss:
            max_loss = loss
            loss_list.append(loss)
            step_list.append(step)
            print(loss,step)

print(len(step_list))
print(len(loss_list))
plt.plot(step_list, loss_list, "")



# log_file = "/home/cyd/Seq2seq_couplet/numlayers2-hiddendim128-drop0.5-lr0.01-batchsize32-log.txt"
# draw_step = 100
# f = open(log_file,"r")
# lines = f.readlines()
# f.close()
#
# loss_list = []
# step_list = []
#
# max_loss = 100
# for i in range(len(lines)):
#     if i % 1 == 0:
#         each_line = lines[i]
#         each_line = each_line.strip()
#         loss = each_line.split(",")[1].split(":")[1].strip()
#         step = each_line.split(",")[0].split(":")[1].split("/")[0].strip()
#         loss = float(loss)
#         step = int(step)
#         if loss < max_loss:
#             max_loss = loss
#             loss_list.append(loss)
#             step_list.append(step)
#             print(loss,step)
#
# print(len(step_list))
# print(len(loss_list))
# plt.plot(step_list, loss_list, "")


# log_file = "/home/cyd/Seq2seq_couplet/numlayers2-hiddendim128-drop0.8-lr0.0001-batchsize32-log.txt"
# draw_step = 100
# f = open(log_file,"r")
# lines = f.readlines()
# f.close()
#
# loss_list = []
# step_list = []
#
# max_loss = 100
# for i in range(len(lines)):
#     if i % 1 == 0:
#         each_line = lines[i]
#         each_line = each_line.strip()
#         loss = each_line.split(",")[1].split(":")[1].strip()
#         step = each_line.split(",")[0].split(":")[1].split("/")[0].strip()
#         loss = float(loss)
#         step = int(step)
#         if loss < max_loss:
#             max_loss = loss
#             loss_list.append(loss)
#             step_list.append(step)
#             print(loss,step)
#
# print(len(step_list))
# print(len(loss_list))
# plt.plot(step_list, loss_list, "")


#设置x,y轴代表意思
plt.xlabel("Step")
plt.ylabel("Loss")
plt.legend(["best model"],loc = 1)
plt.savefig("best_model.jpg")
