# coding: utf-8

# 嗯……要不是因为HCDK，我也不会写这东西
# 之前的v2.1已经够漂亮了，只可惜那只适用于初二
# 这个的话，就用pop随便糊了

version = 'v3.0'

print('计算科平')
print(f'版本: {version} 初三特供版')

# 获取分数
subjects = '语文 数学 英语 物理 化学 政治 历史 地生 体育 生物实验+物化实验'
subjects_list = subjects.split(' ')
got = input(f'输入各科分数：\n格式：{subjects}\n')
# got = '95 113 110 76 66 72 72 99 58 15'

# 分段
pri_grades = got.split(' ')

# 保存科平
avg_grades = []
all_avg = 0

# 计算每科科平
times = 0   # 计次
for i in pri_grades:
    times += 1

    if times <= 3:
        res = int(i)/120*100
    elif times == 4:
        res = int(i)/80*100
    elif times == 5:
        res = int(i)/70*100
    elif 6 <= times <= 7:
        res = int(i)/80*100
    elif times == 8:
        res = int(i)/100*100
    elif times == 9:
        res = int(i)/60*100
    elif times == 10:
        res = int(i)/15*100
    else:
        assert False
    avg_grades.append(res)
    all_avg += res
    print(f'{subjects_list[times-1]}: {res}')

print(f'总科平{all_avg/10}')
input('按回车退出')
