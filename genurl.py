# _*_ coding utf-8 _*_
"""
    这是一个用来生成视频播放列表 url 的小程序
"""
import argparse

parser = argparse.ArgumentParser(description='生成一个组合 URL 清单文件')
parser.add_argument('-u', '--url', type=str, metavar="", required=True, help='第一个 url 字符串片段')
parser.add_argument('-s', '--start_number', type=int, metavar="", help='清单条目的起始序号，不写，默认为 0')
parser.add_argument('-e', '--end_number', type=int, metavar="", required=True, help='清单条目的终止序号')
parser.add_argument('-f', '--file_name', type=str, metavar="", help='指定文件名，不指定时，默认为“l.txt"')
args = parser.parse_args()


def gen_list(url, end, start=None, file_name=None):
    with open((file_name if file_name is not None else 'l.txt'), 'w') as f:
        if start is None:
            for i in range(0, end):
                full_url = url + str(i + 1) + '\n'
                f.write(full_url)
        else:
            for i in range(start - 1, end):
                full_url = url + str(i + 1) + '\n'
                f.write(full_url)


if __name__ == "__main__":
    gen_list(args.url, args.end_number, args.start_number, args.file_name)
