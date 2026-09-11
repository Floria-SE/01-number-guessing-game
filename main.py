import random

print("数当てゲーム！\n1~100の数字を当ててください\n\n")

answer = random.randint(1,100)

play_times = 0

while True:
    
    input_number = input("整数を入力してください：")
    try:
        input_number = int(input_number)
    except ValueError:
        print("\n”整数”を入力してください")
        continue
    
    if input_number < 1 or input_number > 100:
        print("\n1~100の数字を入力してください") 
        continue
    
    play_times += 1
    
    if input_number < answer:
        print("もっと大きいです\n")
    elif input_number > answer:
        print("もっと小さいです\n")
    else:
        print("正解です！")
        print(f"\n\n{play_times}回で正解しました！")
        break
