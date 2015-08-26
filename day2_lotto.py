__author__ = 'DongJu'
import random

def main():
    lottoList = random.sample(range(1,46),6)
    print("lotto number : ", lottoList)
if __name__ == '__main__':
    main()