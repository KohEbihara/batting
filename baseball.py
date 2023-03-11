import random


INNING = 9
# 延長イニング
EXIN = 3

# Aの打率
A_AVE = 0.4
# Bの2塁打率
A_2_RATE = 0.4
# Bの3塁打率
A_3_RATE = 0.1
# Bの本塁打率
A_HR_RATE = 0.1

# Bの打率
B_AVE = 0.23
# Bの2塁打率
B_2_RATE = 0.4
# Bの3塁打率
B_3_RATE = 0.1
# Bの本塁打率
B_HR_RATE = 0.1


# スコアボード
score_board = []
# ベース
base_board = []

# スコアボードに数値を入れる
def init_board(point):
    global score_board
    score_board.append(point)

# スコアボードを見せる
def show_board():
    global score_board

    if (len(score_board)/2) > (len(score_board)//2):
        len_1 = (len(score_board)//2 + 1)
    else:
        len_1 = len(score_board)//2
    # イニング
    if len_1 == 0:
        print("     " + "|")
    else:
        print("     ",end="|")
    for i in range(len_1):
        if i == len_1-1:
            print(str(i+1) + "|")
        else:
            print(i+1,end="|")

    # teamA
    if len_1 == 0:
        print("teamA" + "|")
    else:
        print("teamA",end="|")
    for i in range(len_1):
        if i == len_1-1:
            print(str(score_board[2*i]) + "|")
        else:
            print(score_board[2*i],end="|")
    # teamB
    if len(score_board)//2 == 0:
        print("teamB" + "|")
    else:
        print("teamB",end="|")
    for j in range((len(score_board)//2)):
        if j == (len(score_board)//2)-1:
            print(str(score_board[2*j+1]) + "|")
        else:
            print(score_board[2*j+1],end="|")

# ベースのリセット
def init_base():
    global base_board
    base_board = []
    for i in range(3):
        base_board.append(0)

# 得点のチェック
def score_check(result):
    global base_board
    count = 0
    # 単打 or 犠打
    if (result == 1):
    # or (result == -1)
        if base_board[2] == 1:
            count += 1
    # 二塁打
    if result == 2:
        if base_board[1] == 1:
            count += 1
        if base_board[2] == 1:
            count += 1
    # 三塁打
    if result == 3:
        if base_board[0] == 1:
            count += 1
        if base_board[1] == 1:
            count += 1
        if base_board[2] == 1:
            count += 1
    # 本塁打
    if result == 4:
        count += 1
        if base_board[0] == 1:
            count += 1
        if base_board[1] == 1:
            count += 1
        if base_board[2] == 1:
            count += 1
    return count

# ベースにいるランナーの管理
def base(result):
    global base_board

    # 犠打or犠飛
    # if result == -1:
    #     if base_board[2] == 1:
    #         base_board[2] = 0
    #     if base_board[1] == 1:
    #         base_board[2] = 1
    #         base_board[1] = 0
    #     if base_board[0] == 1:
    #         base_board[1] = 1
    #         base_board[0] = 0

    # 単打
    if result == 1:
        if base_board[2] == 1:
            base_board[2] = 0
        if base_board[1] == 1:
            base_board[2] = 1
            base_board[1] = 0
        if base_board[0] == 1:
            base_board[1] = 1
            base_board[0] = 0
        base_board[0] = 1

    # 二塁打
    if result == 2:
        if base_board[2] == 1:
            base_board[2] = 0
        if base_board[1] == 1:
            base_board[1] = 0
        if base_board[0] == 1:
            base_board[2] = 1
            base_board[0] = 0
        base_board[1] = 1
        
    # 三塁打
    if result == 3:
        if base_board[2] == 1:
            base_board[2] = 0
        if base_board[1] == 1:
            base_board[1] = 0
        if base_board[0] == 1:
            base_board[0] = 0
        base_board[2] = 1
    
    if result == 4:
        if base_board[2] == 1:
            base_board[2] = 0
        if base_board[1] == 1:
            base_board[1] = 0
        if base_board[0] == 1:
            base_board[0] = 0

# ベースにいるランナーの表示
def show_base():
    global base_board
    # 2塁ランナー
    if base_board[1] == 1:
        print("---o---")
    else:
        print("--- ---")
    # 1,3塁ランナー
    if base_board[0] == 1 and base_board[2] == 1:
        print("--o-o--")
    elif base_board[0] == 1 and base_board[2] == 0:
        print("-- -o--")
    elif base_board[0] == 0 and base_board[2] == 1:
        print("--o- --")
    else:
        print("-- - --")
    # バッター
    print("-------")

# 合計点を表示
def sum_point_show(sum_a,sum_b):
    print("TEAM_A:" + str(sum_a) + " - " + "TEAM_B:" + str(sum_b))

# 結果を表示
def result_select(result):
    # if result == -1:
    #     out_2 = ["犠打","犠飛"]
    #     rand = random.randrange(len(out_2))
    #     print(str(out_2[rand]))
    if result == 0:
        out = ["三振","投ゴロ","一ゴロ","二ゴロ","三ゴロ","遊ゴロ","三振","投ゴロ","一ゴロ","二ゴロ","三ゴロ","遊ゴロ","捕飛","一飛","二飛","三飛","遊飛","左飛","中飛","右飛",]
        rand = random.randrange(len(out))
        print(str(out[rand]))
    if result == 1:
        hit = ["左安","中安","右安","左安","中安","右安","遊安",]
        rand = random.randrange(len(hit))
        print(str(hit[rand]))
    if result == 2:
        hit_2 = ["左2","中2","右2","左中2","右中2",]
        rand = random.randrange(len(hit_2))
        print(str(hit_2[rand]))
    if result == 3:
        hit_3 = ["中3","右3","左中3","右中3",]
        rand = random.randrange(len(hit_3))
        print(str(hit_3[rand]))
    if result == 4:
        homerun = ["左本","中本","右本","左中本","右中本",]
        rand = random.randrange(len(homerun))
        print(str(homerun[rand]))

# アウトカウントを表示
def show_out_count(out_count):
    if out_count == 0:
        print("out|")
    else:
        print("out" , end="|")
        for i in range(out_count):
            if i == out_count-1:
                print("o")
            else:
                print("o" , end="")

# Aのバッター
def batter_a(count_a):
    number = count_a % 9 + 1
    batter_name = ["ヌートバー","近藤","大谷","村上","吉田","牧","岡本","甲斐","源田",]
    print(str(number) + ":" + str(batter_name[number-1]))

# Bのバッター
def batter_b(count_b):
    number = count_b % 9 + 1
    batter_name = ["鳥谷","平野","マートン","ブラゼル","金本","新井","城島","江越","メッセンジャー",]
    print(str(number) + ":" + str(batter_name[number-1]))

# Aの打率
def team_a_rate(rand):
    if rand < A_AVE*A_HR_RATE:
        result = 4
    elif rand < A_AVE*A_3_RATE:
        result = 3
    elif rand < A_AVE*A_2_RATE:
        result = 2
    elif rand < A_AVE:
        result = 1
    # elif rand < 6.7:
    #     result = -1
    else:
        result = 0
    
    return result
# Bの打率
def team_b_rate(rand):
    if rand < B_AVE*B_HR_RATE:
        result = 4
    elif rand < B_AVE*B_3_RATE:
        result = 3
    elif rand < B_AVE*B_2_RATE:
        result = 2
    elif rand < B_AVE:
        result = 1
    # elif rand < 4.0:
    #     result = -1
    else:
        result = 0
    
    return result


    
    


# 試合
sum_a = 0
sum_b = 0
count_a = 0
count_b = 0

for i in range(INNING*2):
    # イニング
    if i == INNING*2 -1:
        if sum_a < sum_b:
            break
    init_base()
    show_board()
    out_count = 0
    inning_count = 0
    # 1バッター
    while out_count < 3:
        sum_point_show(sum_a,sum_b)
        rand = random.random()

        if i % 2 == 0:
            result = team_a_rate(rand)
        else:
            result = team_b_rate(rand)
        

        if result <= 0:
            out_count += 1

        if i % 2 == 0:
            batter_a(count_a)
        else:
            batter_b(count_b)
        
        
        if i % 2 == 0:
            sum_a += score_check(result)
            count_a += 1
        else:
            sum_b += score_check(result)
            count_b += 1

        inning_count += score_check(result)
        base(result)
        result_select(result)
        show_base()
        show_out_count(out_count)
        # サヨナラ勝ち
        if i == INNING*2-1:
            if sum_a != sum_b:
                break
    # end1バッター
    init_board(inning_count)
# endイニング
# 延長
if sum_a == sum_b:
    for j in range(EXIN*2):
        init_base()
        show_board()
        out_count = 0
        inning_count = 0
        # 1バッター
        while out_count < 3:
            sum_point_show(sum_a,sum_b)
            rand = random.random()
            if i % 2 == 0:
                result = team_a_rate(rand)
            else:
                result = team_b_rate(rand)

            if result == 0:
                out_count += 1

            if i % 2 == 0:
                batter_a(count_a)
            else:
                batter_b(count_b)
            
            
            if i % 2 == 0:
                sum_a += score_check(result)
                count_a += 1
            else:
                sum_b += score_check(result)
                count_b += 1

            inning_count += score_check(result)
            base(result)
            result_select(result)
            show_base()
            show_out_count(out_count)
            # サヨナラ勝ち
            if j % 2 == 1:
                if sum_a != sum_b:
                    break
        # end1バッター
        init_board(inning_count)
        if j % 2 == 1:
            if sum_a != sum_b:
                break
    # endイニング

show_board()
sum_point_show(sum_a,sum_b)