# Word Jumble猜单词游戏
import sys
import random


def main() -> int:
    WORDS = ('dog', 'cat', 'tree', 'book', 'computer',
             'house', 'table', 'chair', 'person', 'world')

    print(
        '''
        欢迎参加猜单词游戏
        把字母组合成一个正确的单词. 
        '''
    )

    is_continue = 'y'

    while is_continue == 'y' or is_continue == 'Y':  # 循环
        # 从序列中随机挑出一个单词
        word = random.choice(WORDS)
        # 一个用于判断玩家是否猜对的变量
        correct = word
        # 创建乱序后的单词
        jumble = ''

        # 打乱字母顺序方法一（复杂）
        while word:  # word不是空串循环
            # 根据word长度，产生word的随机位置
            position = random.randrange(len(word))
            # 将position位置字母组合到乱序后的单词
            jumble += word[position]
            # 通过切片，将position位置字母从原单词中删除
            word = word[:position] + word[(position + 1):]

        # 打乱字母顺序方法二（简单）
        # convert the string into a list of characters
        char_list = list(word)
        random.shuffle(char_list)     # shuffle the list of characters randomly
        # convert the list of characters back into a string
        jumble = ''.join(char_list)

        print('乱序后的单词:', jumble)

        is_continue = 'N'  # 原书中的bug，没有将iscontinue设置成N，导致程序死循环

        guess = input('\n请你猜: ')
        while guess != correct and guess != '':
            print('对不起，不正确.')
            guess = input('继续猜:')

        if guess == correct:
            print('真棒，你猜对了!')
            is_continue = input('\n是否继续(y/N):')  # 是否继续游戏


if __name__ == '__main__':
    sys.exit(main())
