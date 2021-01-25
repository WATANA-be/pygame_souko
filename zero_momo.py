momo = input('桃は何個買いますか')
num_momo = int(momo)　#桃の個数を整数値に変換

mikan = input('みかんは何個買いますか')
num_mikan = int(mikan)

total_momo = num_momo * 100
total_mikan = num_mikan * 40
total = total_momo + total_mikan

print('桃',num_momo,'個とみかん',num_mikan,'個で',total,'円です')