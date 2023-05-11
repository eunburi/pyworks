import argparse
def get_args():
    parser = argparse.ArgumentParser(
        description="Jump The fIVE",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )


    parser.add_argument('text',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()  #명령줄 인수를 처리해서 반환함

def main():
    args = get_args()
    print(args.text)
    jumper = {'1':'9','2':'8','3':'7','4':'6','5':'0'
               ,'6':'4','7':'3','8':'2','9':'1'}

    # 방법1
    """
    for char in args.text:
        print(jumper.get(char,char),end='')
    """
    #방법2
    """
    new_text = ''
    for char in args.text:
        new_text += jumper.get(char, char)
    print(new_text)
    """
    """
    # 방법3
    new_text = []
    for char in args.text:
        new_text.append(jumper.get(char, char))
        print(''.join(new_text)) # 문자열.join()
    """

     # 방법
    print(''.join([jumper.get(char, char) for char in args.text]))
"""
    #정렬 기능 구현
    if args.sorted:
        items.sort()

    bringing = ''
    if num == 1:   # 명령행의 인수가 1개이면
        bringing = items[0] #bringing 변수에 1개 저장
    elif num ==2:
        bringing = ' and '.join(items)
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)

    print('You are bringing {}.'.format(bringing))
    """


if __name__ == '__main__':
    main()