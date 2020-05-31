# 动态规划
import numpy as np

# 定义重量 = 平均股价
weight = {}
weight["abc001"] = 14.32
weight["abc002"] = 52.30
weight["abc003"] = 4.76
weight["abc004"] = 82.31
weight["abc005"] = 6.67
weight["abc006"] = 55.76
weight["abc007"] = 365.57
weight["abc008"] = 27.18
weight["abc009"] = 4.05
weight["abc010"] = 6.43

# 定义价值 = 最大收益
worth = {}
worth["abc001"] = 6.45
worth["abc002"] = 20.98
worth["abc003"] = 3.21
worth["abc004"] = 22.01
worth["abc005"] = 2.04
worth["abc006"] = 31.4
worth["abc007"] = 347.5
worth["abc008"] = 16.32
worth["abc009"] = 1.02
worth["abc010"] = 0.77


# 存放行标对应的物品名:
table_name = {}
table_name[0] = "abc001"
table_name[1] = "abc002"
table_name[2] = "abc003"
table_name[3] = "abc004"
table_name[4] = "abc005"
table_name[5] = "abc006"
table_name[6] = "abc007"
table_name[7] = "abc008"
table_name[8] = "abc009"
table_name[9] = "abc010"

# 创建矩阵,用来保存价值表
table = np.zeros((len(weight), 20000))

# 创建矩阵，用来保存每个单元格中的价值是如何得到的（物品名）
table_class = np.zeros((len(weight), 20000), dtype=np.dtype((np.str_, 500)))

for i in range(0, len(weight)):
    for j in range(0, 20000):
        # 获取重量
        this_weight = int(weight[table_name[i]])
        # 获得价值
        this_worth = int(worth[table_name[i]])
        # 获取上一个单元格 (i-1,j)的值
        if (i > 0):
            before_worth = table[i - 1, j]
            # 获取（i-1,j-重量）
            temp = 0
            if (this_weight <= j):
                temp = table[i - 1, j - this_weight]
            # (i-1,j-this_weight)+求当前商品价值
            # 判断this_worth能不能用，即重量有没有超标，如果重量超标了是不能加的
            synthesize_worth = 0
            if (this_weight - 1 <= j):
                synthesize_worth = this_worth + temp
            # 与上一个单元格比较,哪个大写入哪个
            if (synthesize_worth > before_worth):
                table[i, j] = synthesize_worth
                if (temp == 0):
                    # 他自己就超过了
                    table_class[i][j] = table_name[i]
                else:
                    # 他自己和(i-1,j-this_weight)
                    table_class[i][j] = table_name[i] + "," + table_class[i - 1][j - this_weight]
            else:
                table[i, j] = before_worth
                table_class[i][j] = table_class[i - 1][j]
        else:
            # 没有（i-1,j）那更没有(i-1,j-重量),就等于当前商品价值,或者重量不够，是0
            if (this_weight - 1 <= j):
                table[i, j] = this_worth
                table_class[i][j] = table_name[i]
print(table)

print("--------------------------------------")

print(table_class[-1][-1])