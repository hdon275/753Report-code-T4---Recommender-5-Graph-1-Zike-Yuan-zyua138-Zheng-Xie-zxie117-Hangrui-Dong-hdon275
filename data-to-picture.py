import matplotlib.pyplot as plt

# 输入纵坐标轴数据与横坐标轴数据
train_loss_0 = [1987,1945,1960,1489,1809,1976,69,50,37]
# train_loss_1 = [1.48455,1.47393,1.45936,1.46971,1.45187,1.44827,1.77533,1.78345,1.78829]
# train_loss_01 = [0.6980,0.6940,0.6880,0.6760,0.6660,0.6540,0.6600,0.6540,0.6500
# ]
alpha = [0.1, 0.2, 0.3, 0.4, 0.5,0.6,0.7,0.8,0.9]

# 4 个 plot 函数画出 4 条线，线形为折线，每条线对应各自的标签 label
plt.plot(alpha, train_loss_0, '.-', label='early stop epoch')
# plt.plot(alpha, train_loss_1, '.-', label='validation loss')
# plt.plot(alpha, train_loss_01, '.-', label='validation accuracy')

plt.xticks(alpha)  # 设置横坐标刻度
plt.xticks(fontsize=13)
plt.yticks(fontsize=13)
font2 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         }
plt.xlabel('alpha', font2)
plt.ylabel('value', font2)
# # 将文件保存至文件中并且画出图
plt.legend(prop={'size': 14}) # 显示图例，即每条线对应 label 中的内容
plt.savefig('figure.png')
plt.show() # 显示图形

###################################################################################
# import matplotlib.pyplot as plt
#
# # 输入纵坐标轴数据与横坐标轴数据
# train_loss_0 = [1.55357,1.40599,1.30424,1.22567,1.19030,1.15079,1.10884,
#                 1.10618,1.09425,1.06832,1.04733,1.04584,1.03210,1.05669,
#                 1.02333,1.05268,1.05937,1.03560,1.01602,1.01911]
# train_loss_1 = [1.74121,1.54292,1.30937,1.14515,1.06258,0.95875,0.95960,
#                 0.91276,0.94551,0.88849,0.86761,0.88953,0.85747,0.87610,
#                 0.87333,0.85934,0.87404,0.88099,0.87177,0.88839]
# train_loss_01 = [1.57859,1.44480,1.34846,1.27293,1.23466,1.19032,1.14701,
#                  1.13854,1.12712,1.09252,1.07159,1.07258,1.05336,1.07484,
#                  1.04217,1.06783,1.07407,1.05372,1.02953,1.03496]
# epochs = [1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
#
# # 4 个 plot 函数画出 4 条线，线形为折线，每条线对应各自的标签 label
# plt.plot(epochs, train_loss_0, '.-', label='train loss 0')
# plt.plot(epochs, train_loss_1, '.-', label='train loss 1')
# plt.plot(epochs, train_loss_01, '.-', label='train loss 01')
#
# plt.xticks(epochs)  # 设置横坐标刻度
# plt.xticks(fontsize=13)
# plt.yticks(fontsize=13)
# font2 = {'family': 'Times New Roman',
#          'weight': 'normal',
#          'size': 20,
#          }
# plt.xlabel('epochs(*100)', font2)
# plt.ylabel('loss', font2)
# # # 将文件保存至文件中并且画出图
# plt.legend(prop={'size': 14}) # 显示图例，即每条线对应 label 中的内容
# plt.savefig('figure.png')
# plt.show() # 显示图形








